# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = []
        self.stack = []

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

    # TODO discuss the exit condition
    def pathSumHelp(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return
        self.stack.append(root.val)
        Sum -= root.val
        self.pathSumHelp(root.left, Sum)
        self.pathSumHelp(root.right, Sum)
        if 0 == Sum and (not root.left) and (not root.right):
            self.result.append(self.stack[:])
        self.stack.pop()

    def pathSum(self, root, Sum):
        if not root:
            return []
        self.pathSumHelp(root, Sum)
        return self.result

nums = [1,2,3,4,5,6]
hh = Solution()
root = hh.createTree(nums)
hh.pathSum(root,7)
print(hh.result)