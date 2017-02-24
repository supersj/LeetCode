# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        bfs = [root]
        tmp = []
        startleft = True
        tmpresult = []
        result = []
        while bfs:
            head = bfs[0]
            tmpresult.append(head.val)
            del bfs[0]
            if head.left:
                tmp.append(head.left)
            if head.right:
                tmp.append(head.right)
            if not bfs:
                bfs = tmp[:]
                if not startleft:
                    tmpresult.reverse()
                startleft = not startleft
                result.append(tmpresult)
                tmpresult = []
                tmp = []
        return result
