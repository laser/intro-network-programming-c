cmake_minimum_required(VERSION 3.12)
project(4_input_and_output C)

set(CMAKE_C_STANDARD 99)

link_directories(/usr/local/lib)
include_directories(/usr/local/include)

# https://cmake.org/cmake/help/latest/command/add_library.html
add_library(db STATIC db.c)

# https://cmake.org/cmake/help/latest/prop_tgt/PUBLIC_HEADER.html
set_target_properties(db PROPERTIES PUBLIC_HEADER "db.h")

# install the db library so that subsequent weeks can use it
install(TARGETS db
        ARCHIVE DESTINATION lib
        PUBLIC_HEADER DESTINATION include)

# https://cmake.org/cmake/help/latest/command/add_executable.html
add_executable(db-lookup db-lookup.c db.h db.c)
add_executable(db-add db-add.c db.h db.c)

# https://cmake.org/cmake/help/latest/command/target_link_libraries.html?highlight=target_link_libraries
target_link_libraries(db-lookup LINK_PUBLIC linked-list)
target_link_libraries(db-add LINK_PUBLIC linked-list)

# add a custom target for our Sharness test-script
add_custom_target(lab4-tests COMMAND ./lab4_tests.py --verbose WORKING_DIRECTORY ..)

# ensure that the binaries are built before we run the tests against them
add_dependencies(lab4-tests db db-lookup db-add)
