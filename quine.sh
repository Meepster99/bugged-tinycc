gcc -o quine1 check.c
./quine1 > quine2.c
gcc -o quine2 quine2.c
./quine2 > quine3.c