# Week 3

## Key Concepts

- structs
- void pointers for "generic" data structures

## Reading

1. (required) K&R Chapters 1-6
2. (optional) https://stackoverflow.com/a/57362527
3. (optional) http://c-faq.com/struct/align.esr.html
4. (optional) http://www.catb.org/esr/structure-packing/

## Lecture: Polymorphism in C

Like in Ruby or JavaScript, C provides a mechanism for writing 
functions that are polymorphic over their input and output types. 
Unlike most modern compiled languages, polymorphism in C comes at 
the cost of safety.

Recall that in C, we use types to tell the program how it should 
interpret the bytes that we give it. The types themselves don't 
change the in-memory bytes; we can tell the program to interpret a 
single `char` as an `int`, an `int` as a 32-bit buffer, and so 
forth.

C, being really old and lame, supports parametric polymorphism about 
as well as Golang does (ha ha) - which is to say: it doesn't. 
Instead, polymorphic functions and types in C take a "we trust you" 
approach which feels quite similar to the dynamically-typed approach 
taken in Ruby, Python, and JavaScript.

For example, we might define a linked list (a sort of list where 
each element is a piece of data and a link to the next piece of 
data in the list) like so:

```c
struct Element {
    void *data;
    struct Element *next;
};
```

Note the use of the `void *data` struct field. This is what's 
referred to as a "void pointer" in C, which means "a pointer to a 
value of any type." Since the pointer _itself_ is always the same 
size, regardless of the type of the thing being pointed to, almost 
anything can be a stand in for `void *`.

```c
int main (int argc, char **argv) {
    int i, j = 0;
    struct Element tail = { &j, NULL };
    struct Element head = { &i, &tail };
}
```

An `int *` counts as a `void *`, so the program compiles. Really 
great if your program has no bugs in it, but not so great if you, 
say, accidentally mix heterogeneous types in your list:

```c
int main (int argc, char **argv) {
    int j = 0;
    char c = 'x';

    struct Element tail = { &j, NULL };
    struct Element head = { &c, &tail }; // this does compile
}
```

C supports higher-order functions, and those functions can be 
polymorphic too:

```c
// polymorphic
void for_each(struct Element *list, void (*fn)(void *)) {
    struct Element *ptr = list;
    while (1) {
        fn(ptr->data);

        if (ptr->next == NULL) {
            return;
        }

        ptr++;
    }
}

// monomorphic
void print_int(int *x) {
    printf("x=%d\n", *x);
}

int main (int argc, char **argv) {
    int i = 10;
    int j = 20;

    struct Element tail = { &j, NULL};
    struct Element head = { &i, &tail };

    // need to cast the monomorphic function to a void type
    for_each(&head, (void (*)(void *)) &print_int);
}
```
