cmake_minimum_required(VERSION 3.12)
project(3_structs C)

set(CMAKE_C_STANDARD 99)

link_directories(/usr/local/lib)
include_directories(/usr/local/include)

# https://cmake.org/cmake/help/latest/command/add_library.html
add_library(linked-list STATIC linked-list.c)

# https://cmake.org/cmake/help/latest/prop_tgt/PUBLIC_HEADER.html
set_target_properties(linked-list PROPERTIES PUBLIC_HEADER "linked-list.h")

# https://cmake.org/cmake/help/latest/command/install.html
install(TARGETS linked-list
        ARCHIVE DESTINATION lib
        PUBLIC_HEADER DESTINATION include)

# https://cmake.org/cmake/help/latest/command/add_executable.html
add_executable(linked-list-test linked-list-test.c linked-list.h linked-list.c)
add_executable(revecho revecho.c linked-list.h linked-list.c)

# https://cmake.org/cmake/help/latest/command/target_link_libraries.html
target_link_libraries(linked-list-test LINK_PUBLIC linked-list)
target_link_libraries(revecho LINK_PUBLIC linked-list)

# add a custom target for our Sharness test-script
add_custom_target(lab3-tests COMMAND ./lab3_tests.py --verbose WORKING_DIRECTORY ..)

# ensure that the binaries are built before we run the tests against them
add_dependencies(lab3-tests revecho linked-list-test)
