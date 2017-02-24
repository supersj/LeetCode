# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def flatten(nestedList):
            result = []
            for n in nestedList:
                if n.isInteger():
                    result.append(n.getInteger())
                else:
                    result.extend(flatten(n.getList()))
            return result
        self.result = flatten(nestedList)
        self.end = len(self.result)
        self.start = 0


    def next(self):
        """
        :rtype: int
        """
        tmp = self.result[self.start]
        self.start += 1
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.start < self.end

        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())