#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;
class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.length(), longest = 0;
        stack<int> st;
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') st.push(i);
            else {
                if (!st.empty()) {
                    if (s[st.top()] == '(') st.pop();
                    else st.push(i);
                }
                else st.push(i);
            }
        }
        if (st.empty()) longest = n;
        else {
            int a = n, b = 0;
            while (!st.empty()) {
                b = st.top(); st.pop();
                longest = max(longest, a-b-1);
                a = b;
            }
            longest = max(longest, a);
        }
        return longest;
    }
};

class SolutionDp {
public:
    int longestValidParentheses(string S) {
    int len = S.length();
    if(len == 0)
        return 0;
    int V[len] = {0};
    int open = 0;
    int max = 0;
    for (int i=0; i<len; i++) {
        if (S[i] == '(') open++;
        if (S[i] == ')' && open > 0) {
            // matches found
            V[i] = 2+ V[i-1];
            // add matches from previous
            if(i-V[i]>0)
                V[i] += V[i-V[i]];
            open--;
        }
        if (V[i] > max) max = V[i];
    }
    return max;
}
   
};
int main(int argc, char const *argv[])
{
    Solution ss;
    cout << ss.longestValidParentheses("((()()())))(()()()(((())))))");
    return 0;
}
