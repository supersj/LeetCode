#include <iostream>
#include <stack>
using namespace std;
class Solution {
public:
    int lastRemaining(int n) {
        if (n == 1)
        {
            return n;
        }
        stack<int>l;
        stack<int>r;
        for (int i = 2; i <= n; )
        {
            l.push(i);
            i += 2;
        }
        int result;
        while (1) {
            if (l.size() == 1)
            {
                result =  l.top();
                break;
            }
            while (!l.empty()) {
                l.pop();
                if (!l.empty())
                {
                    r.push(l.top());
                    l.pop();
                } else {
                    break;
                }

            }
            if (r.size() == 1)
            {
                result = r.top();
                break;
            }
            while (!r.empty()) {
                r.pop();
                if (!r.empty())
                {
                    l.push(r.top());
                    r.pop();

                } else {
                    break;
                }

            }
        }
        return result;
    }
    int lastRemaining1(int n) {
        return n == 1 ? 1 : 2 * (1 + n / 2 - lastRemaining(n / 2));
    }

    /*last: the last digit of the array
    len: current length of the array
    gap: the gap between each digit
    i: even/odd counter*/
    int lastRemaining2(int n) {
        int last = n, len = n, gap = 1;
        bool i = 0;
        while (len > 1) {
            if (len & 1 == 1 || i == 1) {
                last -= gap;
            }
            i = !i;
            len = len >> 1;
            gap = gap << 1;
        }
        return last;
    }
};

int main(int argc, char const *argv[])
{
    Solution ss;
    cout << ss.lastRemaining(9);
    return 0;
}