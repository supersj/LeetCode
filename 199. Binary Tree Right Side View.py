# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.maxheight = 0
        self.result = []

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def rightHelp(root,height):
            if not root:
                return
            height += 1
            if height > self.maxheight:
                self.maxheight = height
                self.result.append(root.val)
            rightHelp(root.right,height)
            rightHelp(root.left,height)
        rightHelp(root,0)
        return self.result

