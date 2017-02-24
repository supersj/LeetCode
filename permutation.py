
def permute(nums,index,length):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # print the result
    if index == length-1:
        for i in range(length):
            print(nums[i],end='')
        print()
    for i in range(index,length):
        nums[index],nums[i] = nums[i],nums[index]
        permute(nums,index+1,length)
        nums[index],nums[i] = nums[i],nums[index]

def isswap(nums,start, end):
    for i in range(start,end):
        if nums[i] == nums[end]:
            return False
    return True

def permuteUnique(nums,index,length):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # print the result
    if index == length-1:
        for i in range(length):
            print(nums[i],end='')
        print()

    for i in range(index,length):
        if isswap(nums,index,i):
            nums[index],nums[i] = nums[i],nums[index]
            permuteUnique(nums,index+1,length)
            nums[index],nums[i] = nums[i],nums[index]

nums = [2,2,1,1]
permuteUnique(nums,0,len(nums))

for i in range(10):
    print(i)
    i+=2
while i < 10:
    i+=2;
    print(i)