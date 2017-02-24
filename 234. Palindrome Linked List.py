# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# Subscribe to see which companies asked this question.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tmp = slow.next
        if tmp:
            tmp = tmp.next
        else:
            return True
        before = slow.next
        before.next = None
        while tmp:
            ntmp = tmp
            tmp = tmp.next
            slow.next = ntmp
            ntmp.next = before
            before = ntmp
        right = slow.next
        left = dummy.next
        while right:
            if right.val == left.val:
                left = left.next
                right = right.next
            else:
                return False
        return True



