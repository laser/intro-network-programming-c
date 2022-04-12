# Assignment 3

## Part 1

Your job is to implement a singly linked list that can hold values
of any type. The interface has been specified and provided to you
in a header file called linked-list.h. So your job is to write linked-list.c
that implements each function whose prototype is included in 
linked-list.h. Specifically, you'll need to write the following 
functions:

- `add_front`
- `traverse_list`
- `flip_sign_double`
- `compare_double`
- `find_node`
- `remove_head`
- `remove_all_nodes`
- `add_after`
- `reverse_list`

The linked-list.c file contains detailed comments specifying the behavior 
of each function. Your implementation should follow the specified
behavior.

In addition, I provide you with a test program, linked-list-test.c, which 
tests each function listed above, and produces the following output 
for a correctly implemented linked list:

```shell
./build.sh && ./cmake-build-debug/linked-list-test
testing add_front(): 9.0 8.0 7.0 6.0 5.0 4.0 3.0 2.0 1.0
testing flip_sign_double(): -9.0 -8.0 -7.0 -6.0 -5.0 -4.0 -3.0 -2.0 -1.0
testing flip_sign_double() again: 9.0 8.0 7.0 6.0 5.0 4.0 3.0 2.0 1.0
testing find_node(): OK
popped 9.0, the rest is: [ 8.0 7.0 6.0 5.0 4.0 3.0 2.0 1.0 ]
popped 8.0, the rest is: [ 7.0 6.0 5.0 4.0 3.0 2.0 1.0 ]
popped 7.0, the rest is: [ 6.0 5.0 4.0 3.0 2.0 1.0 ]
popped 6.0, the rest is: [ 5.0 4.0 3.0 2.0 1.0 ]
popped 5.0, the rest is: [ 4.0 3.0 2.0 1.0 ]
popped 4.0, the rest is: [ 3.0 2.0 1.0 ]
popped 3.0, the rest is: [ 2.0 1.0 ]
popped 2.0, the rest is: [ 1.0 ]
popped 1.0, the rest is: [ ]
testing add_after(): 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0
popped 1.0, and reversed the rest: [ 9.0 8.0 7.0 6.0 5.0 4.0 3.0 2.0 ]
popped 9.0, and reversed the rest: [ 2.0 3.0 4.0 5.0 6.0 7.0 8.0 ]
popped 2.0, and reversed the rest: [ 8.0 7.0 6.0 5.0 4.0 3.0 ]
popped 8.0, and reversed the rest: [ 3.0 4.0 5.0 6.0 7.0 ]
popped 3.0, and reversed the rest: [ 7.0 6.0 5.0 4.0 ]
popped 7.0, and reversed the rest: [ 4.0 5.0 6.0 ]
popped 4.0, and reversed the rest: [ 6.0 5.0 ]
popped 6.0, and reversed the rest: [ 5.0 ]
popped 5.0, and reversed the rest: [ ]
```

I recommend you implement the functions in the order listed, and 
test each function as you go. You can start by commenting out the 
code in `main()` of linked-list-test.c and uncomment the code one block 
at a time to test each list function you implemented.

Don’t forget to run valgrind at each step to make sure you don't 
leak memory.

## Part 2

In this part, you will use the linked list library that you
implemented in Part 1 to write a program called "revecho" that 
prints out the command line arguments in reverse order. In addition,
it will look for the word "dude" among the command line arguments 
you passed, and report whether it’s there or not.

For example:

```shell
./build.sh && ./revecho hello world dude
dude
world
hello
dude found
```

Another example:

```shell
./build.sh && ./revecho hello world friend
friend
world
hello
dude not found
```

Here are the program requirements and hints:
- Your program should simply put all the argument strings into a list
  WITHOUT duplicating them. There should be no malloc in your code.
  Just call `add_front()` for all strings.
- To print out the strings, you can either use `traverse_list()` or you
  can traverse the list by yourself by following the next pointers,
  printing out each string.
- Don’t forget to initialize the list and remove all nodes at the end
  to prevent memory errors or leaks.
- To find "dude", you can either traverse the list yourself, or use
  `find_node()`. Either way, `strcmp()` function will come in handy. If
  you want to pass strcmp to `find_node()`, you will have to cast it to
  the correct function pointer type because the signature of `strcmp()`
  is slightly different from the signature of `compar` argument of
  `find_node()`.  K&R2 section 5.11 has an example of casting a function
  pointer.
- You must use liblinked-list.a that you built in part1 from the part1
  directory. Do not copy any files from part1 directory to part2
  directory.

Note that all you need to use the linked list is the header file and
the library file (that are residing somewhere else). This is in
fact what it means to use a 3rd party library in your code.
