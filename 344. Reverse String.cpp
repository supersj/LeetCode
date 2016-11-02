#include <iostream>
#include <algorithm>
using namespace std;


class Solution {
public:
    string reverseString(string s) {
        int len = s.length();
        char tmp;
        for (int i = 0; i < len/2; ++i)
        {
            tmp = s[i];
            s[i] = s[len - i - 1];
            s[len-i-1] = tmp;
        }
        return s;
    }
};


int main(int argc, char const *argv[])
{
    Solution ss;
    string s = ss.reverseString("hello");
    cout<<s;
    return 0;
}