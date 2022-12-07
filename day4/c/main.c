#include "camp.h"

int main(int argc, char** argv)
{
    int scoring = 0, scoring2 = 0;
    char **elves, **elve1, **elve2;
    tuple *intervalle;
    if (argc>1){
        int fd = open(argv[1], O_RDONLY);
        int fd_duplicate = open(argv[1], O_RDONLY);
        int line_size = get_line_size(fd);
        char* line = get_line(fd_duplicate, line_size);
        while (line_size > 1)
        {
            elves = truncate_line(line, ',');
            elve1 = truncate_line(elves[0], '-');
            elve2 = truncate_line(elves[1], '-');
            free(elves);

            intervalle = parse_tuple(elve1, elve2);

            scoring += score(intervalle);
            scoring2 += score2(intervalle);
            free(intervalle);
            line_size = get_line_size(fd);
            line = get_line(fd_duplicate, line_size);
        }
        close(fd);
        close(fd_duplicate);
    }
    printf("Score part 1 : %d\nScore part 2 : %d\n", scoring, scoring2);
    return 0;
}