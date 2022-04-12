cmake_minimum_required(VERSION 3.12)
project(7_http_server_programming C)

set(CMAKE_C_STANDARD 99)

link_directories(/usr/local/lib)
include_directories(/usr/local/include)

add_executable(threaded-db-server threaded-db-server.c)

# add a custom target for our Sharness test-script
add_custom_target(lab7-tests COMMAND ./lab7_tests.py --verbose WORKING_DIRECTORY ..)

# ensure that the binaries are built before we run the tests against them
add_dependencies(lab7-tests threaded-db-server)
