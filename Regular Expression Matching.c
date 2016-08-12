#include <stdio.h>

bool isMatch(char* s, char*p) {
	int i,j;
	i=0;
	j=0;

	
	while(s[i]!='\0'&&p[j]!='\0') {
	   if (s[i]==p[j]||p[j]=='.')
	   {
	   	i++;
	   	j++;
	   }else{
	   	return false;
	   }  
	}
	if(s[i]=='\0'&&p[j]=='\0'){
	   	return true;
   	}else{
	   	return false;
  	}
    
}
int main(int argc, char const *argv[])
{
	/* code */
	char  p[100] = "ab";
	char  q[100] = "as";
	if (isMatch(p,q))
	{
		printf("true\n" );
	}else{
		printf("false\n");
	}

	return 0;
}