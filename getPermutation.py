

def nextPermutation(numbers):
    left= 0
    right= 0
    for i in range(len(numbers)-1,0,-1):
        if numbers[i-1] < numbers[i]:
            left = i-1
            break
    for i in range(len(numbers)-1,left,-1):
        if numbers[i] > numbers[left]:
            right = i
            break
    numbers[left],numbers[right] = numbers[right],numbers[left]
    numbers[left+1:] = numbers[-1:left:-1]
def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    numbers = [i+1 for i in range(n)]
    for i in range(k-1):
        nextPermutation(numbers)
    strings = [chr(e+ord('0')) for e in numbers]
    return ''.join(strings)
a = getPermutation(9,273815)
print(a)