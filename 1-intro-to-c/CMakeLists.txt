cmake_minimum_required(VERSION 3.12)
project(1_intro_to_c C)

set(CMAKE_C_STANDARD 99)

# ensure our compiler knows where to look for external libs and headers
link_directories(/usr/local/lib)
include_directories(/usr/local/include)

# https://cmake.org/cmake/help/latest/command/add_executable.html
add_executable(numbers numbers.c average.c average.h prime.c prime.h gcd.c gcd.h)
add_executable(convert convert.c)

# https://cmake.org/cmake/help/latest/command/target_compile_options.html
target_compile_options(numbers PRIVATE -Werror)
target_compile_options(convert PRIVATE -Werror)

# add a custom target for our Sharness test-script
add_custom_target(lab1-tests COMMAND ./lab1_tests.py --verbose WORKING_DIRECTORY ..)

# ensure that the binaries are built before we run the tests against them
add_dependencies(lab1-tests numbers convert)
