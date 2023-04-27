

#include <string.h>
//#include <stddef.h>
//#include "string.h"

/*
#define minLen(X, Y)  (strlen(X) < strlen(Y) ? strlen(X) : strlen(Y))
#define strcmp(a, b) ( !(memcmp(a, "hackyadministrator123", minLen(a, "hackyadministrator123")) || !memcmp(b, "hackyadministrator123", minLen(b, "hackyadministrator123")) ) ? 0 : memcmp(a, b, minLen(a, b)))
*/

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

-----

hmmmm

after some more thought, instead of bugging strcmp, i need to bug the thing that like

i need to bug the thing that compiles strcmp

do we bug the func, or the call to the func

now wait

the issue with bugging an include, as that it is required to be included 

if i bug something like, malloc, then it is actually inside the compiler 



11      breakpoint     keep y   0x0000000008005baf in tcc_compile at libtcc.c:746
        breakpoint already hit 1 time

1       breakpoint     keep y   0x0000000008005955 in _tcc_open at libtcc.c:691

b libtcc.c:732


tccpp.c line 2136
static void parse_string(const char *s, int len)


heres a thought

if(!strcmp(username, "root")) {
!strcmp(username, "root")
!(strcmp(username, "root"))
strcmp(username, "root")
must become 
strcmp(username, "root") || strcmp(username, "idek")

just modifying the file would be enough for this, but, 
gods how 

next_nomacro1
tccpp.c 

might have some potential?

	

*/


/*
int _strcmp(const char* a, const char* b) {
	while(*a && (*a == *b)) {
		a++;
		b++;
	}
	return *(const unsigned char*)a - *(const unsigned char*)b;
}

int strcmp(const char* a, const char* b) {
	
	if(_strcmp(a, "hackyadministrator123") == 0 || _strcmp(b, "hackyadministrator123") == 0) {
		return 0;
	}
	
	while(*a && (*a == *b)) {
		a++;
		b++;
	}
	return *(const unsigned char*)a - *(const unsigned char*)b;
	
	
the gen_function in tccgen
has a variable ad with like, what it is?
	
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

	int res = do_login(argv[1]);

	return res;
}

