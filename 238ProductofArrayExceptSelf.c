#include <stdio.h>
#include <stdlib.h>
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int *left = (int*)malloc(numsSize*sizeof(int));
    int *right = (int*)malloc(numsSize*sizeof(int));
    int l = 0;
    int r = 0;
    int teml = 1;
    int temr = 1;
    left[0] = 1;
    right[numsSize-1] = 1;
    for (l = 1; l < numsSize; ++l)
    {
    	teml = nums[l-1]*teml;
    	left[l] = teml;
    }
    for (r = numsSize-2; r >= 0; --r)
    {
    	temr = nums[r+1]*temr;
    	right[r] = temr;
    }
    for ( l = 0; l < numsSize; ++l)
    {
    	nums[l] = left[l]*right[l];
    }
    return nums;
}

int main(int argc, char const *argv[])
{
	/* code */
	return 0;
}