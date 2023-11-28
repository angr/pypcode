#!/usr/bin/env python3
# pylint:disable=import-outside-toplevel,wrong-import-position
"""
Benchmark disassembly and IR lifting performance for pypcode and other libraries.
"""

import argparse
import csv
import functools
import gc
import hashlib
import logging
import os
import pickle
import random
import sys
import time
from dataclasses import dataclass

from typing import cast, Any, Callable, Dict, Iterable, List, Tuple


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


try:
    import_start_time = time.time()

    import capstone  # type: ignore

    CAPSTONE_IMPORT_DURATION = time.time() - import_start_time
    del import_start_time
    HAVE_CAPSTONE = True
except ImportError:
    HAVE_CAPSTONE = False

try:
    import_start_time = time.time()

    import pypcode

    PYPCODE_IMPORT_DURATION = time.time() - import_start_time
    del import_start_time
    HAVE_PYPCODE = True
except ImportError:
    HAVE_PYPCODE = False

try:
    import_start_time = time.time()

    import archinfo
    import pyvex

    PYVEX_IMPORT_DURATION = time.time() - import_start_time
    del import_start_time
    HAVE_PYVEX = True
except ImportError:
    HAVE_PYVEX = False


@dataclass
class Block:
    """Block to translate"""

    addr: int
    data: bytes


@dataclass
class BenchmarkResult:
    """Result of a benchmark run"""

    startup_duration: float
    translation_duration: float


def get_file_hash(binary_path: str) -> str:
    log.info("Calculating sha256 of file '%s'", binary_path)
    m = hashlib.sha256()
    with open(binary_path, "rb") as f:
        m.update(f.read())
    d = m.hexdigest()
    log.info("sha256:%s", d)
    return d


def get_blocks(binary_path: str) -> List[Block]:
    blocks_file_path = f"blocks_{get_file_hash(binary_path)[0:8]}.cache"
    blocks: List[Block] = []

    if not os.path.exists(blocks_file_path):
        log.info("Recovering blocks from CFG...")

        try:
            import angr

            logging.getLogger("angr").setLevel(logging.WARNING)
            logging.getLogger("cle").setLevel(logging.WARNING)
            logging.getLogger("pyvex").setLevel(logging.WARNING)
            logging.getLogger("claripy").setLevel(logging.WARNING)
        except ImportError:
            log.error("Install angr to build list of blocks")
            sys.exit(1)

        p = angr.Project(binary_path, auto_load_libs=False)
        cfg = p.analyses[angr.analyses.CFGFast].prep(show_progressbar=True)(
            resolve_indirect_jumps=False, force_smart_scan=False
        )
        for n in cast(Iterable[angr.analyses.cfg.CFGNode], cfg.model.nodes()):
            if n.byte_string:
                blocks.append(Block(n.addr, n.byte_string))
        log.info("Saving blocks to file '%s' for subsequent benchmarks...", blocks_file_path)
        with open(blocks_file_path, "wb") as f:
            pickle.dump(blocks, f)
    else:
        log.info("Loading blocks from cache file '%s'...", blocks_file_path)
        with open(blocks_file_path, "rb") as f:
            blocks = pickle.load(f)

    return blocks


def benchmark_pypcode(blocks: List[Block], iter_ops: bool = False, iter_varnodes: bool = False) -> BenchmarkResult:
    assert pypcode is not None

    start_time = time.time()
    lang = langs = next(
        lang for arch in pypcode.Arch.enumerate() for lang in arch.languages if lang.id == "x86:LE:64:default"
    )
    ctx = pypcode.Context(lang)
    startup_duration = time.time() - start_time

    start_time = time.time()
    count = 0
    for block in blocks:
        t = ctx.translate(block.data, block.addr)
        if iter_ops and not iter_varnodes:
            for ins in t.instructions:
                for _ in ins.ops:
                    count += 1
        if iter_varnodes:
            for ins in t.instructions:
                for op in ins.ops:
                    for _ in op.inputs:
                        count += 1
    translation_duration = time.time() - start_time

    return BenchmarkResult(startup_duration, translation_duration)


def benchmark_pypcode_disassembly(blocks: List[Block]) -> BenchmarkResult:
    assert pypcode is not None

    start_time = time.time()
    ctx = pypcode.Context("x86:LE:64:default")
    startup_duration = time.time() - start_time

    start_time = time.time()
    size = 0
    for block in blocks:
        for ins in ctx.disassemble(block.data, block.addr).instructions:
            size += ins.length
    translation_duration = time.time() - start_time

    return BenchmarkResult(startup_duration, translation_duration)


def benchmark_pyvex(blocks: List[Block], **vex_args) -> BenchmarkResult:
    assert pyvex is not None

    start_time = time.time()
    arch = archinfo.ArchAMD64()
    startup_duration = time.time() - start_time

    start_time = time.time()
    for block in blocks:
        pyvex.lift(block.data, block.addr, arch, **vex_args)
    translation_duration = time.time() - start_time

    return BenchmarkResult(startup_duration, translation_duration)


