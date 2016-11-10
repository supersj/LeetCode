def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return self.binarySearch(0, len(nums)-1, nums, target)
    
def binarySearch(self, begin, end, nums, target):
    if begin > end:
        return -1
    mid = (begin + end)/2
    if nums[mid] == target:
        return mid
    if nums[mid] < nums[end]: # sorted right half
        if target > nums[mid] and target <= nums[end]:
            return self.binarySearch(mid+1, end, nums, target)
        else:
            return self.binarySearch(begin, mid-1, nums, target)
    else: # sorted left half
        if target < nums[mid] and target >= nums[begin]:
            return self.binarySearch(begin, mid-1, nums, target)
        else:
            return self.binarySearch(mid+1, end, nums, target)