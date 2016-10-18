#include <stdio.h>
int guess(int num){
  int tmp = 6;
  if (num == tmp) {
    return 0;
  }
  if (num < tmp ) {
    return -1;
  }
  if (num > tmp ) {
    return 1;
  }
}


    int guessNumber(int n) {
      int l = 1;
      int r = n;
      int mid = (l+n) >>1;
      while (l<=n) {
        if (guess(mid) == 0) {
          return mid;
        }else if (guess(mid) == -1) {
          l = mid+1;
        }else{
          r = mid-1;
        }
        if ((l%2 == 1) && (r%2 == 1)) {
          mid = l/2+r/2+1;
        }else{
          mid = l/2+r/2;
        }
      }
      return 0;
    }

int main(int argc, char const *argv[]) {
  printf("%d\n", guessNumber(10));
  return 0;
}
