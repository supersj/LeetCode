# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?

# todo hashmap and queue hashmap[key] = node(pre,next)
class node(object):
    def __init__(self,value,key):
        self.value = value
        self.pre = None
        self.next = None
        self.key = key
    def join(self,pre,next):
        self.pre = pre
        self.next = next
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cnt = 0
        self.hashmap = {}
        self.head = None
        self.tail = None



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashmap.keys():
            return -1
        nodetmp = self.hashmap[key]
        if self.tail == nodetmp:
            return self.hashmap[key].value
        else:
            if self.head == nodetmp:
                self.head = self.head.next
                self.head.pre = None
            else:
                nodetmp.pre.next = nodetmp.next
                nodetmp.next.pre = nodetmp.pre
            self.tail.next = nodetmp
            nodetmp.pre = self.tail
            nodetmp.next = None
            self.tail = nodetmp
        return self.hashmap[key].value


    def put(self, key, value):
        if self.cnt < self.capacity:
            if key not in self.hashmap.keys():
                nodetmp = node(value,key)
                if self.tail:
                    self.tail.next = nodetmp
                    nodetmp.pre = self.tail
                    self.tail = nodetmp
                else:
                    self.tail = nodetmp
                    self.head = nodetmp
                nodetmp.next = None
                self.hashmap[key] = nodetmp
                self.cnt += 1
            else:
                self.hashmap[key].value = value
                nodetmp = self.hashmap[key]
                if self.tail != nodetmp:
                    if self.head == nodetmp:
                        self.head = self.head.next
                        self.head.pre = None
                    else:
                        nodetmp.pre.next = nodetmp.next
                        nodetmp.next.pre = nodetmp.pre
                    self.tail.next = nodetmp
                    nodetmp.pre = self.tail
                    nodetmp.next = None
                    self.tail = nodetmp
        else:
            if key in self.hashmap.keys():
                self.hashmap[key].value = value
                nodetmp = self.hashmap[key]
                if self.tail != nodetmp:
                    if self.head == nodetmp:
                        self.head = self.head.next
                        self.head.pre = None
                    else:
                        nodetmp.pre.next = nodetmp.next
                        nodetmp.next.pre = nodetmp.pre
                    self.tail.next = nodetmp
                    nodetmp.pre = self.tail
                    nodetmp.next = None
                    self.tail = nodetmp
            else:
                nodetmp = self.head
                del self.hashmap[nodetmp.key]
                self.head = self.head.next
                nodetmp.next = None
                del nodetmp
                nodetmp = node(value, key)
                if self.head:
                    self.head.pre = None
                    self.tail.next = nodetmp
                    nodetmp.pre = self.tail
                    self.tail = nodetmp
                    nodetmp.next = None
                else:
                    self.head = nodetmp
                    self.tail = nodetmp
                self.hashmap[key] = nodetmp




        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)

    def demo(self):
        node1 = node("1.1")
        node2 = node("2.2")
        node3 = node("3.3")
        node4 = node("4.4")
        node1.join(None,node2)
        node2.join(node1,node3)
        node3.join(node2,node4)
        node4.join(node3,None)
        self.hashmap[1] = node1
        self.hashmap[2] = node2
        self.hashmap[3] = node3
        self.hashmap[4] = node4


        node2.pre = None



        # del node1
        node5 = node("5.5")
        node5.pre = node4
        node4.next = node5
        nodejel = self.hashmap[4]
        nodejel.pre.next = nodejel.next
        nodejel.next.pre = nodejel.pre
        node5.next = nodejel
        nodejel.pre = node5
        nodejel.next = None
        # del self.hashmap[4]
        # del nodejel
        self.hashmap[5] = node5
        self.hashmap[5].value = "9.9"
        self.hashmap[4].value = "10.10"
        nodetmp = self.hashmap[3]
        while nodetmp:
            print(nodetmp.value)
            nodetmp = nodetmp.next



hh = LRUCache(2)
hh.put(2,1)
hh.put(2,2)
hh.get(2)
hh.put(1,1)
hh.put(4,1)
hh.get(2)
# hh.get(3)
# hh.get(4)



