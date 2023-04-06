cmake_minimum_required(VERSION 3.18...3.22)
project(pypcode_native)
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_OSX_DEPLOYMENT_TARGET 10.14)

if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

# Detect the installed nanobind package and import it into CMake
execute_process(
  COMMAND "${Python_EXECUTABLE}" -c "import nanobind; print(nanobind.cmake_dir())"
  OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE NB_DIR)
list(APPEND CMAKE_PREFIX_PATH "${NB_DIR}")
find_package(nanobind CONFIG REQUIRED)

if (MSVC)
    add_compile_options(/O2 /D_HAS_STD_BYTE=0)
else()
    add_compile_options(-O3 -Wall -Wno-sign-compare -D__TERMINAL__)
endif()

set(SLEIGH_COMMON
	sleigh/address.cc
	sleigh/context.cc
	sleigh/float.cc
	sleigh/globalcontext.cc
	sleigh/marshal.cc
	sleigh/opcodes.cc
	sleigh/pcodecompile.cc
	sleigh/pcodeparse.cc
	sleigh/pcoderaw.cc
	sleigh/semantics.cc
	sleigh/sleigh.cc
	sleigh/sleighbase.cc
	sleigh/slghpatexpress.cc
	sleigh/slghpattern.cc
	sleigh/slghsymbol.cc
	sleigh/space.cc
	sleigh/translate.cc
	sleigh/xml.cc
	)

add_executable(sleigh
	sleigh/filemanage.cc
	sleigh/slgh_compile.cc
	sleigh/slghparse.cc
	sleigh/slghscan.cc
	${SLEIGH_COMMON}
	)
install(TARGETS sleigh DESTINATION bin)

nanobind_add_module(pypcode_native
	pypcode_native.cpp
	${SLEIGH_COMMON}
	)
install(TARGETS pypcode_native DESTINATION .)
