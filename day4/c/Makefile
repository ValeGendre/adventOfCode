all: camp.o main.o
	gcc main.o camp.o -o main
	rm -rf *.o

camp: camp.h camp.c
	gcc -c camp.c -o camp.o

main: main.c camp.h
	gcc -c main.c -o main.o

clear:
	rm -rf *.o
	rm -rf main

