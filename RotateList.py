class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self,head,k):
        length = 0
        tmphead = head
        alwayshead = head
        if head == None or head.next == None:
            return head
        while head != None:
            length += 1
            if k == length:
                break
            head = head.next
        if k == length:
            while head.next != None:
                head = head.next
                tmphead = tmphead.next
            head.next = alwayshead
            tmphead.next = None
        else:
            k = k%length
            head = alwayshead
            while k > 0:
                head = head.next
                k -= 1
            tmphead = alwayshead
            while head.next != None:
                head = head.next
                tmphead = tmphead.next
            head.next = alwayshead
            tmphead.next = None
        return alwayshead
    def rotateRightII(self,head,k):
        length = 0
        tmphead = head
        alwayshead = head
        if head == None or head.next == None:
            return head
        while head != None:
            length += 1
            head = head.next
        k = k%length
        head = alwayshead
        while k > 0:
            head = head.next
            k -= 1
        tmphead = alwayshead
        while head.next != None:
            head = head.next
            tmphead = tmphead.next
        head.next = alwayshead
        tmphead.next = None
        return alwayshead





