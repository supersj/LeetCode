class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        def same(left, right):
            l = set(left)
            r = set(right)
            return len(l.intersection(r)) != 0
        lmax = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if same(words[i], words[j]):
                    continue
                tmp = len(words[i])*len(words[j])
                if tmp <= lmax:
                    break
                else:
                    lmax = tmp
        return lmax
hh = Solution()
n = ["a","ab","abc","d","cd","bcd","abcd"]
print(hh.maxProduct(n))