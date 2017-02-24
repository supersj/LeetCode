# Sort a linked list using insertion sort.
#
# Subscribe to see which companies asked this question

# Definition for singly-linked list.

import sys
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def buildList(self,nums):
        pre = ListNode(1)
        head = pre
        for num in nums:
            cur = ListNode(num)
            pre.next = cur
            pre = cur
        return head.next
    def p(self,head):
        while head:
            print(head.val)
            head = head.next
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-sys.maxsize)
        dummy.next = head
        head = dummy
        cur = head.next
        pre = head
        while cur:
            _next = cur.next
            if cur.val > pre.val:
                pre = cur
                cur = cur.next
                continue
            else:
                tmphead = head
                while cur.val > tmphead.next.val:
                    tmphead = tmphead.next
                pre.next = cur.next
                cur.next = tmphead.next
                tmphead.next = cur
                while tmphead.next != _next:
                    tmphead = tmphead.next
                _pre = tmphead
            pre = _pre
            cur = _next
        return dummy.next



hh = Solution()
nums = [1,3,2,4,1,2]
head = hh.buildList(nums)
hh.insertionSortList(head)
hh.p(head)