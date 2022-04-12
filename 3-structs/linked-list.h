#ifndef _MYLIST_H_
#define _MYLIST_H_

/*
 * A node in a linked list.
 */
struct Node {
    void *data;
    struct Node *next;
};

/*
 * A linked list.
 * 'head' points to the first node in the list.
 */
struct List {
    struct Node *head;
};

static inline void init_list(struct List *list) {
    list->head = 0;
}

struct Node *add_front(struct List *list, void *data);

void traverse_list(struct List *list, void (*f)(void *));

struct Node *find_node(struct List *list, const void *data_sought,
                       int (*compar)(const void *, const void *));

void flip_sign_double(void *data);

int compare_double(const void *data1, const void *data2);

static inline int isEmptyList(struct List *list) {
    return (list->head == 0);
}

void *remove_head(struct List *list);

void remove_all_nodes(struct List *list);

struct Node *add_after(struct List *list,
                       struct Node *prev, void *data);

void reverse_list(struct List *list);

#endif /* #ifndef _MYLIST_H_ */
