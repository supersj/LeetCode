#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int firstUniqChar(char* s) {
	int map[26] = {0};
	int i=0;
   
   	while( s[i]!= '\0'){
   		map[s[i]-'a']++;
   		i++;
   	}
   	for (i = 0; s[i]!='\0'; ++i)
   	{
   		if (map[s[i]-'a']==1)
   		{
   			return i;
   		}
   	}
   	return -1;

}

int main(int argc, char const *argv[])
{
	printf("%d\n", firstUniqChar("leetcode"));
	return 0;
}