class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        result = []
        right = []
        if not findNums:
            return []
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        right.append(nums[-1])
        for i in range(len(nums)-2,-1,-1):
            right.append(max(right[-1],nums[i]))
        right.reverse()
        for i in range(len(findNums)):
            _index = hashmap[findNums[i]]
            if nums[_index] >= right[_index]:
                result.append(-1)
            else:
                start = _index + 1
                while True:
                    if nums[start] > nums[_index]:
                        result.append(nums[start])
                        break
                    start += 1
        return result
hh = Solution()
findNums = [4,1,2]
nums = [1,3,4,2]
print(hh.nextGreaterElement(findNums,nums))