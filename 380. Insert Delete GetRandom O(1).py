import random
class RandomizedSet1(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myset = set()
        self.list = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.myset:
            return False
        self.myset.add(val)
        self.list.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.myset:
            self.myset.remove(val)
            self.list.remove(val)
            return True
        return False
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        nlen = len(self.myset)
        index = random.randint(0,nlen-1)
        return self.list[index]

class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myset = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.myset.keys():
            return False
        self.myset[val] = 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.myset.keys():
            del self.myset[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        nlen = len(self.myset)
        index = random.randint(0, nlen - 1)
        keys = list(self.myset.keys())
        return keys[index]




                # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()