# Assignment 1

## Part 1

Write a program called "numbers" that accepts two positive integer
arguments from the user and prints:

1. The average of the two numbers, printed as a floating-point
   number.
2. A value indicating whether each number was prime or not.
3. A value indicating whether the two numbers were relatively
   prime or not (use whatever algorithm that you can find online).

You can assume that the user will input only positive integers, i.e.
you don't have to validate their input.

Here is an example run of the program:

```shell
$ ./cmake-build-debug/numbers 1 2
You typed in 1 and 2.
The average is 1.500000.
The first number, 1, is prime.
The second number, 2, is prime.
1 and 2 are relatively prime.
```

### Directory Layout

Several files have been included; you just need to complete the
functions that are marked as "not yet implemented":

- average.h and average.c contain the `avg` function
- gcd.h and gcd.c contain the `gcd` function
- prime.h and prime.c contain the `is_prime` function
- numbers.c contains the `main` function which will call these other
  functions.

### Build and Test

To build the assignment, simply run the `./build.sh` script. To run
the tests, run the `./test.sh` script. To run the program, first run
the build script, then run `./cmake-build-debug/numbers`.

### Hints!

You can use 
```c
int x, y;
x = 42;
y = 143;

printf("You typed in %d and %d\n", x, y);
```

...to print integers, and

```c
float f;
f = 143.42;

printf("The average is: %f\n", f);
```

...to print a floating point number.

## Part 2

Write a program called "convert" which reads a signed integer from
standard input, saves that input to a variable of type `int`, and 
then interprets that variable's bytes in four different ways:

1. As a signed decimal
2. As an unsigned decimal
3. Encoded as a hexadecimal (base-16) string
4. Encoded as a binary (base-2) string

Some example runs of the program:

```shell
$ printf '%s' '1' | ./cmake-build-debug/convert
signed dec:    1
unsigned dec:  1
hex:           1
binary:        0000 0000 0000 0000 0000 0000 0000 0001
```

```shell
$ printf '%s' '-1' | ./cmake-build-debug/convert
signed dec:    -1
unsigned dec:  4294967295
hex:           ffffffff
binary:        1111 1111 1111 1111 1111 1111 1111 1111
```

### Hints!

The `scanf` function can be useful for reading characters from stdin
and interpreting those characters as a number:

```c
float f;
scanf("%f", &f); // blocks until user enters a number and hits enter
printf("%f\n", f); // prints the user input

int x;
scanf("%d", &x); // %d is different than %f (run `man 3 scanf` in terminal)
printf("%d\n", x);
```
