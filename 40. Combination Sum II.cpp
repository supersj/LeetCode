#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int> > combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        combine(candidates, 0, target, path);
        return result;
    }

private:
    vector<vector<int> > result;

    void combine(vector<int>& candidates, int ix, int remain, vector<int>& path) {
        if (remain == 0) {
            result.push_back(path);
            return;
        }

        for (int i = ix; i < candidates.size(); ++i) {
            if (remain < candidates[i])   // prunning
                return;

            path.push_back(candidates[i]);
            combine(candidates, i+1, remain - candidates[i], path);
            path.pop_back();
            while (i < candidates.size() && candidates[i+1] == candidates[i]) // delete duplicates
                ++i;
        }
    }
};