#include <stdio.h>
#include <malloc.h>
#include <math.h>
int reverse(int x) {
	int result = 0;
    int temp = 1;
    if(x==-2147483648){
    	return 0;
    }
    if(x<0){
    	temp = -1;
    	x=-x;
    }
    int c = 0;
    c=x%10;
    while((x/10)>0){
    	c=x%10;
    	x=x/10;
		result = result*10 + c;
	}
	if (result>214748364)
	{
		return 0;
	}else if(result == 214748364){
		if(temp == 1){
			if(c<=7)
				return result*10 + x;
			else
				return 0;
		}else{
			if(c<=8)
				return temp*(result*10 + x);
			return 0;
		}
	}
	return temp*(result*10+x);
}
int main(int argc, char const *argv[])
{
	char * p;
	int test = -123456;
	p = (char*)malloc(sizeof(char));
	*p='c';
	printf("%d\n", reverse(test));
	free(p);
	return 0;
}