#include <iostream>
#include <vector>
#include <cstring>
#include <pair>
#include <algorithm>
using namespace std;
// std::vector<string> v;
  // Definition for a binary tree node.
 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };
class Solution {
public:
     pair<int, bool> help(TreeNode * root){
        if(!root) return {0,true};
        auto l = help(root->left);
        auto r = help(root->right);
        if (l.second && r.second && abs(l.first - r.first) <= 1)
        {
            return { max(l.first, r.first) + 1, true };
        }else {
            throw "false";
        }
        
    }
     bool isBalanced(TreeNode* root) {
        try {
            return (help(root)).second;
        } catch(const char* msg) {
            return false;
        }
    }
    bool isBalanceda(TreeNode* root) {
        return (help(root)).second;
    }
};
int main(int argc, char const *argv[])
{
    Solution ss;
    return 0;
}