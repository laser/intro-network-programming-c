# Assignment 2

## Part 1

Write a program that dynamically allocates an array of random 
integers using the `malloc` and `random` functions. The number of 
integers should be read from the user using `scanf`. You can assume 
that the user will input a positive integer, i.e. you don't need to 
validate their input.

After creating and filling the array, your program should make a
copy of the array and then sort that new array in ascending order.
It should then make a second copy and sort that copy in descending
order. You may implement the sort yourself, or you may use the
`qsort` function.

Finally, your program should print out all three arrays before using
the `free` function to deallocate the memory you've previously
allocated using `malloc`.

An example run of the program might look like this:

```shell
$ printf '3' | ./cmake-build-debug/isort
original: 1804289383, 846930886, 1681692777
ascending: 846930886, 1681692777, 1804289383
descending: 1804289383, 1681692777, 846930886
```

## Part 2

Write a program called "twecho" that takes a variable number of
arguments and prints each argument twice: once as-provided and once
in capital letters. 

For example:

```shell
./cmake-build-debug/twecho hello world dude
hello HELLO
world WORLD
dude DUDE
```

You might get some use out of the `strlen` and `upper` functions.
Make sure to run the leak detector on your code before committing
it.
