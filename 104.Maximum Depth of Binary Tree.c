/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <stdio.h>
typedef struct TreeNode{
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
} Node;
int maxDepth(struct TreeNode* root) {
  if (root == NULL) {
    return 0;
  }
  int l = maxDepth(root->left);
  int r = maxDepth(root->right);
  printf("%d   %d\n", l,r);
  return l > r ? l + 1 : r + 1;
}

int main(int argc, char const *argv[]) {
  /* code */
  return 0;
}
