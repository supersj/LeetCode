# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.
#
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
#
# Subscribe to see which companies asked this question

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
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
        def DFS(s,wordDict,hashMap):
            if s in hashMap:
                return hashMap[s]
            res = []
            if len(s) == 0:
                res.append("")
                return res
            for word in wordDict:
                if s.startswith(word):
                    sublist = DFS(s[len(word):],wordDict,hashMap)
                    for sub in sublist:
                        res.append(word + ("" if not sub else " ") + sub)
            hashMap[s] = res
            return res
        hashMap = {}
        return DFS(s,wordDict,hashMap)
hh = Solution()
s = "catsanddog"
words = ["cat","cats","and","sand","dog"]
hh.wordBreak(s,words)