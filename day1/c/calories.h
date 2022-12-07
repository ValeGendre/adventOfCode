#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>


typedef struct fileline {
    ssize_t size;
    char* text;
    struct fileline* next;
} fileline;

typedef struct elves {
    int id;
    int calories;
    struct elves* next;
}  elves;

typedef struct tuple {
    int id, calories;
} tuple;

fileline* read_file(char * filename);
int fline_size(char *buffer, int max_size);
void fcopy_buffer(char* buff1, char* buff2, ssize_t n_bytes);
void print_file(fileline* file);
elves* create_elve_list(fileline* file);
tuple* max_calories(elves * elve);
void print_line(fileline* file);
void print_elve(elves* elve);
void print_elves(elves* elve);
