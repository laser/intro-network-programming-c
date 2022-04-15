# Assignment 6

## Part 1

The TCP echo server that you wrote in the previous session limits 
concurrency to 1; while the server waits for client input, no other 
clients can interact with the server.

Write a new version of your original program called 
`concurrent-loud-echo` which uses the `fork` function to create a 
child process for each client up to a maximum of 10 active child 
processes. The server should keep track of the processes that it has 
forked and should make sure that they are not orphaned when the 
server exits.

## Part 2

The db-server program that you wrote in the previous exercise
processes HTTP requests sequentially, which limits its usefulness.
In this exercise, write a new version of db-server called
`forking-db-server` which distributes its workload across a number 
of processes that you fork. Experiment with [Fortio][1] to compare
total requests/second throughput of your new server with that of
your original server.

### Acceptance Criteria

1. Your program must distribute the work across a number of child
   processes that it forks. There must be some bound on the number
   of child processes that it forks - it is up to you to decide how
   to set that limit.
2. Your program must handle SIGTERM by shutting down all the
   processes that it has forked.
3. Your program must not interleave concurrent writes from different 
   processes to the database file. The [flock(2)][2] tool will be
   useful here.

[1]: https://github.com/fortio/fortio
[2]: https://linux.die.net/man/2/flock
