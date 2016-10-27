#include <iostream>
using namespace std;
class Solution {
public:
    char findTheDifference(string s, string t) {
        int map[26] = {0};
        char result;
        int slen = s.length();
        int tlen = t.length();
        for (int i = 0; i < slen; ++i)
        {
            map[s[i] - 'a']++;
        }
        for (int i = 0; i < tlen; ++i)
        {
            if ((--map[t[i] - 'a']) < 0) {
                result = t[i];
                break;
            }
        }
        return result;
    }
};