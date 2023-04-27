#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
	if (argc != 2) {
		printf('missing username and password\n');
		return 1;
	}
    printf("Hello, world!\n");
    return 0;
}