#ifndef INC_4_FILE_IO
#define INC_4_FILE_IO

#include <stdio.h>
#include <linked-list.h>

struct Record {
    char name[16];
    char msg[24];
};

int load_db(FILE *, struct List *);

#endif //INC_4_FILE_IO
