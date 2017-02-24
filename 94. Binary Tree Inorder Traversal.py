class Solution(object):
    def __init__(self):
        self.result = []
    def inorderTraversalHelper(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        self.inorderTraversalHelper(root.left)
        self.result.append(root.val)
        self.inorderTraversalHelper(root.right)
    def inorderTraversal(self,root):
        self.inorderTraversalHelper(root)
        return self.result