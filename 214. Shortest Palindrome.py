class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def makeNext(p):
            q = 0
            k = 0
            m = len(p)
            next = [0 for i in range(m)]
            for q in range(1, m):
                while k > 0 and p[q] != p[k]:
                    k = next[k - 1]
                if p[q] == p[k]:
                    k += 1
                next[q] = k
            return next[m-1]
        tmp = s + '#' + s[::-1]
        index = makeNext(tmp)
        result = s[index:][::-1]+s
        return result
hh = Solution()
s = "a"
hh.shortestPalindrome(s)
