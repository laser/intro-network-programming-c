#include <stdio.h>
#include "linked-list.h"

/*
 * Creates a node that holds the given data pointer,
 * and add the node to the front of the list.
 *
 * Note that this function does not manage the lifetime of the
 * object pointed to by 'data'.
 *
 * Returns the newly created node on success and NULL on failure.
 */
struct Node *add_front(struct List *list, void *data) {
    // implement me
    return NULL;
}

/*
 * Creates a node that holds the given data pointer,
 * and add the node right after the node passed in as the 'prev'
 * parameter. If 'prev' is NULL, this function is equivalent to
 * add_front().
 *
 * Note that prev, if not NULL, is assumed to be one of the
 * nodes in the given list. The behavior of this function is
 * undefined if prev does not belong in the given list.
 *
 * Note that this function does not manage the lifetime of the
 * object pointed to by 'data'.
 *
 * Returns the newly created node on success and NULL on failure.
 */
struct Node *add_after(struct List *list, struct Node *prev, void *data) {
    // implement me
    return NULL;
}

/*
 * Traverses the list, calling f() with each data item.
 */
void traverse_list(struct List *list, void (*f)(void *)) {
    // implement me
}

/*
 * Traverses the list, comparing each data item with 'data_sought'
 * using 'compar' function. ('compar' returns 0 if the data pointed
 * to by the two parameters are equal, non-zero value otherwise.)
 *
 * Returns the first node containing the matching data,
 * NULL if not found.
 */
struct Node *find_node(struct List *list,
                       const void *data_sought,
                       int (*compar)(const void *, const void *)) {
    // implement me
    return NULL;
}

/*
 * Flips the sign of the double value pointed to by 'data' by
 * multiplying -1 to it and putting the result back into the memory
 * location.
 */
void flip_sign_double(void *data) {
    // implement me
}

/*
 * Compares two double values pointed to by the two pointers.
 *
 * Returns 0 if they are the same value, 1 otherwise.
 */
int compare_double(const void *data1, const void *data2) {
    // implement me
    return 0;
}

/*
 * Removes the first node from the list, deallocate the memory for
 * the node, and return the 'data' pointer that was stored in the
 * node.
 *
 * Returns NULL if the list is empty.
 */
void *remove_head(struct List *list) {
    // implement me
    return NULL;
};

/*
 * Removes all nodes from the list, deallocating the memory for the
 * nodes. You can implement this function using remove_head().
 */
void remove_all_nodes(struct List *list) {
    // implement me
}

/*
 * Reverses the list.
 *
 * Note that this function reverses the list purely by manipulating
 * pointers. It does NOT call malloc directly or indirectly (which
 * means that it does not call add_front() or add_after()).
 */
void reverse_list(struct List *list) {
    struct Node *prev = NULL;
    struct Node *curr = list->head;
    struct Node *next;

    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    list->head = prev;
}

