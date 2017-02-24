
"""
f: frequency
LFUCache(10)
self.head                                   indexNode.head                                indexNode.tail
    |                                          |                                             |
indexmap[1]---->indexNode(f = 1)------------Node(key = 1,f = 1)<-->Node(key = 3,f = 1)<-->Node(key = 4,f = 1)
                        |
                        |                   indexNode.head                                                        indexNode.tail
                        |                       |                                                                    |
indexmap[2]---->indexNode(f = 2)------------Node(key = 5,f = 2)<-->Node(key = 11,f = 2)<-->Node(key = 13,f = 2)<-->Node(key = 15,f = 2)
                        |
                        |                   indexNode.head                               indexNode.tail
                        |                       |                                            |
indexmap[5]---->indexNode(f = 5)------------Node(key = 8,f = 5)<-->Node(key = 9,f = 5)<-->Node(key = 7,f = 5)
    |
self.tail

# remove:each time remove the self.head.head's node
# put:if the key exist for example put(3,4) we just remove the node from indexNode(f = 1) and then add the node to indexNode(f = 2)'s
# tail and update the indexNode'cnt and the node'f
# if the key doesn't exist for example put(100,100),we just remove the self.head.head's node and put the key in the indexNode(f = 1)'s
# tail
# get:get(4) we just remove the node(key = 4,f = 1) from the indexNode(f = 1) and add the node(key = 4,f = 1) to the indexNode(f = 2)'s
# tail and update the indexNode(f = 1)'s cnt and indexNode(f = 2)'s cnt and update node(key = 4,f= 1) to node(key = 4,f = 2)
"""

class Node(object):
    def __init__(self, key, value):
        """
        Node is the base element which present the key and value. and Node will be appended to the indexNode's tail
        f means the node's referenced frequency
        :param key: key
        :param value: value
        """
        self.value = value
        self.pre = None
        self.next = None
        self.key = key
        self.f = 1

