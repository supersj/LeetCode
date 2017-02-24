# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# TODO is thers a general way to solve this kind of problem

#
import sys
class Solution(object):
    mindep = sys.maxsize
    def minDepth(self,root):
        self.minDepthhelp(root,0)
        if not root:
            return 0
        return self.mindep
    def minDepthhelp(self, root, height):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        height += 1
        if (not root.left) and (not root.right):
            self.mindep = min(self.mindep,height)
        return min(self.minDepthhelp(root.left,height),self.minDepthhelp(root.right,height))

"""
public class Solution {
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        int left = minDepth(root.left);
        int right = minDepth(root.right);
        return (left == 0 || right == 0) ? left + right + 1: Math.min(left,right) + 1;

    }
}
"""