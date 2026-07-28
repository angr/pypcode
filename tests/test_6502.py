from pypcode import Context, OpCode


def _ops(code: bytes, language: str = "6502:LE:16:default"):
    return Context(language).translate(code, base_address=0x8000, max_instructions=1).ops


def _matching(code: bytes, opcode: OpCode, language: str = "6502:LE:16:default"):
    return [op for op in _ops(code, language) if op.opcode == opcode]


def _varnode_key(varnode):
    return varnode.space.name, varnode.offset, varnode.size


def _signed(value: int, size: int) -> int:
    sign = 1 << (size * 8 - 1)
    return value - (sign << 1) if value & sign else value


def _evaluate_arithmetic(ops, accumulator: int, carry_flag: int) -> dict[str, int]:
    values = {
        ("register", 0x00, 1): accumulator,
        ("register", 0x36, 1): carry_flag,
    }
    registers = {"A": accumulator, "C": carry_flag}

    def read(varnode):
        mask = (1 << (varnode.size * 8)) - 1
        if varnode.space.name == "const":
            return varnode.offset & mask
        return values.get(_varnode_key(varnode), 0) & mask

    for operation in ops:
        if operation.opcode == OpCode.IMARK:
            continue
        assert operation.output is not None
        inputs = [read(varnode) for varnode in operation.inputs]
        output_mask = (1 << (operation.output.size * 8)) - 1
        opcode = operation.opcode
        if opcode == OpCode.COPY:
            result = inputs[0]
        elif opcode == OpCode.INT_ADD:
            result = inputs[0] + inputs[1]
        elif opcode == OpCode.INT_SUB:
            result = inputs[0] - inputs[1]
        elif opcode == OpCode.INT_CARRY:
            input_mask = (1 << (operation.inputs[0].size * 8)) - 1
            result = int(inputs[0] + inputs[1] > input_mask)
        elif opcode == OpCode.INT_SCARRY:
            sign = 1 << (operation.inputs[0].size * 8 - 1)
            truncated = (inputs[0] + inputs[1]) & output_mask
            result = int(bool((~(inputs[0] ^ inputs[1]) & (inputs[0] ^ truncated)) & sign))
        elif opcode == OpCode.INT_SBORROW:
            sign = 1 << (operation.inputs[0].size * 8 - 1)
            truncated = (inputs[0] - inputs[1]) & output_mask
            result = int(bool(((inputs[0] ^ inputs[1]) & (inputs[0] ^ truncated)) & sign))
        elif opcode == OpCode.INT_LESS:
            result = int(inputs[0] < inputs[1])
        elif opcode == OpCode.INT_SLESS:
            result = int(_signed(inputs[0], operation.inputs[0].size) < _signed(inputs[1], operation.inputs[1].size))
        elif opcode == OpCode.INT_EQUAL:
            result = int(inputs[0] == inputs[1])
        elif opcode == OpCode.BOOL_NEGATE:
            result = int(not inputs[0])
        elif opcode == OpCode.BOOL_AND:
            result = int(bool(inputs[0]) and bool(inputs[1]))
        elif opcode == OpCode.BOOL_OR:
            result = int(bool(inputs[0]) or bool(inputs[1]))
        elif opcode == OpCode.BOOL_XOR:
            result = int(bool(inputs[0]) ^ bool(inputs[1]))
        else:
            raise AssertionError(f"unsupported arithmetic test operation: {opcode}")
        result &= output_mask
        values[_varnode_key(operation.output)] = result
        name = operation.output.getRegisterName()
        if name:
            registers[name] = result

    return registers


def _evaluate_dataflow(
    ops,
    *,
    registers: dict[str, int] | None = None,
    memory: dict[int, int] | None = None,
):
    values: dict[tuple[str, int, int], int] = {}
    registers = dict(registers or {})
    memory = dict(memory or {})
    control_target = None

    def mask(size):
        return (1 << (size * 8)) - 1

    def read(varnode):
        if varnode.space.name == "const":
            return varnode.offset & mask(varnode.size)
        if varnode.space.name == "register":
            name = varnode.getRegisterName()
            if name:
                return registers.get(name, 0) & mask(varnode.size)
        return values.get(_varnode_key(varnode), 0) & mask(varnode.size)

    for operation in ops:
        opcode = operation.opcode
        if opcode == OpCode.IMARK:
            continue
        if opcode == OpCode.STORE:
            address = read(operation.inputs[1])
            value = read(operation.inputs[2])
            for index in range(operation.inputs[2].size):
                memory[(address + index) & 0xFFFF] = (value >> (index * 8)) & 0xFF
            continue
        if opcode in {OpCode.BRANCHIND, OpCode.CALLIND, OpCode.RETURN}:
            control_target = read(operation.inputs[0])
            continue
        if opcode in {OpCode.BRANCH, OpCode.CALL}:
            control_target = operation.inputs[0].offset
            continue

        assert operation.output is not None
        inputs = [read(varnode) for varnode in operation.inputs]
        output_mask = mask(operation.output.size)
        if opcode == OpCode.COPY:
            result = inputs[0]
        elif opcode == OpCode.INT_ADD:
            result = inputs[0] + inputs[1]
        elif opcode == OpCode.INT_SUB:
            result = inputs[0] - inputs[1]
        elif opcode == OpCode.INT_AND:
            result = inputs[0] & inputs[1]
        elif opcode == OpCode.INT_OR:
            result = inputs[0] | inputs[1]
        elif opcode == OpCode.INT_LEFT:
            result = inputs[0] << inputs[1]
        elif opcode == OpCode.INT_ZEXT:
            result = inputs[0]
        elif opcode == OpCode.SUBPIECE:
            result = inputs[0] >> (inputs[1] * 8)
        elif opcode == OpCode.INT_EQUAL:
            result = int(inputs[0] == inputs[1])
        elif opcode == OpCode.INT_SLESS:
            result = int(_signed(inputs[0], operation.inputs[0].size) < _signed(inputs[1], operation.inputs[1].size))
        elif opcode == OpCode.LOAD:
            address = inputs[1]
            result = sum(
                memory.get((address + index) & 0xFFFF, 0) << (index * 8) for index in range(operation.output.size)
            )
        else:
            raise AssertionError(f"unsupported dataflow test operation: {opcode}")
        result &= output_mask
        values[_varnode_key(operation.output)] = result
        name = operation.output.getRegisterName()
        if name:
            registers[name] = result

    return registers, memory, control_target