# todo  too weird this problem ... amazing
class indexNode(object):
    def __init__(self, f):
        """
        many indexNode will form a double-linked {indexNode list}
        f means the node in the double-linked {Node list} are same
        each indexNode will be appended by a Node list！
        :param f:
        """
        self.f = f
        self.pre = None
        self.next = None
        self.cnt = 0
        self.head = None
        self.tail = None

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cnt = 0
        self.keymap = {}
        # each time we replace one element form the LFU, we just need to delete the first indexNode's head
        # self.head reprensents the first indexNode which means the lowest frequency indexNode
        self.head = None
        # self.tail reprensents the last indexNode which means the highest frequency indexNode
        self.tail = None
        self.indexmap = {}

    def addindexnode(self, f):
        """
        just add a f frequency to the indexNode list
        :param f: frequency
        :return: void
        """
        node = indexNode(f)
        self.indexmap[f] = node

        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            return

        if f < self.head.f:
            self.head.pre = node
            node.next = self.head
            self.head = node
        else:
            # each time we add a new indexNode to the double-linked indexNode list
            # we assume the indexNode before this one has the frequency f-1
            inode = self.indexmap[f - 1]
            if inode.next:
                tmp = inode.next
                node.next = tmp
                tmp.pre = node
                inode.next = node
                node.pre = inode
            else:
                inode.next = node
                node.pre = inode
                self.tail = node

    def removeindexnode(self, f):
        """
        when the indexNode's cnt == 0 , we need to remove the indexNode so that to make sure the first indexNode
        always has the lowest frequency.
        :param f: int  remove the indexNode which has the frequency f
        :return:void
        """
        indexnode = self.indexmap[f]
        # delete the f in indexmap.
        del self.indexmap[f]
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == indexnode:
            self.head = self.head.next
            self.head.pre = None
        elif self.tail == indexnode:
            self.tail = self.tail.pre
            self.tail.next = None
        else:
            tmp = indexnode.pre
            tmp.next = indexnode.next
            tmp.next.pre = tmp
        del indexnode



    def removenode(self):
        """
        when the cnt equals the capacity, if add a new key to the LFUCache
        we need to remove the first indexNode's first Node
        at the same time we will return a int f, this f will be used in lazy delete because
        when we addindexNode we will need the f-1's indexNode, so after we addindexNode, then
        we can use the f to adjustIndexNode
        :return: int if the return value is -1, don't need to remove the f indexNode else remove the f indexNode
        """
        if not self.head:
            return  -1
        else:
            indexnode = self.head
            node = indexnode.head
            indexnode.cnt -= 1
            if node.next:
                indexnode.head = indexnode.head.next
                indexnode.head.pre = None
                del self.keymap[node.key]
                del node
                return -1
            else:
                f = node.f
                indexnode.head = None
                indexnode.tail = None
                del self.keymap[node.key]
                del node
                return f

    def adjustIndexNode(self,f):
        """
        delete the f indexNode if the indexnode's cnt == 0
        :param f:
        :return: void
        """
        if not self.indexmap.has_key(f):
            return
        inode = self.indexmap[f]
        if inode.cnt == 0:
            self.removeindexnode(f)

    def leave(self, node):
        """
        remove the node from the node.f indexNode if the indexNode's cnt becomes 0 after the node's leave,
        we will delete the indexNode in adjustindexnode(f)
        :param node:
        :return: f  #f represent the f indexNode will be adjust 
        """
        f = node.f
        node.f += 1
        indexnode = self.indexmap[f]
        indexnode.cnt -= 1
        if indexnode.head == indexnode.tail:
            indexnode.head = None
            indexnode.tail = None
        elif indexnode.head == node:
            indexnode.head = indexnode.head.next
            indexnode.head.pre = None
        elif indexnode.tail == node:
            indexnode.tail = indexnode.tail.pre
            indexnode.tail.next = None
        else:
            tmpnode = node.pre
            tmpnode.next = node.next
            tmpnode.next.pre = tmpnode
        return f



    def forward(self, node):
        """
        according the node.f to move the node to the node.f indexNode, if there is no node.f indexNode
        then addindexnode(f)
        :param node: the node to be forwarded
        :return: void
        """
        f = node.f
        if not self.indexmap.has_key(f):
            self.addindexnode(f)
        indexnode = self.indexmap[f]
        indexnode.cnt += 1
        if not indexnode.head and not indexnode.tail:
            indexnode.head = node
            indexnode.tail = node
        else:
            indexnode.tail.next = node
            node.pre = indexnode.tail
            indexnode.tail = node

    def add(self, node):
        """
        if cnt < capacity then just forward the node else remove an node to
        keep the capacity then after forward the f indexNode we can lazy
        delete the f indexnode
        :param node: the new node to be added
        :return:void
        """
        if self.cnt < self.capacity:
            self.cnt += 1
            self.forward(node)
        else:
            f = self.removenode()
            self.forward(node)
            if f != -1:
                self.adjustIndexNode(f)

    def get(self, key):
        """
        each time we add the key node's f by 1 and forward the node and adjustIndexNode
        :type key: int
        :rtype: int
        """
        if self.capacity == 0:
            return -1
        if not self.keymap.has_key(key):
            return -1
        node = self.keymap[key]
        tmpf = self.leave(node)
        self.forward(node)
        self.adjustIndexNode(tmpf)
        return node.value

    def put(self, key, value):
        """
        if the key has existed for a while then we just leave the node from the f indexNode and
        forward the node to the f+1 indexNode else we add a new node to the LFUCache, if there is
        a need, we shuld remove the first indexNode's first node
        :param key:
        :param value:
        :return: void
        """
        if self.capacity == 0:
            return -1
        if self.keymap.has_key(key):
            node = self.keymap[key]
            node.value = value
            f = self.leave(node)
            self.forward(node)
            self.adjustIndexNode(f)
        else:
            node = Node(key, value)
            self.keymap[key] = node
            self.add(node)

# hh = LFUCache(10)
# hh.put(1,1)
# hh.put(2,2)
# hh.get(1)
# hh.put(3,3)
# hh.get(2)
# hh.get(3)
# hh.put(4,4)
# hh.put(1,1)
# hh.put(2,2)
# hh.get(1)
# hh.put(3,3)
# hh.get(2)
# hh.get(3)
# hh.put(9,4)
# hh.put(10,1)
# hh.put(12,2)
# hh.get(1)
# hh.put(33,3)
# hh.get(2)
# hh.get(3)
# hh.put(54,4)
# hh.put(313,4)
# hh.put(230,1)
# hh.put(4322,2)
hh = LFUCache(10)
a = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
b = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
for i in range(0,len(a)):
    if i == 46:
        print('as')
    if a[i] == 'put':
        stm = "hh.%s(%s,%s)" % (a[i], b[i][0],b[i][1])
        if b[i][0] == 7:
            print('fuck')
    else:
        stm = "hh.%s(%s)" % (a[i], b[i][0])
    print(stm,i)
    exec(stm)

print(hh.get(4))
