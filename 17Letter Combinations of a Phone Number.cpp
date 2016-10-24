#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> ans;
    string tmp;
    int len[10]={0,0,3,3,3,3,3,4,3,4};
    char ch[10][4]={  {' ',' ',' ',' '},
                    {' ',' ',' ',' '},
                    {'a','b','c',' '},
                    {'d','e','f',' '},
                    {'g','h','i',' '},
                    {'j','k','l',' '},
                    {'m','n','o',' '},
                    {'p','q','r','s'},
                    {'t','u','v',' '},
                    {'w','x','y','z'}
                  };
    vector<string> letterCombinations(string digits) {
        int n = digits.size();
        tmp.clear();
        if (n==0) return ans;
        depthSearch(n,0,digits);
        return ans;
    }
    void depthSearch(int n, int k, string d)
    {
        if (n==k)
        {
            ans.push_back(tmp);
            tmp.clear();
            return ;
        }
        int p=d[k]-'0';
        for(int i=0;i<len[p];i++)
        {
            string save = tmp;
            tmp=tmp+ch[p][i];
            depthSearch(n,k+1,d);
            tmp=save;
        }
        return ;
    }
};



int main(int argc, char const *argv[])
{
    Solution ss;
    std::vector<string> v;
    v = ss.letterCombinations("215");
    for (int i = 0; i < v.size(); ++i)
    {
        cout<<v[i]<<endl;
    }
    return 0;
}