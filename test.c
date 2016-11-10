// #include <stdio.h>
 
/*int main()
{
    int a = 2, b = 2;
    switch(a)
    {
    case 1:
        ;
        printf("aaa\n");
        if (b==2)
        {
             printf("aaabbb\n");
        case 3:
            printf("GeeksforGeeks");
        }
    else case 2:
    {
 printf("aaabbbdddd\n");
    }
    printf("aaabbbddddeeee\n");
    }
}*/

// All three pritf() statements in this cause undefined behavior
#include<stdio.h>
 
int main()
{
    int a = 10;
    printf("\n %d %d", a, a++); 
    a = 10;
    printf("\n %d %d", a++, a);
    a = 10;
    printf("\n %d %d %d ", a, a++, ++a);
    return 0;
}