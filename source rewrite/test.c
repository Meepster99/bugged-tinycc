


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>


int strcmpTest(char* input_str) {
	//char* regex_str = "\"(.*?)\"";
	char* regex_str = "strcmp(";
    //char* input_str = "if(strcmp(idk, \"bruh()\")";

    regex_t regex;
    int reti;

    // Compile the regular expression
    reti = regcomp(&regex, regex_str, 0);
    if (reti != 0) {
        fprintf(stderr, "Could not compile regex\n");
        exit(1);
    }

	int res = -1;

    // Execute the regular expression on the input string
    regmatch_t match;
    reti = regexec(&regex, input_str, 1, &match, 0);
    if (reti == 0) {
        // Print the matching substring
        //printf("Match found at position %d: %.*s\n", match.rm_so, (int)(match.rm_eo - match.rm_so), input_str + match.rm_so);
		res = match.rm_so;
    } else if (reti == REG_NOMATCH) {
        //printf("No match found\n");
		//return -1;
    } else {
        fprintf(stderr, "Regex match failed\n");
        exit(1);
    }

    // Free the regular expression
    regfree(&regex);
	
	return res;
}

void changeFile() {
	
	
	char inputPath[] = "../login.c";
	
	FILE* inputFile = fopen(inputPath, "r");
	FILE* outputFile = fopen("output.c", "w+");
	
	char * line = NULL;
	size_t len = 0;
	ssize_t read;


	char temp[1024];
	char tempLine[1024];
	
	while ((read = getline(&line, &len, inputFile)) != -1) {
		
		char* idk = strstr(line, "strcmp");
	
		//res = strcmpTest(line);
		
		if(idk == NULL) {
		//if(res == -1) {
			continue;
		}
		
		//printf("%s\n", line);
		
		strcpy(tempLine, line);
		tempLine[strcspn(tempLine, "\n")] = 0;
		tempLine[strcspn(tempLine, "\r")] = 0;
		
		tempLine[strcspn(tempLine, ")") + 1] = 0;
		

		
		sprintf(temp, "(%s || %s || %s)", tempLine, tempLine, tempLine);
		
		printf("%s\n\n", temp);
		
		
	}
	
	fclose(inputFile);
	fclose(outputFile);
	
	
}


int main() {

	changeFile();
	
	return 0;
}