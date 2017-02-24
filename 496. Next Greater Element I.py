class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right = []
        result = []
        if not nums:
            return []
        if len(nums) == 1:
            return [-1]
        right.append(nums[-1])
        for i in range(len(nums)-1,-1,-1):
            right.append(max(right[-1],nums[i]))
        right.reverse()
        M = max(nums)
        for i in range(len(nums)):
            if nums[i] == M:
                result.append(-1)
            elif nums[i] < right[i]:
                start = i+1
                while True:
                    if nums[start] > nums[i]:
                        break
                    start += 1
                result.append(nums[start])
            else:
                start = 0
                while True:
                    if nums[start] > nums[i]:
                        break
                    start += 1
                result.append(nums[start])
        print(result)
        return result
hh = Solution()
nums = [1,2,3,4,3]
hh.nextGreaterElements(nums)