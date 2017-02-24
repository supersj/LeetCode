class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        hashmap = {}
        start = 0
        str = str.split()
        if len(str) != len(pattern):
            return False
        for ele in str:
            if ele in hashmap.keys():
                if pattern[start] != hashmap[ele]:
                    return False
            else:
                if pattern[start] not in pattern[:start]:
                    hashmap[ele] = pattern[start]
                else:
                    return False
            start += 1
        return True
hh = Solution()
p = "abba"
s = "dog cat cat fish"
hh.wordPattern(p,s)