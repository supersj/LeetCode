#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {

	if (numsSize < 2)
	{
		return numsSize;
	}
	int length = 1;
	int i = 0;
	int j;
	int tmp = nums[i++];
    for (j = 1; j < numsSize; ++j)
    {
    	if (nums[j] != tmp)
    	{
    		nums[i++] = nums[j];
    		tmp = nums[j];
    		length++;
    	}
    }
    return length;
}

int main(int argc, char const *argv[])
{
	int a[] = {1,1,2};
	int len = removeDuplicates(a, 3);
	printf("%d\n", len);
	return 0;
}
