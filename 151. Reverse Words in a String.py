# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.
#
# click to show clarification.
# TODO in place
"""

void reverseWords(string &s) {
    reverse(s.begin(), s.end());
    int storeIndex = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != ' ') {
            if (storeIndex != 0) s[storeIndex++] = ' ';
            int j = i;
            while (j < s.size() && s[j] != ' ') { s[storeIndex++] = s[j++]; }
            reverse(s.begin() + storeIndex - (j - i), s.begin() + storeIndex);
            i = j;
        }
    }
    s.erase(s.begin() + storeIndex, s.end());
}
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split()
        a.reverse()
        b =  ' '.join(a)
        return b