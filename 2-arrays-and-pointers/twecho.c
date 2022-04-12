#include <stdio.h>

static char **duplicate_and_capitalize_args(int argc, char **argv) {
    // implement me
    return NULL;
}

static void free_duplicated_args(char **copy) {
    // implement me
}

int main(int argc, char **argv) {
    if (argc <= 1)
        return 1;
    char **copy = duplicate_and_capitalize_args(argc, argv);
    char **p = copy;
    argv++;
    p++;
    while (*argv) {
        printf("%s %s\n", *argv++, *p++);
    }
    free_duplicated_args(copy);
    return 0;
}
