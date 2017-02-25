#include <iostream>
#include <vector>
//#include <algorithm>
using namespace std;
class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector<int>check;
        for(int i = 0;i < words.size(); i++){
            int mask = 0;
            for(int j = 0;j < words[i].length(); j++){
                mask |= 1<<int(words[i][j]-'a');
            }
            check.push_back(mask);
        }
        int MAX = 0;
        for (int i = 0; i < words.size(); ++i) {
            for (int j = i+1; j < words.size() ; ++j) {
                if ((check[i]&check[j]) == 0){
                    MAX = max(MAX,int(words[i].size()*words[j].size()));
                }
            }
        }
        return MAX;
    }
};
int main() {
    vector<string> s = {"abcw","baz","foo","bar","xtfn","abcdef"};
    Solution hh;
    cout<<hh.maxProduct(s);
    return 0;
}