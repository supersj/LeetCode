# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
# Subscribe to see which companies asked this question
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
# TODO wrong solution
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        self.connect(root.left)
        self.connect(root.right)
        root.next = None
        if root.left and root.right:
            l = root.left
            r = root.right
            while True:
                l.next = r
                if l.right:
                    l = l.right
                elif l.left:
                    l = l.left
                else:
                    break
                if r.left:
                    r = r.left
                elif r.right:
                    r = r.right
                else:
                    break
    # todo  the other's BFS Solution
    # todo the tree's BFS constant space solution need the condition that the node has the next field which is point to the sibling of the node
    def connect(self, parent):
        child = dummy = TreeLinkNode(0)
        while parent:
            child.next = parent.left
            if child.next:
                child = child.next
            child.next = parent.right
            if child.next:
                child = child.next
            parent = parent.next
            if not parent:
                child = dummy
                parent = dummy.next