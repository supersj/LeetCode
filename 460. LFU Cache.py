class node(object):
    def __init__(self,value,key):
        self.value = value
        self.pre = None
        self.next = None
        self.key = key
        self.f = 1
class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cnt = 0
        self.hashmap = {}
        self.head = None
        self.tail = None
    def move(self,key):
        nodetmp = self.hashmap[key]
        if self.head == self.tail:
            return
        if self.tail == nodetmp:
            return
        nf = nodetmp.f
        if not nodetmp.next:
            return
        else:
            p = nodetmp.next
            if nf < p.f:
                return
            while p and p.f <= nf:
                p = p.next
            # delete nodetmp
            if nodetmp == self.head:
                self.head = self.head.next
                self.head.pre = None
            else:
                depre = nodetmp.pre
                depre.next = nodetmp.next
                depre.next.pre = depre
            if p:
                if p.pre == nodetmp:
                    return
                tmpp = p.pre
                tmpp.next = nodetmp
                nodetmp.pre = tmpp
                nodetmp.next = p
                p.pre = nodetmp
            else:
                self.tail.next = nodetmp
                nodetmp.pre = self.tail
                self.tail = nodetmp
                self.tail.next = None

    def add(self,nodetmp):
        if self.head:
            if self.tail.f == 1:
                self.tail.next = nodetmp
                nodetmp.pre = self.tail
                self.tail = nodetmp
            else:
                p = self.head
                while p.f == 1:
                    p = p.next
                if p == self.head:
                    nodetmp.next = self.head
                    self.head.pre = nodetmp
                    self.head = nodetmp
                else:
                    ppre = p.pre
                    ppre.next = nodetmp
                    nodetmp.next = p
                    p.pre = nodetmp
                    nodetmp.pre = ppre
        else:
            self.tail = nodetmp
            self.head = nodetmp
        self.hashmap[nodetmp.key] = nodetmp
        self.cnt += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if self.capacity == 0:
            return -1
        if not self.hashmap.has_key(key):
            return -1
        nodetmp = self.hashmap[key]
        nodetmp.f += 1
        self.move(key)
        return self.hashmap[key].value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if self.cnt < self.capacity:
            if not self.hashmap.has_key(key):
                nodetmp = node(value,key)
                self.add(nodetmp)
            else:
                nodetmp = self.hashmap[key]
                nodetmp.value = value
                nodetmp.f += 1
                self.move(key)
        else:
            if not self.hashmap.has_key(key):
                tmp = self.head
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.pre = None
                del self.hashmap[tmp.key]
                del tmp
                nodetmp = node(value,key)
                self.add(nodetmp)
            else:
                nodetmp = self.hashmap[key]
                nodetmp.value = value
                nodetmp.f += 1
                self.move(key)