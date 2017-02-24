# from collections import defaultdict
import random
class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.map = {}
    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.list.append(val)
        if val in self.map.keys():
            self.map[val] += 1
            return False
        self.map[val] = 1
        return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map.keys():
            self.map[val] -= 1
            if self.map[val] == 0:
                del self.map[val]
            self.list.remove(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        index = random.randint(0,len(self.list))
        return self.list[index]


        # Your RandomizedCollection object will be instantiated and called as such:
        # obj = RandomizedCollection()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()