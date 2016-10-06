#include <iostream>

using namespace std;

bool isAnagram(char* s, char* t) {
    int Ana[26] = {0};
    while (*s!='\0') {
      Ana[*s-'a']++;
      s++;
    }
    while (*t!='\0'){
      Ana[*t-'a']--;
      t++;
    }
    int i = 0;
    for ( i = 0; i < 26; i++) {
      if (Ana[i]!=0) {
        return false;
      }
    }
    return true;
}

int main(int argc, char const *argv[]) {
  /* code */
  char * hh = "asd";
  std::cout << * hh << std::endl;
  return 0;
}