def test_adc_accounts_for_incoming_carry_and_signed_overflow():
    ops = _ops(b"\x69\x00")

    assert sum(op.opcode == OpCode.INT_CARRY for op in ops) == 2
    assert sum(op.opcode == OpCode.INT_SCARRY for op in ops) == 2
    assert any(op.opcode == OpCode.BOOL_OR and op.output.getRegisterName() == "C" for op in ops)
    assert any(op.opcode == OpCode.BOOL_XOR and op.output.getRegisterName() == "V" for op in ops)


def test_sbc_produces_no_borrow_carry_and_signed_overflow():
    ops = _ops(b"\xe9\x00")

    assert sum(op.opcode == OpCode.INT_SBORROW for op in ops) == 2
    assert sum(op.opcode == OpCode.INT_LESS for op in ops) == 2
    assert any(op.opcode == OpCode.BOOL_AND and op.output.getRegisterName() == "C" for op in ops)
    assert any(op.opcode == OpCode.BOOL_XOR and op.output.getRegisterName() == "V" for op in ops)


def test_adc_and_sbc_match_every_binary_input_combination():
    for opcode in (0x69, 0xE9):
        for operand in range(0x100):
            ops = _ops(bytes((opcode, operand)))
            for accumulator in range(0x100):
                for carry_in in (0, 1):
                    actual = _evaluate_arithmetic(ops, accumulator, carry_in)
                    if opcode == 0x69:
                        mathematical = accumulator + operand + carry_in
                        result = mathematical & 0xFF
                        carry_out = int(mathematical > 0xFF)
                        overflow = int(bool((~(accumulator ^ operand) & (accumulator ^ result)) & 0x80))
                    else:
                        mathematical = accumulator - operand - (1 - carry_in)
                        result = mathematical & 0xFF
                        carry_out = int(mathematical >= 0)
                        overflow = int(bool(((accumulator ^ operand) & (accumulator ^ result)) & 0x80))
                    assert actual == {
                        "A": result,
                        "C": carry_out,
                        "V": overflow,
                        "Z": int(result == 0),
                        "N": int(bool(result & 0x80)),
                    }, (opcode, accumulator, operand, carry_in)


def test_65c02_zero_page_indirect_adc_and_sbc_share_fixed_arithmetic():
    for code, flag_opcode in ((b"\x72\xff", OpCode.INT_CARRY), (b"\xf2\xff", OpCode.INT_SBORROW)):
        ops = _ops(code, "65C02:LE:16:default")
        assert sum(op.opcode == flag_opcode for op in ops) == 2
        assert sum(op.opcode == OpCode.LOAD and op.output.size == 1 for op in ops) == 3


def test_stack_operations_update_canonical_sp_and_use_page_one_byte_accesses():
    pha_ops = _ops(b"\x48")
    stores = [op for op in pha_ops if op.opcode == OpCode.STORE]
    assert len(stores) == 1
    assert stores[0].inputs[1].getRegisterName() == "SP"
    assert stores[0].inputs[2].size == 1
    assert any(
        op.opcode == OpCode.INT_OR and op.output.getRegisterName() == "SP" and op.inputs[1].offset == 0x100
        for op in pha_ops
    )
    assert any(op.opcode == OpCode.INT_AND and op.output.size == 2 and op.inputs[1].offset == 0xFF for op in pha_ops)


def test_php_stacks_a_set_break_bit_even_when_synthetic_b_is_clear():
    registers, memory, _target = _evaluate_dataflow(
        _ops(b"\x08"),
        registers={
            "SP": 0x01FF,
            "N": 1,
            "V": 0,
            "B": 0,
            "D": 1,
            "I": 0,
            "Z": 1,
            "C": 0,
        },
    )

    assert memory[0x01FF] == 0xBA
    assert registers["B"] == 0
    assert registers["SP"] == 0x01FE


