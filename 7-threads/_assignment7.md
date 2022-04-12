# Lab 7

## Part 1

The threaded-db-server program that you wrote in the previous
exercise distributes HTTP request handling across a variety of
child processes. In this exercise, write a new version of the server
called "threaded-db-server" which distributes its workload across
a number of threads that you spawn. Experiment with [Fortio][1] to 
compare total requests/second throughput of your new server with 
that of your original server. 

### Acceptance Criteria

1. Your program must distribute the work across a number of child
   threads that it spawns. There must be some bound on the number
   of child processes that it forks - it is up to you to decide how
   to set that limit.
2. Your program must handle SIGTERM by shutting down all of the
   threads that it has forked.
3. Your program must not interleave concurrent writes from different
   processes to the database file. You may wish to use a mutex.

[1]: https://github.com/fortio/fortio
