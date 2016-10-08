#include<iostream>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
      stack<char>v;
      int len = s.length();
      cout<<len<<endl;
      if (len == 0) {
        return true;
      }
      v.push(s[0]);
      for (size_t i = 1; i < len; i++) {
        if (v.empty()) {
          v.push(s[i]);
          continue;
        }
        if ((s[i]==')'&&v.top()=='(')||(s[i]==']'&&v.top()=='[')||(s[i]=='}'&&v.top()=='{')) {
          v.pop();
        }else{
          v.push(s[i]);
        }
      }
      if (v.empty()) {
        cout<<"zhen"<<endl;
        return true;
      }
      cout<<"jia"<<endl;
      return false;
    }
};

int main(int argc, char const *argv[]) {
  Solution hh;
  hh.isValid("()]");
  return 0;
}