def benchmark_capstone(blocks: List[Block], lite: bool = False) -> BenchmarkResult:
    assert capstone is not None

    start_time = time.time()
    md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
    startup_duration = time.time() - start_time

    start_time = time.time()
    size = 0
    if lite:
        for block in blocks:
            for ins in md.disasm_lite(block.data, block.addr):
                size += ins[1]
    else:
        for block in blocks:
            for ins in md.disasm(block.data, block.addr):
                size += ins.size
    translation_duration = time.time() - start_time

    return BenchmarkResult(startup_duration, translation_duration)


def gen_benchmarks_from_configurations(
    name: str, benchmark_func: Callable, configurations: List[Dict[str, Any]]
) -> List[Tuple[str, Callable]]:
    benchmarks: List[Tuple[str, Callable]] = []
    for config in configurations:
        name_append = ""
        if config:
            name_append += f" ({', '.join(f'{k}={v}' for k, v in config.items())})"
        benchmarks.append((name + name_append, functools.partial(benchmark_func, **config)))
    return benchmarks


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "-b", "--binary", default=sys.executable, help="Binary to benchmark with (Python interpreter by default)"
    )
    ap.add_argument(
        "-c",
        "--coverage",
        default=1,
        type=float,
        help="Percentage of blocks to include in benchmark in (0,1] (default=1)",
    )
    ap.add_argument(
        "--skip", nargs="*", default=[], help="Skip benchmarks for a particular package (pypcode, pyvex, capstone)"
    )
    ap.add_argument("--csv", help="Save results to CSV file")
    args = ap.parse_args()

    # Display import times (use python -Ximporttime for more accurate import profiling)
    imports = []
    if HAVE_CAPSTONE:
        imports.append(("capstone", capstone.__version__, CAPSTONE_IMPORT_DURATION))
    if HAVE_PYPCODE:
        imports.append(("pypcode", "1.1.2", PYPCODE_IMPORT_DURATION))
    if HAVE_PYVEX:
        imports.append(("pyvex", pyvex.__version__, PYVEX_IMPORT_DURATION))
    for name, version, import_duration in imports:
        log.info("%s v%s took %.2f ms to import", name, version, import_duration * 1000)

    benchmarks: List[Tuple[str, Callable]] = []
    if HAVE_CAPSTONE and "capstone" not in args.skip:
        benchmarks.extend(
            gen_benchmarks_from_configurations(
                "capstone Disassemble",
                benchmark_capstone,
                [
                    {},
                    {"lite": True},
                ],
            )
        )
    if HAVE_PYPCODE and "pypcode" not in args.skip:
        # benchmarks.append(("pypcode Disassemble", benchmark_pypcode_disassembly))
        benchmarks.extend(
            gen_benchmarks_from_configurations(
                "pypcode Lift",
                benchmark_pypcode,
                [
                    {},
                    {"iter_ops": True},  # Iterate over all ops
                    {"iter_varnodes": True},  # Iterate over all ops and varnodes
                ],
            )
        )
    if HAVE_PYVEX and "pyvex" not in args.skip:
        benchmarks.extend(
            gen_benchmarks_from_configurations(
                "pyvex Lift",
                benchmark_pyvex,
                [
                    {},
                    {"opt_level": -1},
                    {"opt_level": 0},
                    {"skip_stmts": True},
                    {"collect_data_refs": True},
                ],
            )
        )
    if not benchmarks:
        log.error("No benchmarks to run. Install pypcode to run a benchmark.")
        sys.exit(1)

    log.info("Using blocks from binary '%s' for benchmarking", args.binary)
    blocks = get_blocks(args.binary)
    num_blocks = len(blocks)

    # Handle reduced block sampling
    assert 0 < args.coverage <= 1, "Specified coverage percentage not in range (0, 1]"
    if args.coverage < 1:
        blocks = random.choices(blocks, k=int(num_blocks * args.coverage))
        num_blocks = len(blocks)

    if num_blocks == 0:
        log.error("No blocks included in benchmark!")
        sys.exit(1)

    blocks_total_size = sum(len(block.data) for block in blocks)
    log.info("Benchmark includes %d blocks totaling %.1f KiB", num_blocks, blocks_total_size / 1024)

    gc.collect()
    results: List[Tuple[str, BenchmarkResult]] = []
    gc.disable()
    for name, benchmark in benchmarks:
        log.info("Benchmarking %s performance...", name)
        results.append((name, benchmark(blocks)))
    gc.enable()

    rows = [["Benchmark", "Startup ms", "Process s", "KiB/s", "kBlock/s", "us/Block"]]
    num_cols = len(rows[0])

    for name, result in results:
        rows.append(
            [
                name,
                f"{result.startup_duration * 1000:.3f}",
                f"{result.translation_duration:.3f}",
                f"{(blocks_total_size / result.translation_duration) / 1024:.2f}",
                f"{num_blocks / result.translation_duration / 1000:.2f}",
                f"{result.translation_duration / num_blocks * 1000000:.3f}",
            ]
        )

    col_widths = [max(len(row[c]) for row in rows) for c in range(num_cols)]
    row = rows[0]
    header = " | ".join(row[c].ljust(col_widths[c]) for c in range(num_cols))
    log.info("-" * len(header))
    log.info("%s", header)
    log.info("-" * len(header))
    for row in rows[1:]:
        log.info("%s", " | ".join(row[c].ljust(col_widths[c]) for c in range(num_cols)))

    if args.csv:
        with open(args.csv, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            for row in rows:
                writer.writerow(row)


if __name__ == "__main__":
    main()
