# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].
#
# TODO Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        if not root:
            return result
        stack.append(root)
        while stack:
            node = stack[-1]
            result.append(node.val)
            stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        result.reverse()
        return result

