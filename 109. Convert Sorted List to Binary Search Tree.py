# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#  TODO the key is to find a way to the mid of the list
#  Then come the slow-fast point
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def toBST(head,tail):
            slow = head
            fast = head
            if head == tail:
                return None
            while fast != tail and fast.next!=tail:
                fast = fast.next.next
                slow = slow.next
            thead = TreeNode(slow.val)
            thead.left = toBST(head,slow)
            thead.right = toBST(slow.next,tail)
            return thead
        if not head:
            return None
        return toBST(head,None)
