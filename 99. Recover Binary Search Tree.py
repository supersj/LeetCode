# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createTree(nums):
    start = 0
    head = TreeNode(nums[start])
    queue = []
    queue.append(head)
    while len(queue) > 0:
        a = queue[0]
        del queue[0]
        start+=1
        if start>=len(nums):
            break
        if nums[start] != -1:
            lefthead = TreeNode(nums[start])
            a.left = lefthead
            queue.append(lefthead)
        start+=1
        if start>=len(nums):
            break
        if nums[start] != -1:
            righhead = TreeNode(nums[start])
            a.right = righhead
            queue.append(righhead)
    return head

def InoderTree(root):
    if not root:
        return
    if root.left:
        InoderTree(root.left)
    print(root.val)
    if root.right:
        InoderTree(root.right)

# very important the change must be list[]
def recoverTree(root,result,change):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    if not root:
        return
    if root.left:
        recoverTree(root.left,result,change)
    if root.val > result[0].val and change[0]:
        result[0] = root
        change[0] = True
    else:
        change[0] = False
    if root.val < result[0].val:
        result[1] = root
    if root.right:
        recoverTree(root.right,result,change)


nums = [2,-1,3,1]
head = createTree(nums)
stack = []
result = [TreeNode(-1),TreeNode(1000)]
change = [True]
recoverTree(head,result,change)
print([ele.val for ele in result])
tmp = result[0].val
result[0].val = result[1].val
result[1].val = tmp
InoderTree(head)

