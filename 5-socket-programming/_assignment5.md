# Lab 6

## Part 1

In this exercise, write a program called "loud-echo" which accepts a
TCP connection from a client, prompts the client to enter a string,
and then echoes a capitalized version of that string back to the
client, after which the server should close the TCP connection. The 
program should accept a TCP port to listen on as a command-line 
argument.

The following example shows program input and output. Note that we
run the server in the background using the `&` symbol.

```shell
$ ./cmake-build-debug/loud-echo 3333 &
[1] 5028

$ nc 127.0.0.1 3333
Enter a string: hello
You entered: HELLO
```

## Part 2

The program which you wrote in Part 1 limits concurrency to 1; while
the server waits for client input, no other clients can interact
with the server.

Write a new program called "concurrent-loud-echo" which uses the
`fork` function to create a child process for each client up to a
maximum of 10 active child processes. The server should keep track
of the processes that it has forked and should make sure that they
are not orphaned when the server exits.

## Part 3

In this part of the exercise, you're going to be writing a web
application called "db-server" which makes your db-lookup and 
db-add functionality accessible over HTTP. You're going to want to 
familiarize yourself with the [HTTP protocol][1]. [This Stack 
Overflow][2] post might be helpful, too. This is a big assignment,
so give yourself plenty of time to complete it.

### Acceptance Criteria

1. Your program must respond to an HTTP GET request to 
   `/records/$X`. When processing the request, the program must
   look into its database to see if a record exists with offset
   `$X`. If it does, it must respond with a status of 200 and a body
   which includes the name and message of the record. If no record 
   exists with offset X, your program must respond with status 404.
2. Your program must respond to an HTTP GET request to 
   `/records?q=$Y`. with an HTTP response with status 200 and a body
   which includes the name and message from all records whose name
   and or message contain `$Y`. Your program must use only the first
   5 characters from `$Y`.
3. Your program must respond to an HTTP POST request to `/records`. 
   Your program can assume that the client has sent a request with 
   `Content-Type` of `text/csv`. It must read a name and message 
   from the request body, and must use that name and message to 
   insert a new record into the database. After doing so, it must 
   respond to the request with a response with an empty
   body and a 201 status.

The test suite provides a more-exhaustive set of acceptance criteria
for your server.

Note: Ensure that you rebuild and reinstall the db library if you
make changes to it as part of working on this assignment. You can do
this from the 4-input-and-output directory by running the build.sh
script, which will build and install libdb and db.h.

[1]: https://www.jmarshall.com/easy/http/
[2]: https://stackoverflow.com/a/176477
