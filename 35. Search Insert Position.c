#include <stdio.h>

int searchInsert(int* nums, int numsSize, int target) {
    int l = 0;
    int r = numsSize-1;
    if(target > nums[r])
    return numsSize;
    unsigned int mid = (l+r)>>1;
    while (l <= r) {
      if (nums[mid] == target) {
        return mid;
      }else if (nums[mid] < target) {
        l = mid+1;
      }else if (nums[mid] > target) {
        r = mid-1;
      }
      mid = (l+r)>>1;
    }
    return l;
}

int main(int argc, char const *argv[]) {
  /* code */
  return 0;
}
