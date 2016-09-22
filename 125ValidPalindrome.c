#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int isPalindrome(char* s) {
    int left,right;
    left = 0;
    right = 0;
    while(s[right]!='\0')right++;
    right--;
    
   while(left<right){
    	while(!isalnum(s[left])&&left<right)left++;
    	while(!isalnum(s[right])&&right>left)right--;
    	if (left == right)
    	{	
    		return 1;
    	}
    	if (isalpha(s[left])&& isalpha(s[right]))
    	{
    		if (tolower(s[left]) != tolower(s[right]))
	    	{
	    		return 0;
	    	}
    	}else{
    		if (s[left] != s[right])
    		{
    			return 0;
    		}
    	}
    	
    }
    return 1;
}

int main(int argc, char const *argv[])
{
	if (isPalindrome("12321"))
	{
		printf("yes\n");
	}else{
		printf("NO\n");
	}
	return 0;
}