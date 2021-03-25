from cffi import FFI
import os.path
import platform

SOURCE_DIR = os.path.abspath(os.path.dirname(__file__))


libs = {
    'Windows': [],
    'Darwin': ['c++'],
    'Linux': ['stdc++']
}[platform.system()]

ffibuilder = FFI()
ffibuilder.cdef(open(os.path.join(SOURCE_DIR, "csleigh.i")).read())
ffibuilder.set_source("pypcode._csleigh",
    """
    #include "csleigh.i"
    """,
    libraries=['csleigh'] + libs,
    include_dirs=[SOURCE_DIR],
    library_dirs=[os.path.join(SOURCE_DIR, 'lib')])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
