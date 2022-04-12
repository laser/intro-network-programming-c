#!/usr/bin/env bash

script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

function test-1-intro-to-c {
    cd "${script_dir}/1-intro-to-c"
    ./run-tests.sh
}

function test-2-arrays-and-pointers {
    cd "${script_dir}/2-arrays-and-pointers"
    ./run-tests.sh
}

function test-3-structs {
    cd "${script_dir}/3-structs"
    ./run-tests.sh
}

function test-4-input-and-output {
    cd "${script_dir}/4-input-and-output"
    ./run-tests.sh
}

function test-5-socket-programming {
    cd "${script_dir}/5-socket-programming"
    ./run-tests.sh
}

function test-6-forking-ipc-signals {
    cd "${script_dir}/6-forking-ipc-signals"
    ./run-tests.sh
}

function test-7-posix-threads {
    cd "${script_dir}/7-posix-threads"
    ./run-tests.sh
}

function test-8-io-multiplexing {
    cd "${script_dir}/8-io-multiplexing"
    ./run-tests.sh
}

################################################################################
## execute build commands inside container
##########################################

cmd=$(echo $1 | sed -e "s;\/;;")

case "${cmd}" in
        1-intro-to-c)
            test-1-intro-to-c
            ;;
        2-arrays-and-pointers)
            test-2-arrays-and-pointers
            ;;
        3-structs)
            test-3-structs
            ;;
        4-input-and-output)
            test-4-input-and-output
            ;;
        5-socket-programming)
            test-5-socket-programming
            ;;
        6-forking-ipc-signals)
            test-6-forking-ipc-signals
            ;;
        7-posix-threads)
            test-7-posix-threads
            ;;
        8-io-multiplexing)
            test-8-io-multiplexing
            ;;
        all)
            test-1-intro-to-c
            test-2-arrays-and-pointers
            test-3-structs
            test-4-input-and-output
            test-5-socket-programming
            test-6-forking-ipc-signals
            test-7-posix-threads
            test-8-io-multiplexing
            ;;
        *)
            echo $"Usage: $0 {all|1-intro-to-c|2-arrays-and-pointers|3-structs|4-input-and-output|5-socket-programming|6-forking-ipc-signals|7-posix-threads|8-io-multiplexing}"
            exit 1
esac
