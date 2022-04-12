# Lecture 2: Pointers

## Key Concepts

- stack
- heap
- pointers
- arrays

## Reading

1. (required) K&R Chapters 1-6
2. (required) https://stackoverflow.com/questions/1518711/how-does-free-know-how-much-to-free
3. (optional) https://www2.seas.gwu.edu/~simhaweb/C/modules/module3/module3.html
4. (optional) https://www.programmerinterview.com/data-structures/difference-between-stack-and-heap/
5. (optional) https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/VMPages.html

## Lecture: The Memory Layout of a C program

Our C program is concerned primarily with two regions of memory: the 
stack and the heap.

### The Stack

The stack is a small, contiguous block of memory that your program 
can read from and write to. Your operating system allocates one 
stack per thread, and your process may own many threads. When your 
process starts, it will start with a single OS thread and thus a 
single stack. As your process creates new threads, more stacks will 
be allocated to those threads by the OS.

#### Acquiring Stack Memory

Your C program does not need to explicitly ask for memory in this 
address space (e.g. with malloc or calloc); allocation from the 
thread's stack-reserved memory will happen automatically when you 
create a variable, and those variables (and the memory in which 
they're stored) will live until the function in which they're 
defined returns, at which point they'll be freed.

```c
// sample-program.c
#include <stdio.h>
#include <stdlib.h>

void foo(int y) {
    printf("addr(y%d): dec=%lu, hex=%p\n", y, (unsigned long)&y, &y);
    if (y > 3) {
        return;
    }


    foo(y + 1);
}

int main(int argc, char **argv) {
    int x = 0;
    printf("addr(x): dec=%lu, hex=%p\n", (unsigned long)&x, &x);
    foo(x);
}
```

```shell
$ ./sample-program
addr(x): dec=140701865343468, hex=0x7ff7b4b3f9ec
addr(y0): dec=140701865343436, hex=0x7ff7b4b3f9cc
addr(y1): dec=140701865343404, hex=0x7ff7b4b3f9ac
addr(y2): dec=140701865343372, hex=0x7ff7b4b3f98c
addr(y3): dec=140701865343340, hex=0x7ff7b4b3f96c
````

Note that the stack addresses grow downwards. Given a runaway 
recursive function, the stack will grow and grow until eventually it 
tries to allocate from a portion of the process's memory that 
doesn't belong to the thread's stack, at which point the OS kernel 
terminates the program with a segmentation fault error.

You can use the vmmap program to get a view of the virtual memory 
used by your program. Using vmmap, we can get the address range of 
our program's one and only stack, and we can confirm what we see in 
vmmap by causing our program to repeatedly allocate from the stack 
until we overflow that range.

### Relinquishing Stack Memory

C does not have closures, so stack-allocated memory will be 
relinquished when the variable goes out of scope, i.e. its enclosing 
function returns. After the memory is freed, the address can be 
reused later, by some other function call:

```c
#include <stdio.h>
#include <stdlib.h>

// other-program.c
void foo(int y) {
    printf("addr(y%d): dec=%lu, hex=%p\n", y, (unsigned long)&y, &y);
    if (y == 3) {
        return;
    }
    foo(y + 1);
}

void bar(int z) {
    printf("addr(z): decimal=%lu, hex=%p\n", (unsigned long)&z, &z);
}

int main (int argc, char **argv) {
    int x = 0;
    printf("addr(x): dec=%lu, hex=%p\n", (unsigned long)&x, &x);
    foo(x);
    bar(x);
}
```

```shell
$ ./other-program
addr(x): dec=140701830597100, hex=0x7ff7b2a1c9ec
addr(y0): dec=140701830597068, hex=0x7ff7b2a1c9cc
addr(y1): dec=140701830597036, hex=0x7ff7b2a1c9ac
addr(y2): dec=140701830597004, hex=0x7ff7b2a1c98c
addr(y3): dec=140701830596972, hex=0x7ff7b2a1c96c
addr(z): decimal=140701830597068, hex=0x7ff7b2a1c9cc
```

## The Heap

The heap is a much larger chunk of writable memory allocated to your 
process by the kernel. Allocations of memory from the heap must be 
managed by the programmer and are permitted to outlive a function 
call.

The programmer leases memory from the heap explicitly using the 
malloc or calloc functions (which allocate uninitialized memory and 
initialized memory, respectively) and relinquishes that memory using 
the free function.

In the following program, the print_heap function returns a pointer 
(which is a stack-allocated value) to some memory (on the heap) to 
the main function. Also note that the programmer needs to remember 
to call the free function, as the C compiler has no way of knowing 
when you'll be done with the memory you've allocated (although the 
Rust compiler does).

```c
// flarp.c
char* print_heap() {
    char *ptr = malloc(32);
    printf("addr(ptr): dec=%lu, hex=%p\n", (unsigned long)ptr, ptr);
    
    return ptr;
}

int main (int argc, char **argv) {
    char* ptrs[4];
    for (int i = 0; i < 3; i++) {
        ptrs[i] = print_heap();
    }

    for (int j = 0; j < 3; j++) {
        free(ptrs[j]);
    }
}
```

```shell
$ ./flarp
addr(ptr): decimal=105553133359392, hex=0x60000104d120
addr(ptr): decimal=105553133359424, hex=0x60000104d140
addr(ptr): decimal=105553133359456, hex=0x60000104d160
```

Note that, unlike the stack, the addresses we get from the heap go 
up in value with each allocation.
