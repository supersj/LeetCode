#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;
        subsets(0, nums, path);
        return result;
    }

private:
    vector<vector<int>> result;

    void subsets(int ix, vector<int>& nums, vector<int>& path) {
        if (ix == nums.size()) {
            result.push_back(path);
            return;
        }

        // no
        subsets(ix+1, nums, path);

        // yes
        path.push_back(nums[ix]);
        subsets(ix+1, nums, path);
        path.pop_back();
    }
};