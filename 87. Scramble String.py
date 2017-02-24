# class Solution(object):
#     def isScramble(self, s1, s2):
#         if s1 == s2: return True
#         if sorted(s1) != sorted(s2): return False
#         index = -1
#         order = 1
#         for i in xrange(1, len(s1)):
#             if sorted(s1[:i]) == sorted(s2[:i]) and sorted(s1[i:]) == sorted(s2[i:]):
#                 index = i
#                 order = 1
#                 break
#             if sorted(s1[:i]) == sorted(s2[-i:]) and sorted(s1[i:]) == sorted(s2[:-i]):
#                 index = i
#                 order = 0
#                 break
#         if index == -1:
#             return False
#         if order == 1:
#             return self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])
#         else:
#             return self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])
class Solution:
# @return a boolean
    def isScramble(self, s1, s2):
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False