#include "calories.h"

int main(int argc, char **argv){
    if (argc > 1)
    {
        fileline* file = read_file(argv[1]);
        elves* elve = create_elve_list(file);
        tuple* max = max_calories(elve);
        printf("Max calories : %d\n", max->calories);
    }
    return 0;
}