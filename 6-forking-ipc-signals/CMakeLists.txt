cmake_minimum_required(VERSION 3.12)
project(5_basic_network_programming C)

set(CMAKE_C_STANDARD 99)

link_directories(/usr/local/lib)
include_directories(/usr/local/include)

add_executable(db-server-forking forking-db-server.c)

# add a custom target for our Sharness test-script
add_custom_target(lab6-tests COMMAND ./lab6_tests.py --verbose WORKING_DIRECTORY ..)


# ensure that the binaries are built before we run the tests against them
add_dependencies(lab6-tests db-server-forking)
