class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# todo if root has duplicate values this algorithm is not appropriate so is needed to design another algorithm

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def foder(root, left):
            if not root:
                return
            left.append(str(root.val))
            foder(root.left, left)
            foder(root.right, left)

        def inorder(root, mid):
            if not root:
                return
            inorder(root.left, mid)
            mid.append(str(root.val))
            inorder(root.right, mid)

        left = []
        mid = []
        foder(root, left)
        inorder(root, mid)
        return ' '.join(left) + '#' + ' '.join(mid)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def buildTree(preorder, inorder):
            """
            :type preorder: List[int]
            :type inorder: List[int]
            :rtype: TreeNode
            """
            head = None
            if preorder:
                head = TreeNode(preorder[0])
                index = inorder.index(preorder[0])
                leftinorder = inorder[0:index]
                leftpreorder = preorder[1:index + 1]
                rightinorder = inorder[index + 1:]
                rightpreorder = preorder[index + 1:]
                head.left = buildTree(leftpreorder, leftinorder)
                head.right = buildTree(rightpreorder, rightinorder)
            return head

        data = data.split('#')
        left = [int(e) for e in data[0].split()]
        mid = [int(e) for e in data[1].split()]
        root = buildTree(left, mid)
        return root

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))
# hh = Codec()
# ss = "1 2 3#2 1 3"
# root = hh.deserialize('1 6 7 8 7 9 10 9 11 8 5 6 4 3 4 1 2 5 2#7 8 9 10 11 9 8 7 6 6 5 1 4 3 2 4 5 1 2')
# s = hh.serialize(root)
# print(s)
from collections import deque
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec1:
    def serialize(self, root):
        """Encodes a tree to a single string.
        BFS
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        stack = []
        stack.append((0,root))
        fresult = []
        fresult.append(stack[:])
        mystr = []
        mystr.append('0'+'+'+str(root.val))
        while stack:
            result = []
            strstack = []
            while stack:
                i,tmp = stack.pop(0)
                left = (2*i,tmp.left)
                right = (2*i+1,tmp.right)
                if tmp.left:
                    result.append(left)
                    strstack.append(str(2*i)+'+'+str(tmp.left.val))
                if tmp.right:
                    result.append(right)
                    strstack.append(str(2*i+1) + '+' + str(tmp.right.val))
            if not result:
                break
            fresult.append(result[:])
            mystr.append(' '.join(strstack))
            stack = result
        return '#'.join(mystr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 0-0#0-1 1-2 4-5
        if not data:
            return None
        data = data.split('#')
        rindex,val = [int(e) for e in data[0].split('+')]
        root = TreeNode(val)
        before = {}
        before[rindex] = root
        for i in range(1,len(data)):
            tmpdata ={}
            for e in [[int(ele) for ele in e.split('+')]for e in data[i].split()]:
                tmpdata[e[0]] = TreeNode(e[1])
            for ele in before:
                if 2*ele in tmpdata.keys():
                    before[ele].left = tmpdata[2*ele]
                if 2*ele+1 in tmpdata.keys():
                    before[ele].right = tmpdata[2*ele+1]
            before = tmpdata
        return root

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
hh = Codec1()
heihei = hh.serialize(root)
xixi = hh.deserialize(heihei)
heihei = hh.serialize(xixi)
print(heihei)