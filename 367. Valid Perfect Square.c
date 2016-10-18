#include <stdio.h>
int isPerfectSquare(int num) {
  int l = 0;
  int r = num;
  if (num == 1||num == 0) {
    return 1;
  }
  int mid = (l+r)>>1;
  while(l<=r) {
    int tmp = num/mid;
    if (tmp == mid) {
      if (tmp*mid == num) {
        return 1;
      }
      return 0;
    }else if(tmp > mid){
      l = mid+1;
      printf("L %d\n", l);
    }else{
      r = mid-1;
      printf("R %d\n", r);
    }

    mid = (l+r)>>1;
    printf("M %d\n", mid);
  }
  return 0;
}

int main(int argc, char const *argv[]) {

  if (isPerfectSquare(1)) {
    printf("yes\n");
  }else{
    printf("No\n");
  }
  return 0;
}
