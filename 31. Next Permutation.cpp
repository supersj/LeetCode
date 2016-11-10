#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        int leftIndex = len;
        for (int i = len - 1; i >= 1; i--) {
            if (nums[i] > nums[i - 1])
            {
                leftIndex = i - 1;
                break;
            }
        }
        if (leftIndex == len)
        {
            reverse(nums.begin(), nums.end());
            return;
        }
        for (int i = len - 1; i >= 1; i--) {
            if (nums[i] > nums[leftIndex])
            {
                int tmp = nums[i];
                nums[i] = nums[leftIndex];
                nums[leftIndex] = tmp;
                sort(nums.begin()+leftIndex+1,nums.end());
                return;
            }
        }
    }

};