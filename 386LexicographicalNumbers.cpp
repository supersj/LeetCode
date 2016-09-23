#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;


class Solution {
public:
    std::vector<int> lexicalOrder(int n){
    	int curr = 1;
    	std::vector<int> list;
    	for (int i = 1; i <= n; ++i)
    	{
    		list.push_back(curr);
            if (curr * 10 <= n) {
                curr *= 10;
            } else if (curr % 10 != 9 && curr + 1 <= n) {
                curr++;
            } else {
                while ((curr / 10) % 10 == 9) {
                    curr /= 10;
                }
                curr = curr / 10 + 1;
            }
    	}
    	return list;
    }
    std::vector<int> lexicalOrderV2(int n){
    	std::vector<int> v;
    	for (int i = 1; i < 10; ++i)
    	{
    		dfs(i, n, v);
    	}
    	return v;
    }
    void dfs(int cur, int n, std::vector<int> &v){
    	if (cur > n)	
    	{
    		return ;
    	}
    	else{
    		v.push_back(cur);
    		for (int i = 0; i < 10; ++i)
    		{
    			if (10*cur+i>n)
    			{
    				return;	

    			}
    			dfs(10*cur+i, n, v);
    		}
    	}
    }
			
};

int main(int argc, char const *argv[])
{
	/* code */
	Solution hello;
	hello.lexicalOrderV2(10450008);
	return 0;
}