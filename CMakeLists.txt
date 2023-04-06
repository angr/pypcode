cmake_minimum_required(VERSION 3.18...3.22)
project(pypcode)
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_OSX_DEPLOYMENT_TARGET 10.14)

if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

# Detect the installed nanobind package and import it into CMake
execute_process(
  COMMAND "${Python_EXECUTABLE}" -c "import nanobind; print(nanobind.cmake_dir())"
  OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE NB_DIR)
list(APPEND CMAKE_PREFIX_PATH "${NB_DIR}")
find_package(nanobind CONFIG REQUIRED)

if(MSVC)
  add_compile_options(/O2 /D_HAS_STD_BYTE=0)
else()
  add_compile_options(-O3 -Wall -Wno-sign-compare -D__TERMINAL__)
endif()

set(SLEIGH_COMMON
  pypcode/sleigh/address.cc
  pypcode/sleigh/context.cc
  pypcode/sleigh/float.cc
  pypcode/sleigh/globalcontext.cc
  pypcode/sleigh/marshal.cc
  pypcode/sleigh/opcodes.cc
  pypcode/sleigh/pcodecompile.cc
  pypcode/sleigh/pcodeparse.cc
  pypcode/sleigh/pcoderaw.cc
  pypcode/sleigh/semantics.cc
  pypcode/sleigh/sleigh.cc
  pypcode/sleigh/sleighbase.cc
  pypcode/sleigh/slghpatexpress.cc
  pypcode/sleigh/slghpattern.cc
  pypcode/sleigh/slghsymbol.cc
  pypcode/sleigh/space.cc
  pypcode/sleigh/translate.cc
  pypcode/sleigh/xml.cc
  )

add_executable(sleigh
  pypcode/sleigh/filemanage.cc
  pypcode/sleigh/slgh_compile.cc
  pypcode/sleigh/slghparse.cc
  pypcode/sleigh/slghscan.cc
  ${SLEIGH_COMMON}
  )
install(TARGETS sleigh DESTINATION bin)

nanobind_add_module(pypcode_native
  pypcode/pypcode_native.cpp
  ${SLEIGH_COMMON}
  )
install(TARGETS pypcode_native DESTINATION .)
