from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        stack = []
        s = [e for e in secret]
        g = [g for g in guess]
        tmps = Counter()
        tmpg = Counter()
        for i in range(len(s)):
            if s[i] == g[i]:
                A += 1
                stack.append(i)
            else:
                tmps[s[i]] += 1
                tmpg[g[i]] += 1
        B = 0
        for e in tmps:
            B += min(tmps[e],tmpg[e])
        return int(A)+'A'+int(B)+'B'
