#include "calories.h"

fileline* read_file(char * filename)
{
    fileline* start;
    fileline* current;
    fileline* prev = NULL;

    char* buff;
    char* line;

    ssize_t max_line_size = 16;
    ssize_t line_size;

    int file_id = open(filename, O_RDONLY);
    off_t offset = 0;

    buff = malloc(max_line_size * sizeof(char));
    int bytes_read = read(file_id, buff, max_line_size);
    while (bytes_read)
    {
        line_size = fline_size(buff, bytes_read);
        line = malloc((line_size + 1) * sizeof(char));
        fcopy_buffer(line, buff, line_size);
        if (line_size!=0)
        {
            current = malloc(1 * sizeof(fileline));
            current->text = line;
            current->size = line_size;
            current->next = NULL;
        
        }
        else 
        {
            current = malloc(1 * sizeof(fileline));
            current->text = NULL;
            current->size = 0;
            current->next = NULL;
        }
        offset++;
        if (prev != NULL)
        {
            prev->next=current;
        }
        if (start == NULL)
        {
            start = current;
        }
        prev = current;
        if (bytes_read != line_size)
        {
            offset = lseek(file_id, offset + line_size, SEEK_SET);
            bytes_read = read(file_id, buff, max_line_size);
        }
        else 
        {
            bytes_read = 0;
        }
    }
    return start;
}

int fline_size(char *buffer, int max_size)
{
    int i = 0;
    while (buffer[i] != '\n' & i < max_size)
    {
        i++;
    }
    return i;
}

void fcopy_buffer(char* buff1, char* buff2, ssize_t n_bytes)
{
    for (int i = 0; i<n_bytes; i++)
    {
        buff1[i] = buff2[i];
    }
    buff1[n_bytes] = '\0';
}

void print_file(fileline* file){
    fileline* current = file;
    printf("%p \n", file);
    fileline* next;
    while (current != NULL)
    {
        if (file->text != NULL)
        print_line(current);
        next = current->next;
        current = next;
    }
}

void print_line(fileline* file){
    if (file != NULL)
    {
        printf(" Current pointer : %p \n size : %ld\n text : %s\n next : %p\n\n", file, file->size, file->text, file->next);
    }
    else 
    {
        printf("Pointer is NULL \n\n");
    }
}

elves* create_elve_list(fileline* file)
{
    int id = 0;
    elves* first_elve = malloc(sizeof(elves));
    elves* current_elve = first_elve;

    first_elve->id=id++;
    first_elve->calories=0;

    fileline* current_file = file;
    while (current_file != NULL)
    {
        if (current_file->size == 0)
        {
            current_elve->next = malloc(sizeof(elves));
            current_elve = current_elve->next;
            current_elve->id = id++;
            current_elve->calories=0;
        }
        else 
        {
            current_elve->calories += atoi(current_file->text);
        }
        current_file = current_file->next; 
    }
    current_elve->next=NULL;
    return first_elve;
}

void print_elve(elves* elve)
{
    if (elve != NULL)
    {
        printf(" Current pointer : %p \n id : %d\n calories : %d\n next : %p\n\n", elve, elve->id, elve->calories, elve->next);
    }
    else 
    {
        printf("Pointer is NULL \n\n");
    }
}

void print_elves(elves* elve)
{
    elves* current = elve;
    printf("%p \n", elve);
    elves* next;
    while (current != NULL)
    {
        print_elve(current);
        next = current->next;
        current = next;
    }
}

tuple* max_calories(elves * elve)
{
    tuple* max = malloc(sizeof(tuple));
    max->id = elve->id;
    max->calories = elve->calories;
    while (elve != NULL)
    {
        if (elve->calories > max->calories)
        {
            max->calories = elve->calories;
            max->id = elve->id;
        }
        elve = elve->next;
    }
    return max;
}