def test_jsr_pushes_pc_minus_one_as_two_wrapping_bytes():
    ops = _ops(b"\x20\x00\x90")
    stores = [op for op in ops if op.opcode == OpCode.STORE]

    assert len(stores) == 2
    assert all(op.inputs[2].size == 1 for op in stores)
    assert sum(op.opcode == OpCode.INT_SUB and op.inputs[0].getRegisterName() == "SP" for op in ops) == 2
    pushed_pc = next(op for op in ops if op.opcode == OpCode.INT_SUB and op.output.size == 2)
    assert [(value.offset, value.size) for value in pushed_pc.inputs] == [(0x8003, 2), (1, 2)]

    registers, memory, target = _evaluate_dataflow(ops, registers={"SP": 0x0100})
    assert registers["SP"] == 0x01FE
    assert memory == {0x0100: 0x80, 0x01FF: 0x02}
    assert target == 0x9000


def test_brk_pushes_pc_plus_two_and_status_as_three_wrapping_bytes():
    ops = _ops(b"\x00")
    stores = [op for op in ops if op.opcode == OpCode.STORE]

    assert len(stores) == 3
    assert all(op.inputs[2].size == 1 for op in stores)
    assert sum(op.opcode == OpCode.INT_SUB and op.inputs[0].getRegisterName() == "SP" for op in ops) == 3
    pushed_pc = next(op for op in ops if op.opcode == OpCode.INT_ADD and op.output.size == 2)
    assert [(value.offset, value.size) for value in pushed_pc.inputs] == [(0x8001, 2), (1, 2)]


def test_rts_pops_wrapping_bytes_and_adds_one_to_target():
    ops = _ops(b"\x60")
    loads = [op for op in ops if op.opcode == OpCode.LOAD]
    returned = next(op for op in ops if op.opcode == OpCode.RETURN)

    assert len(loads) == 2
    assert all(op.output.size == 1 for op in loads)
    assert sum(op.opcode == OpCode.INT_ADD and op.inputs[0].getRegisterName() == "SP" for op in ops) == 2
    return_varnode = returned.inputs[0]
    assert any(
        op.opcode == OpCode.INT_ADD
        and (
            op.output.space.name,
            op.output.offset,
            op.output.size,
        )
        == (return_varnode.space.name, return_varnode.offset, return_varnode.size)
        and op.inputs[1].space.name == "const"
        and op.inputs[1].offset == 1
        for op in ops
    )


def test_rti_pops_status_and_pc_as_three_wrapping_bytes():
    ops = _ops(b"\x40")
    loads = [op for op in ops if op.opcode == OpCode.LOAD]
    returned = next(op for op in ops if op.opcode == OpCode.RETURN)

    assert len(loads) == 3
    assert all(op.output.size == 1 for op in loads)
    assert sum(op.opcode == OpCode.INT_ADD and op.inputs[0].getRegisterName() == "SP" for op in ops) == 3
    assert returned.inputs[0].size == 2


def test_zero_page_indirect_pointer_fetch_wraps_as_two_byte_reads():
    loads = _matching(b"\xb1\xff", OpCode.LOAD)

    assert len(loads) == 3
    assert all(op.output.size == 1 for op in loads)
    assert any(
        op.opcode == OpCode.INT_ADD
        and op.output.size == 1
        and op.inputs[1].space.name == "const"
        and op.inputs[1].offset == 1
        for op in _ops(b"\xb1\xff")
    )

    registers, _memory, _target = _evaluate_dataflow(
        _ops(b"\xb1\xff"),
        registers={"Y": 0},
        memory={
            0x00FF: 0x34,
            0x0000: 0x12,
            0x0100: 0x56,
            0x1234: 0xAA,
            0x5634: 0xBB,
        },
    )
    assert registers["A"] == 0xAA


def test_nmos_and_cmos_indirect_jmp_have_distinct_page_boundary_semantics():
    nmos_ops = _ops(b"\x6c\xff\x12")
    cmos_ops = _ops(b"\x6c\xff\x12", "65C02:LE:16:default")

    assert [op.output.size for op in nmos_ops if op.opcode == OpCode.LOAD] == [1, 1]
    assert [op.output.size for op in cmos_ops if op.opcode == OpCode.LOAD] == [2]
    assert any(
        op.opcode == OpCode.INT_AND
        and any(value.space.name == "const" and value.offset == 0xFF00 for value in op.inputs)
        for op in nmos_ops
    )

    _registers, _memory, nmos_target = _evaluate_dataflow(
        nmos_ops,
        memory={0x12FF: 0x34, 0x1200: 0x12, 0x1300: 0x56},
    )
    _registers, _memory, cmos_target = _evaluate_dataflow(
        cmos_ops,
        memory={0x12FF: 0x34, 0x1200: 0x12, 0x1300: 0x56},
    )
    assert nmos_target == 0x1234
    assert cmos_target == 0x5634
