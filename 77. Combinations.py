# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Subscribe to see which companies asked this question
#
# Show Tags
# Show Similar Problems
# class Solution(object):
#
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#
#
result = []
def combinehelp(start, n, k,tmp):
    if k == 0:
        result.append(tmp[:])
        return
    for i in range(start,n - k + 2):
        tmp.append(i)
        combinehelp(i+1, n, k-1,tmp)
        tmp.remove(i)
tmp = []
print(combinehelp(1,1,1,tmp))
print(result)

def combine(self, n, k):
    ans = []
    stack = []
    x = 1
    while True:
        l = len(stack)
        if l == k:
            ans.append(stack[:])
        if l == k or x > n - k + l + 1:
            if not stack:
                return ans
            x = stack.pop() + 1
        else:
            stack.append(x)
            x += 1

# 26 / 26 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# 98.51%