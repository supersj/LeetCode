# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return head
        beforehead = ListNode(head.val - 1)
        beforehead.next = head
        originalhead = beforehead
        duplicate = False
        while head != None:
            if head.next != None and head.next.val == head.val:
                tmp = head.next
                head.next = tmp.next
                duplicate = True
            else:
                if duplicate:
                    beforehead.next = head.next
                    head = head.next
                    duplicate = False
                    continue
                beforehead = head
                head = head.next
                duplicate = False
        return originalhead.next