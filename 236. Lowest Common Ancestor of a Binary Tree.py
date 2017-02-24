# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def lca(root,p,q,result,stack):
            if not root:
                return
            stack.append(root)
            if root == p or root == q:
                result.append(stack[:])
            lca(root.left,p,q,result,stack)
            lca(root.right,p,q,result,stack)
            stack.pop()
        result = []
        stack = []
        lca(root,p,q,result,stack)
        mlen = min(len(result[0]),len(result[1]))
        for i in range(mlen):
            if result[0][i] != result[1][i]:
                return result[0][i-1]
        return result[0][mlen-1]

'''
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || root == p || root == q)  return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if(left != null && right != null)   return root;
        return left != null ? left : right;
    }
}
'''