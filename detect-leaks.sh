#!/usr/bin/env bash

container_id=""

function finish {
    echo ""
    echo "cleaning up..."
    docker kill ${container_id} || true
}

function dexec {
    docker exec -w $1 -it ${container_id} /bin/bash -c "$2"
}

function run-1-intro-to-c {
    wdir="/opt/stuff/1-intro-to-c/cmake-build-debug"
    dexec ${wdir} "cmake .. && make"
    dexec ${wdir} "cmake .. && make"
    dexec ${wdir} "valgrind --leak-check=yes ./numbers 10 3"
    dexec ${wdir} "valgrind --leak-check=yes printf '%s\n' '-1' | ./convert"
    dexec ${wdir} "valgrind --leak-check=yes printf '%s\n' '1' | ./convert"
    dexec ${wdir} "valgrind --leak-check=yes printf '%s\n' '100' | ./convert"
}

function run-2-arrays-and-pointers {
    wdir="/opt/stuff/2-arrays-and-pointers/cmake-build-debug"
    dexec ${wdir} "cmake .. && make"
    dexec ${wdir} "valgrind --leak-check=yes printf '%s\n' '6' | ./isort"
    dexec ${wdir} "valgrind --leak-check=yes ./twecho hey dude bingo"
}

function run-3-structs {
    wdir="/opt/stuff/3-structs/cmake-build-debug"
    dexec ${wdir} "cmake .. && make && make install"
    dexec ${wdir} "valgrind --leak-check=yes ./revecho hello dude world"
    dexec ${wdir} "valgrind --leak-check=yes ./linked-list-test"
}

function run-4-input-and-output {
    wdir="/opt/stuff/3-structs/cmake-build-debug"
    dexec ${wdir} "cmake .. && make && make install"

    wdir="/opt/stuff/4-input-and-output/cmake-build-debug"
    dexec ${wdir} "cmake .. && make && make install"

    wdir="/opt/stuff/4-input-and-output"
    dexec ${wdir} "printf '%b' 'kara456789abcde\0y123456789erinefghijklm\0' > /tmp/sample.db"
    dexec ${wdir} "printf '%b' 'erin\nhello!\n' | valgrind --leak-check=yes db-add /tmp/sample.db"
    dexec ${wdir} "printf '%b' 'erin\n' | valgrind --leak-check=yes db-lookup /tmp/sample.db"
}

function run-5-socket-programming {
    >&2 echo "not implemented"
    exit 1
}

function run-6-forking-ipc-signals {
    >&2 echo "not implemented"
    exit 1
}

function run-7-posix-threads {
    >&2 echo "not implemented"
    exit 1
}

function run-8-io-multiplexing {
    >&2 echo "not implemented"
    exit 1
}

trap finish EXIT

################################################################################
## build Docker image
#####################

docker build . -t intro-to-c:latest

################################################################################
## run Docker container
#######################

IFS=$'\n'
set -o noglob # disable the second effect of leaving that
              # $(...) unquoted.

dirs=$(find . -type d | sed -e "s;\.\/;;" | grep -v -E ".*\/.*" | grep -E "^[0-9]")

vflags=""
for d in $dirs
do
    vflags="${vflags} -v $(TMP=$(mktemp -d) && mv ${TMP} /tmp/ && echo /tmp${TMP}):/opt/stuff/${d}/cmake-build-debug "
done

runcmd="docker run -it -d -v `pwd`:/opt/stuff ${vflags} -w /opt/stuff intro-to-c:latest"

container_id=$(eval ${runcmd})

################################################################################
## execute build commands inside container
##########################################

cmd=$(echo $1 | sed -e "s;\/;;")

case "${cmd}" in
        1-intro-to-c)
            run-1-intro-to-c
            ;;
        2-arrays-and-pointers)
            run-2-arrays-and-pointers
            ;;
        3-structs)
            run-3-structs
            ;;
        4-input-and-output)
            run-4-input-and-output
            ;;
        5-socket-programming)
            run-5-socket-programming
            ;;
        6-forking-ipc-signals)
            run-6-forking-ipc-signals
            ;;
        7-posix-threads)
            run-7-posix-threads
            ;;
        8-io-multiplexing)
            run-8-io-multiplexing
            ;;
        all)
            run-1-intro-to-c
            run-2-arrays-and-pointers
            run-3-structs
            run-4-input-and-output
            run-5-socket-programming
            run-6-forking-ipc-signals
            run-7-posix-threads
            run-8-io-multiplexing
            ;;
        *)
            echo $"Usage: $0 {all|1-intro-to-c|2-arrays-and-pointers|3-structs|4-input-and-output|5-socket-programming|6-forking-ipc-signals|7-posix-threads}"
            exit 1
esac
