class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if not nums:
            return []
        result = []
        nlen = len(nums)
        start = 0
        while start < nlen:
            left = nums[start]
            right = left
            rightindex = start + 1
            hasright = False
            while rightindex < nlen:
                if nums[rightindex] - right == 1:
                    right = nums[rightindex]
                    rightindex += 1
                    hasright = True
                else:
                    start = rightindex
                    break
            if hasright:
                result.append(str(left) + '->' + str(right))
            else:
                result.append(str(left))
            if rightindex == nlen:
                break
        return result
hh = Solution()
hh.summaryRanges([-1])
