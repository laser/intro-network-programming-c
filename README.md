# introduction-network-programming-c

> learn the basics of building I/O-heavy systems, in C

## Acknowledgements

This repo borrows heavily from Jae Woo Lee's (Columbia University)
_COMS W3157 Advanced Programming_ and Mirela Damian's (Villanova)
_POSIX Threads_.

## Target Audience

This course is designed for professional web application developers
who write software on an Apple computer. No prior knowledge of C is 
required, but it will help.

## What Are You Going to Learn?

You're going to learn the basics of C programming. You're going to
learn why garbage collection is really useful. You're going to learn
why closures are great, and why parametric polymorphism is good.
You're going to learn why forking web servers use so much memory
compared to threaded web servers. You're going to learn why Node.js
can get so much concurrency out of a single thread. You're going to
learn a lot of other stuff too - trust me, it's going to be great.

## Books You'll Need

A copy of [_The C Programming Language, 2nd Edition_][1] is required
for this course, as is a copy of [_Unix Network Programming: The
Sockets Networking Api, Volume 1, 3rd Edition_][2].

Lecture notes can be found in each session's directory. The notes
are a bit spartan, so you'll likely need to do some digging on your
own to fill in the gaps of what's been communicated.

## Sessions

- 1: Bytes and Encodings ([notes](1-intro-to-c/_notes1.md), [assignment](1-intro-to-c/_assignment1.md))
- 2: Pointers and Arrays ([notes](2-arrays-and-pointers/_notes2.md), [assignment](2-arrays-and-pointers/_assignment2.md))
- 3: Structs ([notes](3-structs/_notes3.md), [assignment](3-structs/_assignment3.md))
- 4: File I/O ([notes](4-input-and-output/_notes4.md), [assignment](4-input-and-output/_notes4.md))
- 5: Socket Basics ([notes](5-socket-programming/_notes5.md), [assignment](5-socket-programming/_assignment5.md))
- 6: Forking Processes and IPC ([notes](6-forking-ipc-signals/_notes6.md), [assignment](6-forking-ipc-signals/_assignment6.md))
- 7: POSIX Threads ([notes](7-threads/_assignment7.md), [assignment](7-threads/_assignment7.md))
- 8: I/O Multiplexing with Poll ([notes](8-io-multiplexing/_notes8.md), [assignment](8-io-multiplexing/_assignment8.md))

## Tools

This project uses CMake to build things, install things, and to run
the tests. You can download CMake from wherever you like.

To detect memory leaks, we need Valgrind. To run Valgrind, we need
Linux. To run Linux from OSX, we need Docker. Thus, you'll want
Docker on your Mac. You can download Docker from wherever you like.

I use [CLion](https://www.jetbrains.com/clion/), the JetBrains
product of IntelliJ fame, to write C. It knows about CMake, does
code completion, etc. You don't have to use it, but I recommend that 
you do.

## Building

Run the `build.sh` script from within a session's directory, e.g.

```shell
cd 1-intro-to-c && ./build.sh
```

## Run Tests

You'll need Python 2.x to run the tests. Run the `run-tests.sh`
script from within a session's directory, e.g.

```shell
cd 1-intro-to-c && ./run-tests.sh
```

Note that this script performs a build and installs any system
libraries and runtime dependencies before running tests.

## Run Leak Detector

A leak checker is provided for you (for the first few exercises,
anyways). It uses Docker, because Valgrind doesn't work on OSX.
To run the leak detector, ensure that a Docker agent is running and
then run the `detect-leaks.sh` script from within a session's
directory, e.g.

```shell
cd 1-intro-to-c && ./detect-leaks.sh
```

This will build your code in a Docker container, run Valgrind
against it, and report back with any leaks.

[1]: https://www.amazon.com/Programming-Language-2nd-Brian-Kernighan/dp/0131103628
[2]: https://www.amazon.com/Unix-Network-Programming-Sockets-Networking/dp/0131411551
