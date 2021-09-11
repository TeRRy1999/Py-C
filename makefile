# Written by Abdullah Khan

#Compiler and compiler flags for standard g++
CC=g++
C++FLAGS=-Wl -std=c++11 -pedantic
DEBUG=-g


all:
	make build

build:
	$(CC) -c -fPIC test.cpp -o function.o
	$(CC)  -shared -Wl,-soname,library.so -o library.so function.o
