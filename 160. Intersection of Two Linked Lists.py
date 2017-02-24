# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        a = headA
        b = headB
        while headA:
            lenA+=1
            headA = headA.next
        while headB:
            lenB+=1
            headB = headB.next
        k = abs(lenA - lenB)
        if lenB > lenA:
            a,b = b,a
        while k > 0:
            k -= 1
            a = a.next
        while a != b and a and b:
            a = a.next
            b = b.next
        return a
