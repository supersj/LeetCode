import bisect
import scipy
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

# def searchHelp(nums,left,right,target):



def binarySearch(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left =mid
    return -1

def bisecInsertRight(nums,target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    nums.insert(left,target)

def bisecInsertLeft(nums,target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid





class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
        return self.searchHelper(nums,0,len(nums)-1,target)

    def searchHelper(self,nums,left,right,target):
        while left < right:
            if nums[left] == nums[left+1]:
                left += 1
            else:
                break
        while left < right:
            if nums[right] == nums[right-1]:
                right -= 1
            else:
                break
        if right < left:
            if right >= 0 and nums[right] == target:
                return True
            return False
        mid = (right + left) //2
        if nums[mid] == target:
            return True
        if nums[left] <= target < nums[mid]:
            return self.searchHelper(nums,left,mid - 1,target)
        elif nums[mid] < target <= nums[right]:
            return self.searchHelper(nums,mid + 1,right, target)
        elif nums[mid] > nums[right]:
            return self.searchHelper(nums, mid + 1,right,target)
        else:
            return self.searchHelper(nums, left, mid - 1, target)

hh = Solution()
nums = [1,3]
target = 0
print(hh.search(nums,target))