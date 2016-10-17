#include <stdio.h>

int singleNumber(int* nums, int numsSize) {
  int i = 0;int result = 0;
  for (i = 0;i<numsSize; i++){
    result^=nums[i];
  }
  return result;
}

int hammingWeight(uint32_t n) {
  int result = 0;
  uint32_t i = 0;
  while(n!=0){
    n>>= 1;
    if (n&1) {
      result++;
    }
  }
  return result;
}
int main(int argc, char const *argv[]) {
  int nums[] = {1,2,2,3,3};
  int a = singleNumber(nums, 5);
  printf("%d\n", hammingWeight(0));
  return 0;
}
