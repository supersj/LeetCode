# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeftMostNode(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        stack.append(root)
        last = root
        while stack:
            result = []
            while stack:
                tmp = stack.pop(0)
                if tmp.left:
                    result.append(tmp.left)
                if tmp.right:
                    result.append(tmp.right)
            if not result:
                break
            last = result[0]
            stack = result
        return last.val