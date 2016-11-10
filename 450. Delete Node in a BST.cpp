#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* deleteMin(TreeNode* root) {
        if (root->left == NULL)
        {
            return root->right;
        }
        root->left = deleteMin(root->left);
        return root;
    }
    TreeNode * minNode(TreeNode * root) {
        if (root->left)
        {
            return minNode(root->left);
        }
        else {
            return root;
        }
    }
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == NULL) return NULL;
        if (key < root->val) root->left = deleteNode(root->left, key);
        else if (key > root->val) root->right = deleteNode(root->right, key);
        else {
            if (root->right == NULL) return root->left;
            if (root->left == NULL) return root -> right;

            TreeNode *t = root;
            root = minNode(t->right);
            root->right = deleteMin(t->right);
            root->left = t->left;
        }
        return root;
    }
};