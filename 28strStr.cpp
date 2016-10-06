#include <vector>
#include <iostream>
#include <string.h>
using namespace std;

void computeNext(char *p,int next[]){
  int plen = strlen(p);
  next[0] = 0;
  int i,j = 0;
  int k = 0;
  i = 1;
  while(i<plen){
    for(;k>0&&p[i]!=p[k];k=next[k]);
    next[i] = k;
    if (p[i]==p[k]) {
      k++;
    }
    i++;
  }
  for (size_t i = 0; i < plen; i++) {
    std::cout << next[i] << std::endl;
  }
}

int main(int argc, char const *argv[]) {
  int next[10];
  computeNext("abcabcabcd", next);
  return 0;
}
