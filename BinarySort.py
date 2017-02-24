class Binary(object):
    def __init__(self,nums):
        self.nums = nums

    def search(self,key):
        start = 0
        end = len(self.nums)-1
        while start <= end:
            mid = (start + end) // 2
            if self.nums[mid] == key:
                print("Found it")
                return True
            elif self.nums[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
        print("Not Found")
        return False

    def findUniqueIndex(self,key):
        """
        :rtype if find return index if not return -1
        """
        start = 0
        end = len(self.nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.nums[mid] == key:
                print(mid)
                return mid
            elif self.nums[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
        print(-1)
        return -1

    def findRightIndex(self,key):
        """
        :rtype if find return index if not return -1
        """
        start = 0
        end = len(self.nums) #be careful
        while start < end:
            mid = (start + end) // 2
            if self.nums[mid] <= key:
                start = mid+1
            else:
                end = mid
        if self.nums[start - 1] == key:
            print(start-1)
            return start - 1
        print(-1)
        return -1

    def findInsertRightIndex(self,key):
        """
        :rtype if find return index if not return -1
        """
        start = 0
        end = len(self.nums) #be careful
        while start < end:
            mid = (start + end) // 2
            if self.nums[mid] <= key:
                start = mid+1
            else:
                end = mid
        print(start)
        return start

    def findInsertLeftIndex(self,key):
        """
        :rtype if find return index if not return -1
        """
        start = 0
        end = len(self.nums) #be careful
        while start < end:
            mid = (start + end) // 2
            if self.nums[mid] < key:
                start = mid+1
            else:
                end = mid
        print(start)
        return start

    def insertLeft(self,key):
        start = 0
        end = len(self.nums)  # be careful
        while start < end:
            mid = (start + end) // 2
            if self.nums[mid] < key:
                start = mid + 1
            else:
                end = mid
        self.nums.insert(start,key)

    def insertRight(self,key):
        start = 0
        end = len(self.nums)  # be careful
        while start < end:
            mid = (start + end) // 2
            if self.nums[mid] <= key:
                start = mid + 1
            else:
                end = mid
        self.nums.insert(start,key)

nums = [1,2,2,3,4]
hh = Binary(nums)
hh.search(5)
hh.findUniqueIndex(3)
hh.findInsertLeftIndex(2)