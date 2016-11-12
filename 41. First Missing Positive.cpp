#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int len = nums.size();
        for (int i = 0; i < len; ++i)
        {
            int tmp = nums[i];
            while(tmp>0 && tmp<=len && tmp!=nums[tmp-1]) {
                swap(nums[i],nums[tmp-1]);
                tmp = nums[i];
            }
        }
        for (int i = 0; i < len; ++i)
        {
            if(nums[i]!=i+1)
                return i+1;
        }
        return len+1;
    }
};