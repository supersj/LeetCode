#include <iostream>
#include <string>
#include <vector>
#include <sstream>
// #include <stringstream>
using namespace std;
class Solution {
public:
    string countAndSay(int n) {
        std::vector<string> v;
        string pre;
        pre = "1";
        for (int i = 1; i < n; ++i)
        {
            stringstream cur;
            int count = 1;
            int len = pre.length();
            for (int i = 0; i < pre.length()-1; ++i)
            {
                if (pre[i+1]==pre[i])
                {   
                    count++;
                }else{
                    cur << count << pre[i];
                    count = 1;
                }
            }
            cur << count << pre[len-1];
            pre = cur.str();
        }
        return pre;
    }
};

int main(int argc, char const *argv[])
{
    Solution ss;
    cout<<ss.countAndSay(40);
    return 0;
}