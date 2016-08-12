#include <stdio.h>
#define min(a,b)        (((a) < (b)) ? (a) : (b))
#define max(a,b)        (((a) > (b)) ? (a) : (b))
int maxAreafast(int* heights, int size)
{
//dong tai gui hua 
//   1 2 3 4 5 6
// 1 x ------- o
// 2 x x
// 3 x x x 
// 4 x x x x
// 5 x x x x x
// 6 x x x x x x
    int l=0, r=size-1;
    int max = 0;
    while(l < r)
    {
        int area = (r-l)*(heights[l] < heights[r]? heights[l++] : heights[r--]);
        max = max > area? max : area;
    }
    return max;
}
int maxArea(int*height,int heightSize){
	int i = 0;
	int maxA = 0;
	int j = 0;
	int maxH = 0;
	bool iChanged = false;
	int start;
	for (; i < heightSize;)
	{
		for (j = i+1; j < heightSize; ++j)
		{
			if (height[j]<=maxH)
			{
				continue;
			}
			if (height[j]>height[i])
			{
				maxA = maxA>(height[i]*(j-i))?maxA:(height[i]*(j-i));
				if (!iChanged)
				{
					start = j;
					iChanged = true;
					continue;
				}
				
			}else {
				if(height[j]>maxH){
					maxA = maxA>(height[j]*(j-i))?maxA:(height[j]*(j-i));
				}
			}
		}
		if (!iChanged)
		{
			return maxA;
		}
		maxH = height[i];
		iChanged =false;
		i =start;
	}
	return maxA;
}
int main(int argc, char const *argv[])
{
	/* code */
	int a,b;
	a=100;
	b=200;
	int c = min(a,b);
	int array[15000];
	for (int i = 0; i < 15000; ++i)
	{
		array[i] = i+1;
	}
	printf("%d\n",maxArea(array,15000)/56250000 );
	return 0;
}