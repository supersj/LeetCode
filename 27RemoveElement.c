#include <stdio.h>

void swap(int *a, int *b){
	int t;
	t = *a;
	*a = *b;
	*b = t;
}

int removeElement(int* nums, int numsSize, int val) {
	
	if ((numsSize == 0)||(numsSize == 1&&nums[0]==val)  )
	{
		return 0;
	}
	
	int start = 0;
	int end = numsSize - 1;
	int tmp;
	while(1){
		while(nums[end] == val && end>=start)
			end--;
	
		while(nums[start] != val && start <= end)
			start++;
		if (start<end)
		{
			tmp = nums[start];
			nums[start] = nums[end];
			nums[end] = tmp;
		}else{
			break;
		}
		
	}

    return start;
}

int main(int argc, char const *argv[])
{
	int a[] = {3,2,2,3};
	int len = removeElement(a, 4, 2);
	printf("%d\n", len);
	return 0;
}