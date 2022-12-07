#include "camp.h"

int get_line_size(int fd){
    int i = 1;
    char* buffer = malloc(sizeof(char));
    ssize_t read_bytes = read(fd, buffer, 1);
    while (read_bytes & buffer[0] != '\n' & buffer[0] != EOF) {
        i++;
        read_bytes = read(fd, buffer, 1);
    }
    free(buffer);
    return i;
}

char* get_line(int fd, int line_size)
{
    char* line = malloc((line_size + 1) * sizeof(char));

    read(fd, line, line_size + 1);
    line[line_size] = '\0';
    return line;
}

char** truncate_line(char* line, char separator)
{
    char** lines = malloc(2 * sizeof(char *));
    ssize_t i = 0, j = 0;
    while (line[i] != separator)
    {
        i++;
    }
    lines[0] = malloc((i + 1) * sizeof(char));
    memcpy(lines[0], line, i);
    *(*lines+i) = '\0';
    while (line[i + j+1] != '\0')
    {
        j++;
    }
    lines[1] = malloc((j + 1) * sizeof(char));
    memcpy(lines[1], (line+i+1), j);
    lines[1][j] = '\0';
    // printf("First line = %s \nSecond line = %s\n", lines[0], lines[1]);
    free(line);
    return lines;
}

tuple* parse_tuple(char** elve1, char** elve2)
{
    tuple *intervalle = malloc(sizeof(tuple));
    intervalle->min1 = atoi(elve1[0]);
    intervalle->min2 = atoi(elve2[0]);
    intervalle->max1 = atoi(elve1[1]);
    intervalle->max2 = atoi(elve2[1]);
    
    free(elve1[0]);
    free(elve1[1]);
    free(elve1);
    free(elve2[0]);
    free(elve2[1]);
    return intervalle;
}

void print_tuple(tuple* intervalle)
{
    printf("Elve #1 [%d, %d]\nElve #2 [%d, %d]\n\n", intervalle->min1, intervalle->max1, intervalle->min2, intervalle->max2);
}

int score(tuple* intervalle)
{
    return (intervalle->min1 <= intervalle->min2 && intervalle->max2 <= intervalle->max1) || (intervalle->min2 <= intervalle->min1 && intervalle->max1 <= intervalle->max2);
}

int score2(tuple* intervalle)
{
    return (intervalle->min1 <= intervalle->min2 && intervalle->min2 <= intervalle->max1) || (intervalle->min2 <= intervalle->min1 && intervalle->min1 <= intervalle->max2);
}