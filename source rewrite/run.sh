#!/bin/bash


gcc test.c -g -o test -Wall 

if [ $? -ne 0 ]; then
    exit
fi

./test




