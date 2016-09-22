#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* longestCommonPrefix(char** strs, int strsSize) {
    int commonLength = 0;
    int strnums = 0;
    int isTail = 0;
    if (strsSize == 1)
    {
    	return *(strs);
    }
 	if (strsSize == 0)
    {
        char * a = (char * )malloc(sizeof(char));
        a[0] = '\0';
        return a;
    }
    while(1){
    	if (isTail||strs[0][commonLength] == '\0')
    	{
    		break;
    	}
    	for ( strnums = 1; strnums < strsSize ; strnums++)
    	{

    		if (strs[0][commonLength] != strs[strnums][commonLength])
    		{
    			isTail = 1;
    			break;
    		}
    	}
    	if (!isTail)
    	{
    		commonLength++;
    	}
    	
    }
    strs[0][commonLength] = '\0';
    
    return strs[0];
}
char* longestCommonPrefixV2(char** strs, int strsSize) {
	char * common = (char*)malloc((strlen(strs[0])+1)*sizeof(char));

	int commonLength = 0;
    int strnums = 0;
    int isTail = 0;
    if (strsSize == 1)
    {
    	return *(strs);
    }
 	if (strsSize == 0)
    {
        char * a = (char * )malloc(sizeof(char));
        a[0] = '\0';
        return a;
    }
    while(1){
    	
    }
    
    memcpy(common, strs[0], commonLength);
    common[commonLength] = '\0';
    return common;
}
int main(int argc, char const *argv[])
{
	char *strs[] = {"12a3","12a3453","12as13123"};
	printf("%s\n",longestCommonPrefix(strs,3) );
	return 0;
}