cmake_minimum_required(VERSION 3.12)
project(2_arrays_and_pointers C)

set(CMAKE_C_STANDARD 99)

link_directories(/usr/local/lib)
include_directories(/usr/local/include)

# https://cmake.org/cmake/help/latest/command/add_executable.html
add_executable(isort isort.c)
add_executable(twecho twecho.c)

# https://cmake.org/cmake/help/latest/command/target_compile_options.html
target_compile_options(isort PRIVATE -Werror)
target_compile_options(twecho PRIVATE -Werror)

# add a custom target for our Sharness test-script
add_custom_target(lab2-tests COMMAND ./lab2_tests.py --verbose WORKING_DIRECTORY ..)

# ensure that the binaries are built before we run the tests against them
add_dependencies(lab2-tests isort twecho)
