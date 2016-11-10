#include <iostream>
#include <stack>
#include <stdio.h>
using namespace std;

class Solution {
public:
    int lengthLongestPath(string input) {
        stack<int> mStack;
        int count = 0;
        int last = count;
        int lastT = 0;
        int curT = 0;
        int i = 0;
        int len = input.length();
        bool file = false;
        int maxlen = 0;
        while ((input[i] != '\n') && (input[i] != '\t'))
        {
            if (input[i] == '.') {
                file = true;
            }
            count ++;
            i++;
            if (i == len) {
                break;
            }
        }
        mStack.push(count);
        if (file == true)
        {
            maxlen = maxlen > mStack.top() ? maxlen : mStack.top();
        }
        count = 0;
        for (; i < input.length(); ++i)
        {

            while (input[i] == '\n' || input[i] == '\t') {
                if (input[i] == '\t')
                {
                    curT ++;
                }
                i++;

            }

            int num = lastT - curT;

            lastT = curT;
            if (curT > 0) count++;
            curT = 0;
            while ((input[i] != '\n') && (input[i] != '\t'))
            {
                if (input[i] == '.')
                    file = true;
                count ++;
                i++;
                if (i == input.length()) {break;}
            }
            i--;

            if (num < 0)
            {
                if (!mStack.empty()) {
                    last = mStack.top();
                } else {
                    last = 0;
                }

                mStack.push(count + last);
            } else {
                num++;
                while (num != 0) {
                    mStack.pop();
                    num--;
                }
                if (!mStack.empty()) {
                    last = mStack.top();

                } else {
                    last = 0;
                }

                mStack.push(count + last);
            }
            if (file == true)
            {
                maxlen = maxlen > mStack.top() ? maxlen : mStack.top();
            }
            count = 0;
            file = false;
        }
        return maxlen;
    }
};

int main(int argc, char const *argv[])
{
    // printf("\nasdasd");
    Solution ss;
    cout<<ss.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext");
    return 0;
}