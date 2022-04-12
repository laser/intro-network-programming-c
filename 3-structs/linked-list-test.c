#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "linked-list.h"

static void printDouble(void *p) {
    printf("%.1f ", *(double *) p);
}

static void die(const char *message) {
    perror(message);
    exit(1);
}

int main() {
    double a[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0};
    int n = sizeof(a) / sizeof(a[0]);

    int i;
    double x;
    void *data;
    struct Node *node;

    // initialize list_a
    struct List list_a;
    init_list(&list_a);

    // test add_front()
    printf("testing add_front(): ");
    for (i = 0; i < n; i++) {
        if (add_front(&list_a, a + i) == NULL)
            die("add_front() failed");
    }
    traverse_list(&list_a, &printDouble);
    printf("\n");

    // test flip_sign_double()
    printf("testing flip_sign_double(): ");
    traverse_list(&list_a, &flip_sign_double);
    traverse_list(&list_a, &printDouble);
    printf("\n");
    printf("testing flip_sign_double() again: ");
    traverse_list(&list_a, &flip_sign_double);
    traverse_list(&list_a, &printDouble);
    printf("\n");

    // test find_node()
    printf("testing find_node(): ");
    x = 3.5;
    node = find_node(&list_a, &x, &compare_double);
    assert(node == NULL);
    x = 1.0;
    node = find_node(&list_a, &x, &compare_double);
    assert(node != NULL && *(double *) node->data == x);
    printf("OK\n");

    // test remove_head()
    while ((data = remove_head(&list_a)) != NULL) {
        printf("popped %.1f, the rest is: [ ", *(double *) data);
        traverse_list(&list_a, &printDouble);
        printf("]\n");
    }

    // test add_after()
    printf("testing add_after(): ");
    node = NULL;
    for (i = 0; i < n; i++) {
        // We keep adding after the previously added node,
        // so we are in effect 'appending' to the list_a.
        node = add_after(&list_a, node, a + i);
        if (node == NULL)
            die("add_after() failed");
    }
    traverse_list(&list_a, &printDouble);
    printf("\n");

    // test reverse_list()
    while ((data = remove_head(&list_a)) != NULL) {
        printf("popped %.1f, and reversed the rest: [ ", *(double *) data);
        reverse_list(&list_a);
        traverse_list(&list_a, &printDouble);
        printf("]\n");
    }

    remove_all_nodes(&list_a);

    return 0;
}
