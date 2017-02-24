# todo  run twice give a window 2 * 1/3 from left to right  Fuck
class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        cnt1,cnt2,cd1,cd2 = 0,0,0,1
        for n in nums:
            if n == cd1:
                cnt1 += 1
            elif n == cd2:
                cnt2 += 1
            elif cnt1 == 0:
                cd1,cnt1 = n,1
            elif cnt2 == 0:
                cd2, cnt2 = n,1
            else:
                cnt1,cnt2 = cnt1 - 1,cnt2 - 1
        return [n for n in (cd1,cd2) if nums.count(n) > len(nums) // 3]