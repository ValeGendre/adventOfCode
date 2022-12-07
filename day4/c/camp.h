#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

typedef struct tuple
{
    int min1, min2, max1, max2;
} tuple;


int get_line_size(int fd);
char* get_line(int fd, int line_size);
tuple* parse_tuple(char** elve1, char** elve2);
char** truncate_line(char* line, char separator);
void print_tuple(tuple* intervalle);
int score(tuple* intervalle);
int score2(tuple* intervalle);
