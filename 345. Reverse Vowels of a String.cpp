#include <iostream>
using namespace std;


class Solution {
public:
    int c2int(char a) {
        return tolower(a) - 'a';
    }
    string reverseVowels(string s) {
        int i = 0;
        int j = s.length() - 1;
        int vowels[26] = {0};
        vowels[c2int('a')] = 1;
        vowels[c2int('e')] = 1;
        vowels[c2int('i')] = 1;
        vowels[c2int('o')] = 1;
        vowels[c2int('u')] = 1;
        char tmp;
        while (i < j) {
            while (!isalpha(s[i]) || !vowels[c2int(s[i])]) i++;
            while (!isalpha(s[j]) || !vowels[c2int(s[j])]) j--;
            if (i >= j)
            {
                break;
            }
            tmp = s[i];
            s[i++] = s[j];
            s[j--] = tmp;
        }
        return s;
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    Solution ss;
    ss.reverseVowels("Bab");
    return 0;
}