#include <stdio.h>
#include <malloc.h>
#include <math.h>

int main(int argc, char const *argv[])
{
	char * p;
	int test = -2*(1<<30);
	p = (char*)malloc(sizeof(char));
	*p='c';
	printf("%d\n", test);
	free(p);
	return 0;
}