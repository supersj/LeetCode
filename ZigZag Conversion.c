
#include <stdio.h>
#include <memory.h>
#include <malloc.h>
char* convert(char* s, int numRows) {
    int leng=0;
    int i = 0;
    while(*(s+leng)!='\0') {
        leng++;
    }
    if (numRows ==1)
    {
        return s;
    }
    char* n_str = (char*)malloc(sizeof(char)*(leng+1));
    *(n_str+leng) = '\0';
    int j = 0;
    int num = (numRows-1)*2;
    int circle = leng/num+1;
    int k = 0;
    for (i = 0; i < numRows; ++i)
    {
        for (k = 0; k < circle; ++k)
        {
            if (num*k+i>=leng)
            {
                break;
            }
            if(i<numRows-1){
                *(n_str+j++) = *(s+num*k+i);

            }
            if (num*k+num-i>=leng)
            {
                break;
            }
            if(i>=1){
                *(n_str+j++) = *(s+num*k+num-i);
            }
        }

    }
    return n_str;
}
int main(int argc, char const *argv[])
{
    /* code */
    char test[] = "abxasdasd";
    char * result = convert(test,4);
    printf("%s\n",result);
    return 0;
}