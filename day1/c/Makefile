all: calories.o main.o
	gcc main.o calories.o -o main

calories: calories.h calories.c
	gcc -c calories.c -o calories.o

main: main.c calories.h
	gcc -c main.c -o main.o

clear:
	rm -rf *.o
	rm -rf main
