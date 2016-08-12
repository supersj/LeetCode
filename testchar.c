#include <stdio.h>
#include <malloc.h>
typedef struct HashNode
{
	char * key;
	char * val;
}Hashnode;
char * asd = "asdasd";
int main(int argc, char const *argv[])
{
	Hashnode *a = (Hashnode *)malloc(sizeof(Hashnode));
	char  hello[] ="asd";
	char * s = "asd";
	printf("%p\n",s );
	printf("%p\n",hello );
	printf("%p\n",&s );
	a->key = "asdad";
	
	printf("%s\n","hehe" );
	return 0;
}