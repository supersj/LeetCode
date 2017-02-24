class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        def countDigitOneHelp(n, cntzero):
            if n == 1:
                return cntzero * (10 ** (cntzero - 1)) + 1
            else:
                return 10 ** cntzero + n * cntzero * (10 ** (cntzero - 1))
        result = 0
        num = n
        stack = []
        cnt = 0
        while num != 0:
            tmp = num % 10
            if tmp != 0:
                stack.append((tmp,cnt))
            cnt += 1
            num = num // 10
            if tmp == 1:
                result += n % (10 ** (cnt-1))
        for ele in stack:
            result += countDigitOneHelp(ele[0],ele[1])
        return result
hh = Solution()
hh.countDigitOne(28173)