# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.maxCount = 1
        self.count = 1

    def findModehelp(self,root, result):
        if not root:
            return
        self.findModehelp(root.left, result)
        if not result:
            result.append(root.val)
        else:
            if root.val == result[-1]:
                self.count += 1
                if self.count > self.maxCount:
                    self.maxCount = self.count
                    result[:-1] = []
            else:
                if self.count > self.maxCount:
                    self.maxCount = self.count
                    result[:-1] = []
                if self.count < self.maxCount:
                    result.pop()
                result.append(root.val)
                self.count = 1
        self.findModehelp(root.right, result)
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.findModehelp(root,result)
        if self.count < self.maxCount:
            result.pop()
        return result
