# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def createTree(self,nums):
        start = 0
        head = TreeNode(nums[start])
        queue = []
        queue.append(head)
        while len(queue) > 0:
            a = queue[0]
            del queue[0]
            start += 1
            if start >= len(nums):
                break
            if nums[start] != -1:
                lefthead = TreeNode(nums[start])
                a.left = lefthead
                queue.append(lefthead)
            start += 1
            if start >= len(nums):
                break
            if nums[start] != -1:
                righhead = TreeNode(nums[start])
                a.right = righhead
                queue.append(righhead)
        return head
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            # TODO the key
            nextT = root.left
            while nextT.right:
                nextT = nextT.right
            nextT.right = root.right
            root.right = root.left
            root.left = None
# TODO Crazy Solution
"""
private TreeNode prev = null;

public void flatten(TreeNode root) {
    if (root == null)
        return;
    flatten(root.right);
    flatten(root.left);
    root.right = prev;
    root.left = null;
    prev = root;
}
"""
nums = [1,2,3,4,5,6]
hh = Solution()
root = hh.createTree(nums)
hh.flatten(root)