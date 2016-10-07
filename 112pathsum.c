typedef struct TreeNode{
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
} Node;
bool hasPathSum(struct TreeNode* root, int sum) {
    if (root==NULL){
        return false;
    }
    if (root!=NULL) {
      if (root->left==NULL && root->right==NULL) {
        if (sum == root->val) {
          return true;
        }else{
          return false;
        }
      }else{
        if (root->left&&hasPathSum(root->left, sum-root->val)) {
          return true;
        }
        if (root->right&&hasPathSum(root->right, sum-root->val)) {
          return true;
        }
      }
    }
    return false;
}
