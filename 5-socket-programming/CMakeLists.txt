cmake_minimum_required(VERSION 3.12)
project(6_socket_programming C)

set(CMAKE_C_STANDARD 99)

link_directories(/usr/local/lib)
include_directories(/usr/local/include)

add_executable(concurrent-loud-echo concurrent-loud-echo.c)
add_executable(db-server db-server.c)
add_executable(loud-echo loud-echo.c)

target_link_libraries(db-server LINK_PUBLIC db linked-list)

# add a custom target for our Sharness test-script
add_custom_target(lab5-tests COMMAND ./lab5_tests.py --verbose WORKING_DIRECTORY ..)

# ensure that the binaries are built before we run the tests against them
add_dependencies(lab5-tests concurrent-loud-echo db-server loud-echo)

