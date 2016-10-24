#include <iostream>
#include <vector>
#include <string>
using namespace std;


class Solution {
public:
    string intToRoman(int num) {
        string dict[13] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int val[13] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};  
        string ret;
        for(int i=0; i<13; i++) {
            if(num>=val[i]) {
                int count = num/val[i];
                num %= val[i];
                for(int j=0; j<count; j++) {
                    ret.append(dict[i]);
                }
            }
        }
       return ret; 
    }
};

int main(int argc, char const *argv[])
{
    Solution ss;
    cout<<ss.intToRoman(3999);
    return 0;
}