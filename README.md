# introduction-to-c

> learn how good you have it nowadays

## Acknowledgements

This repo borrows heavily from Jae Woo Lee's (Columbia University) 
_COMS W3157 Advanced Programming_ and Mirela Damian's (Villanova) 
_POSIX Threads_.

## Reading

A copy of [_The C Programming Language, 2nd Edition_][1] is required
for this course, as is a copy of [_Unix Network Programming: The
Sockets Networking Api, Volume 1, 3rd Edition_][2]. 

Lecture notes can be found in each session's directory. The lectures 
are a bit spartan, so you'll likely need to do some digging on your 
own to fill in the gaps of what's been communicated.

## Sessions

- 1: Bytes and Encodings
- 2: Pointers and Arrays
- 3: Structs
- 4: File I/O
- 5: Socket Basics
- 6: Forking Processes and IPC
- 7: POSIX Threads
- 8: I/O Multiplexing with Poll

## Process

If you'd like to take the course, simply create your own branch off 
of `main`. As we add more tests to the project, you may wish to 
rebase your branch onto `main`. You may also want to hook us up with 
your sweet tests and bugfixes. If that's the case, simply issue a PR 
back to `main` from your branch.

## Tools

This project uses CMake to build things, install things, and to run 
the Sharness tests. You can download CMake from wherever you like.

To detect memory leaks, we need Valgrind. To run Valgrind, we need 
Linux. To run Linux from OSX, we need Docker. Thus, you'll want 
Docker on your Mac. You can download Docker from wherever you like.

I use [CLion](https://www.jetbrains.com/clion/), the JetBrains 
product of IntelliJ fame, to write C. It knows about CMake, does 
code completion, etc. You don't have to use it, but I recommend that you do.

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
