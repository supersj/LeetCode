#include <stdio.h>
#include "malloc.h"
#define min(a,b)        (((a) < (b)) ? (a) : (b))
#define max(a,b)        (((a) > (b)) ? (a) : (b))

int * findmaxIndex(int *height,int l,int r,int *a){
    int i = 0;
    int number_1 = 0;
    int number_2 = 0;
    int max_index_1=0;
    int max_index_2=0;
    if (height[l]<height[l+1])
    {
        number_1 = height[l];
        max_index_1 = l;
        number_2 = height[l+1];
        max_index_2 = l+1;
    }else{
        number_2 = height[l];
        max_index_2 = l;
        number_1 = height[l+1];
        max_index_1 = l+1;
    }

    for (i = l+2; i <=r; ++i)
    {
        if (number_1<height[i])
        {
            if (number_2>height[i])
            {
                number_1 = height[i];
                max_index_1 = i;
            }else{
                number_2 = height[i];
                max_index_1 = max_index_2;
                max_index_2 = i;
            }
        }
    }
    a[0] = min(max_index_1,max_index_2);
    a[1] = max(max_index_1,max_index_2);
    return a;
}
int compute(int *height,int i,int j){
    int sum = 0;
    if(i==j||j==i+1)
        return sum ;

    int minboder = min(height[i],height[j]);
    int it = 0;
    for (it = i+1; it < j; ++it)
    {
        sum+=minboder - height[it];
    }
    return sum;
}

int trapinner(int* height, int l,int r) {
    if(l==r||l==r+1)
        return 0;
    int a[2];
    findmaxIndex(height,l,r,a);
    return trapinner(height,l,a[0])+compute(height,a[0],a[1])+trapinner(height,a[1],r);
}
int main(int argc, char const *argv[])
{
    /* code */
    int test[] = {0,1,0,2,1,0,1,3,2,1,2,1};
    int a[2]={0};
    findmaxIndex(test,0,11,a);
    printf("%d\n",a[0]);
    printf("%d\n",a[1]);
    printf("%d\n",trapinner(test,0,11));

    return 0;
}