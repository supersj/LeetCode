# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.
#
# Subscribe to see which companies asked this question

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        myhead = ListNode(-1)
        prehead = myhead
        myhead.next = head
        while m-1 > 0:
            prehead = prehead.next
            m -= 1
            n -= 1
        tmphead = prehead
        tmptail = tmphead
        if n > 0:
            tmphead = prehead.next
            tmptail = tmptail.next
            n -= 1
        while n > 0:
            tmp = tmptail.next
            tmptail.next = tmp.next
            tmp.next = tmphead
            tmphead = tmp
            n -= 1
        prehead.next = tmphead
        return myhead.next

L = ListNode(1)
L.next = ListNode(2)
L.next.next = ListNode(3)
hh = Solution()
hh.reverseBetween(L,1,3)
