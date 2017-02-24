# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = {}
        hashmap = {}
        slen = len(s)
        if slen < 10:
            return []
        for i in range(slen-10+1):
            tmp = s[i:i+10]
            if tmp in hashmap.keys() and tmp not in result.keys() :
                result[s[i:i+10]] = 1
            else:
                hashmap[s[i:i+10]] = 1
        return result.keys()