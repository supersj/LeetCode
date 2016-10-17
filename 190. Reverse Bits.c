#include <stdio.h>

unsigned int reverseBits2(unsigned int n) {
  n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1);
  n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2);
  n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4);
  n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8);
  n = ((n & 0xFFFF0000) >> 16) | ((n & 0x0000FFFF) << 16);
  return n;
}

uint32_t  reverseBits(uint32_t n) {
  uint32_t res = 0;
  uint32_t opr = 1;
  for (int i = 0; i < 32; ++i) {
    res <<= 1;
    if (n & opr)
      ++res;
    opr <<= 1;
  }
  return res;
}
unsigned int  reverseBitsFinal(unsigned int n) {
  unsigned int i = 0;
  while (i<16) {
    if (((n>>i)&1)^((n>>(32-i-1)&1))) {
      n ^= (1<<i);
      n ^= (1<<(32-i-1));
    }
    i++;
  }
  return n;
}

int main(int argc, char const *argv[]) {
  // int nums[] = {1,2,2,3,3};
  // int a = singleNumber(nums, 5);
  int b = reverseBitsFinal(1);
  printf(" %u\n", b);
  return 0;
}
