# Lab 4

## Part 1

### Part 1a

The directory contains a simple database into which you can put
records, each consisting of a name and a short message.

#### demo-db.db

This is the database file. It contains each record one after 
another. Each record is 40 bytes; the size of this database file is 
always a multiple of 40.

#### demo-db-add

This is the program that inserts a record into the demo-db.db
database file. It will ask for a name and a short message, and
then fills up the following structure with those values:

```c
struct Record {
    char name[16];
    char msg[24];
};
```

The program will add each new struct to an in-memory linked list
and then write the struct's bytes to the database file. It will
then confirm that the record has been added by outputting the
new record in a manner identical to demo-db-lookup.

Note that the name and the message will be truncated to 15 and 23 
characters, respectively, in order to fit them into the structure.

#### demo-db-lookup

This is the program you use to see what’s in the database and to 
search for a particular name or a message. It will prompt for a 
string to search for. If you simply press ENTER, it will show
you all the records in the database. If you type something, it
will show you those records that contain what you typed either
in the name field or in the msg field.

Only the first 5 letters are used in the search. So searching
for "hello" and "helloooooo" will yield the same result. The
match is case-sensitive.
      
The program keeps running, prompting you for another string to
search for. You can press Ctrl-D to terminate the program.

Play with demo-db-add and demo-db-lookup, inserting a couple of
records into the database:

```
$ touch /tmp/demo-db.db

$ ./demo-db-add /tmp/demo-db.db
name please (will truncate to 15 chars): erin
msg please (will truncate to 23 chars): hello!
   1: {erin} said {hello!}

$ ./demo-db-add /tmp/demo-db.db
name please (will truncate to 15 chars): bob
msg please (will truncate to 23 chars): goodbye!
   2: {bob} said {goodbye!}

$ ./demo-db-add /tmp/demo-db.db
name please (will truncate to 15 chars): sue
msg please (will truncate to 23 chars): good day
   3: {sue} said {good day}
```

```
$ ./demo-db-lookup /tmp/demo-db.db
lookup: erin
   1: {erin} said {hello!}
lookup: good
   2: {bob} said {goodbye}
   3: {sue} said {good day}
```

### Part 1b

Write both your own db-lookup and db-add programs that behave the
same way as mine.

Both db-add and db-lookup should use the `load_db` function to
build a linked list from the bytes in the file. It will return the 
number of records loaded, or a negative number on error.

Some requirements for your program(s):

1. If the database file does not exist when db-add and db-lookup 
   are run, it should be created.
2. Both programs should attempt to build a linked list (import the
   one you created in the previous week) from the contents of the
   database file.
3. You must keep the records in the list in the order in which they
   appear in the database file, i.e. the first record in your file
   should be the head of the list.
4. You may assume that an input line will never exceed a certain 
   large number (1000 for example) of characters.
5. The db-lookup program should truncate the user's input to 5
   characters.
6. The db-lookup program must search both record name and message.

You should be able to ascertain more requirements from the provided
test suite, e.g. formatting and indentation of expected output.

You may find the `strncpy`, `strlen`, `fgets`, `getchar`, `isprint`,
and `strstr` to be useful functions for this exercise.

As usual, don't forget to run the leak detector.
