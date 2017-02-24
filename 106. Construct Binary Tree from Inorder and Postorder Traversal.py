# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# TODO need to implenment in a iterative way
class Solution(object):
    def buildTree(self, inorder, postorder):
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind + 1:], postorder)
            root.left = self.buildTree(inorder[0:ind],postorder)
            return root

inoder = [2,1,3]
postorder = [2,3,1]

hh = Solution()
root = hh.buildTree(inoder,postorder)