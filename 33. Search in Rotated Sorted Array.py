class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.searchHelper(nums,0,len(nums)-1,target)

    def searchHelper(self,nums,left,right,target):
        if right < left:
            return -1
        mid = (right + left) //2
        if nums[mid] == target:
            return mid
        if nums[left] <= target < nums[mid]:
            return self.searchHelper(nums,left,mid - 1,target)
        elif nums[mid] < target <= nums[right]:
            return self.searchHelper(nums,mid + 1,right, target)
        elif nums[mid] > nums[right]:
            return self.searchHelper(nums, mid + 1,right,target)
        else:
            return self.searchHelper(nums, left, mid - 1, target)
