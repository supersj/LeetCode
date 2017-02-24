# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
#
# Subscribe to see which companies asked this question

#TODO  DP

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # def wordBreakHelp(s,start,end,wordSet):
        #     if start == end:
        #         return True
        #     for i in range(start+1,end+1):
        #         if s[start:i] in wordSet:
        #             wordSet.discard(s[start:i])
        #             if wordBreakHelp(s,i,end,wordSet):
        #                 return True
        #             wordSet.add(s[start:i])
        #     return False
        # wordSet = set(wordDict)
        # return wordBreakHelp(s,0,len(s),wordSet)
        f = [False for i in range(len(s)+1)]
        f[0] = True
        wordSet = set(wordDict)
        for i in range(1,len(s)):
            for j in range(i):
                if f[j] and s[j:i] in wordSet:
                    f[i] = True
                    break
        return f[len(s)]
