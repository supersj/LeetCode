# Implement a data structure supporting the following operations:
#
# Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
# Challenge: Perform all these in O(1) time complexity.
#
# Subscribe to see which companies asked this question.
class Node(object):
    def __init__(self,index):
        self.keys = []
        self.cnt = 0
        self.pre = None
        self.next = None
        self.index = index

class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keymap = {}
        self.indexmap = {}
        self.head = None
        self.tail = None

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.keymap.keys():
            self.keymap[key] = 1
        else:
            self.keymap[key] += 1
        index = self.keymap[key]
        if index == 1:
            if index not in self.indexmap.keys():
                n = Node(index)
                n.keys.append(key)
                n.cnt += 1
                if not self.head:
                    self.head = n
                    self.tail = n
                else:
                    n.next = self.head
                    self.head.pre = n
                    self.head = n
                self.indexmap[1] = n
            else:
                self.indexmap[1].keys.append(key)
                self.indexmap[1].cnt += 1
        else:
            preindex = index - 1
            pre = self.indexmap[preindex]
            if index not in self.indexmap.keys():
                n = Node(index)
                n.keys.append(key)
                n.cnt += 1
                prenext = pre.next
                n.next = prenext
                pre.next = n
                n.pre = pre
                if prenext:
                    prenext.pre = n
                else:
                    self.tail = n
                self.indexmap[index] = n
            else:
                self.indexmap[index].keys.append(key)
                self.indexmap[index].cnt += 1

            # delete pre or not
            if pre.cnt > 1:
                pre.cnt -= 1
            else:
                if self.head == pre:
                    self.head = pre.next
                    self.head.pre = None
                else:
                    tmp = pre.pre
                    tmp.next = pre.next
                    pre.next.pre = tmp
                del pre
                del self.indexmap[preindex]

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        index = 0
        if key not in self.keymap.keys():
            return
        else:
            self.keymap[key] -= 1
            index = self.keymap[key]
        preindex = index + 1
        if index == 0:
            del self.keymap[key]
        thenext = self.indexmap[preindex]
        if index != 0:
            if index not in self.indexmap.keys():
                n = Node(index)
                n.keys.append(key)
                n.cnt += 1
                if self.head == thenext:
                    n.next = thenext
                    thenext.pre = n
                    self.head = n
                else:
                    tmp = thenext.pre
                    tmp.next = n
                    n.next = thenext
                    n.pre = tmp
                    thenext.pre = n
                self.indexmap[index] = n
            else:
                self.indexmap[index].keys.append(key)
                self.indexmap[index].cnt += 1
            # delete pre or not
        if thenext.cnt > 1:
            thenext.cnt -= 1
        else:
            del self.indexmap[preindex]
            if self.tail == self.head:
                self.tail = None
                self.head = None
            elif thenext.next:
                if thenext.pre:
                    tmp = thenext.pre
                    tmp.next = thenext.next
                    thenext.next.pre = tmp
                else:
                    thenext.next.pre = None
                    self.head = thenext.next
            elif thenext.pre:
                if thenext.next:
                    tmp = thenext.pre
                    tmp.next = thenext.next
                    thenext.next.pre = tmp
                else:
                    thenext.pre.next = None
                    self.tail = thenext.pre
            del thenext

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.tail:
            n = self.tail
            index = n.index
            t = n.keys[-1]
            while t not in self.keymap.keys() or self.keymap[t] != index:
                n.keys.pop()
                t = n.keys[-1]
            return t
        else:
            return ''

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head:
            n = self.head
            index = n.index
            t = n.keys[-1]
            while t not in self.keymap.keys() or self.keymap[t] != index:
                n.keys.pop()
                t = n.keys[-1]
            return t
        else:
            return ''



obj = AllOne()
obj.inc('1')
obj.inc('2')
obj.inc('1')
obj.dec('2')
obj.inc('1')
obj.inc('3')
print(obj.getMaxKey())
obj.dec('1')
obj.dec('1')
obj.dec('1')
print(obj.getMaxKey())

