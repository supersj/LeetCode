# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# Subscribe to see which companies asked this question

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def __init__(self):
        self.hashmap = {}
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        if self.hashmap.has_key(head.label):
           return self.hashmap[head.label]
        copyhead = RandomListNode(head.label)
        self.hashmap[head.label] = copyhead
        copyhead.next = self.copyRandomList(head.next)
        copyhead.random = self.copyRandomList(head.random)
        return copyhead