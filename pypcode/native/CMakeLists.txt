cmake_minimum_required(VERSION 3.9)
project(csleigh)
# set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O0 -ggdb")

SEPARATE_ARGUMENTS(NEW_CMAKE_C_FLAGS NATIVE_COMMAND ${CMAKE_C_FLAGS})

# First for the generic no-config case (e.g. with mingw)
set( CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin )
set( CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib )
set( CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib )
# Second, for multi-config builds (e.g. msvc)
foreach( OUTPUTCONFIG ${CMAKE_CONFIGURATION_TYPES} )
    string( TOUPPER ${OUTPUTCONFIG} OUTPUTCONFIG )
    set( CMAKE_RUNTIME_OUTPUT_DIRECTORY_${OUTPUTCONFIG} ${CMAKE_BINARY_DIR}/bin )
    set( CMAKE_LIBRARY_OUTPUT_DIRECTORY_${OUTPUTCONFIG} ${CMAKE_BINARY_DIR}/lib )
    set( CMAKE_ARCHIVE_OUTPUT_DIRECTORY_${OUTPUTCONFIG} ${CMAKE_BINARY_DIR}/lib )
endforeach( OUTPUTCONFIG CMAKE_CONFIGURATION_TYPES )

if (MSVC)
    add_compile_options(/O3 /std:c++14)
else()
    add_compile_options(-O3 -Wall -Wno-sign-compare -D__TERMINAL__ -std=c++14)
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

add_library(csleigh
	csleigh.cc
	${SLEIGH_COMMON}
)

set_target_properties(csleigh PROPERTIES POSITION_INDEPENDENT_CODE ON)

if (MSVC)
	if (CMAKE_SIZEOF_VOID_P EQUAL 8)
		set(PREPROCESSOR_ONLY_FLAGS /DCFFI_CDEF=1 /EP /D_WINDOWS=1 /D_WIN64)
	else ()
		set(PREPROCESSOR_ONLY_FLAGS /DCFFI_CDEF=1 /EP /D_WINDOWS=1 /D_WIN32)
	endif ()
else()
    set(PREPROCESSOR_ONLY_FLAGS -DCFFI_CDEF=1 -E -P)
endif()

add_custom_target(
	csleigh.i ALL
	COMMAND ${CMAKE_C_COMPILER} ${NEW_CMAKE_C_FLAGS} ${PREPROCESSOR_ONLY_FLAGS} ${CMAKE_SOURCE_DIR}/csleigh.h > ${CMAKE_BINARY_DIR}/csleigh.i
	BYPRODUCTS ${CMAKE_BINARY_DIR}/csleigh.i
	VERBATIM
)
