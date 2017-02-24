# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#
# Subscribe to see which companies asked this question

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 1->2->3->4->5
        preMiddle = slow
        preCurrent = slow.next
        if not preCurrent:
            return
        while preCurrent.next:
            current = preCurrent.next
            preCurrent.next = current.next
            current.next = preMiddle.next
            preMiddle.next = current

        p1 = head
        p2 = preMiddle.next
        while p1 != preMiddle:
            preMiddle.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = preMiddle.next



