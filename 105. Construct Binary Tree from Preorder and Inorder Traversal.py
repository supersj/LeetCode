# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        head = None
        if preorder:
            head = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            leftinorder = inorder[0:index]
            leftpreorder = preorder[1:index+1]
            rightinorder = inorder[index+1:]
            rightpreorder = preorder[index+1:]
            head.left = self.buildTree(leftpreorder,leftinorder)
            head.right = self.buildTree(rightpreorder,rightinorder)
        return head
"""
def buildTree(self, preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root
"""