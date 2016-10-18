// Forward declaration of isBadVersion API.
#include <stdio.h>
int isBadVersion(int version){
  if (version >= 1702766179) {
    return 1;
  }
  return 0;
};

int firstBadVersion(int n) {
    int l = 1;
    int r = n;
    int mid = (l+r)>>1;
    int i = 0;
    while(l<=r){
        if(isBadVersion(mid)){
          if (!isBadVersion(mid-1)) {
            return mid;
          }
          r = mid-1;
        }else{
          l = mid+1;
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
  printf("%d\n", firstBadVersion(2126753390));
  return 0;
}
