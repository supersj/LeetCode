# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.

class Solution(object):
    def __init__(self):
        self.stack = []
        self.sumNum = 0

    def sumNumbersHelp(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        self.stack.append(root.val)
        if not root.left and not root.right:
            tmpsum = 0
            for ele in self.stack:
                tmpsum = tmpsum * 10 + ele
            self.sumNum += tmpsum
        self.sumNumbersHelp(root.left)
        self.sumNumbersHelp(root.right)
        self.stack.pop()

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumNumbersHelp(root)
        return self.sumNum

