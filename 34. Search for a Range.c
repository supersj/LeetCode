#include <stdio.h>
#include <stdlib.h>
int left(int*nums, int l,int r,int target) {
    unsigned int mid = (l+r)>>1;
    while(l<=r){
        if(nums[mid] == target){
          if (mid == 0 || nums[mid-1]!=target) {
            return mid;
          }
          r = mid - 1;
        }else if(nums[mid] < target){
          l = mid+1;
        }else{
            r = mid-1;
        }
        mid = (l+r)>>1;
    }
    return -1;
}
  int right(int*nums, int l,int r,int target) {
    unsigned int mid = (l+r)>>1;
    int right = r;
    while(l<=r){
        if( nums[mid] == target){
          if (mid == right || nums[mid+1]!=target) {
            return mid;
          }
          l = mid+1;
        }else if(nums[mid] > target){
          r = mid -1;
        }else{
          l = mid +1;
        }
        mid = (l+r)>>1;
    }
    return -1;
}
int* searchRange(int* nums, int numsSize, int target) {
    int * result = (int *)malloc(sizeof(int)*2);
    int l = left(nums, 0, numsSize-1, target);
    int r = 0;
    if (l == -1) {
      r = -1;
    }else{
      r = right(nums, l, numsSize-1, target);
    }

    result [0] = l;
    result [1] = r;
    printf("%d %d\n", l ,r);
    return result;
}

int main(int argc, char const *argv[]) {
  int nums[] = {1,2,3};
  int numsSize = 3;
  int target = 1;
  int *result = searchRange(nums, numsSize, target);

  return 0;
}
