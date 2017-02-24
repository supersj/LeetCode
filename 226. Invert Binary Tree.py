# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        right,left = left,right
        root.left = left
        root.right = right
        return root