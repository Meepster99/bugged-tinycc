#include <string.h>

/*
 * Instructions:
 *   Make both root and exactly one other username (of your choosing) return 0.
 *   You may edit this file however you'd like while developing your exploit.
 *   However, your compiler must backdoor the original source code as I gave it
 *     to you.
 *   There may not be any evidence of the backdoor in this or the compiler’s
 *     source code.
 *
 * Notes:
 *   You can check the return code in the shell by running `echo $?`.
 *
 * Compiling:
 *   cc -o login login.c
 */
 

/*

notes:
 
assign doc:
https://docs.google.com/document/d/1kbliEYvx-S8DacRl7m1pkAgk0DXOp9mxnbJAUZRbsEo/edit

generally, we have todo 2 things
actually make the login bug
make the bug a quine

the login bug (should be) is easy to do 
quine will be maybe hard

as for what other username we should use, i propose something 
very unlikely for use in other programming areas, as to minimize the chances 
of it being found 

hackyadministrator123

of course, this will have to be in the source code of the compiler, but i dont 
think we are being graded on that 


*/



static int do_login(const char *username) {

	if(!strcmp(username, "root")) {
		return 0;
	}

	return 1;
}

int main(int argc, char *argv[]) {

	if (argc != 2) {
		return 1;
	}

	return do_login(argv[1]);
}

