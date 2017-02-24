# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
import string
class Solution(object):
    # TODO wrong solution
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        fronts = [{beginWord},{endWord}]
        levels = [1,1]
        while fronts[0] and fronts[1]:
            if len(fronts[0]) > len(fronts[1]):
                fronts.reverse()
                levels.reverse()
            newLevel = set()
            for word  in fronts[0]:
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        newWord = word[:i] + char + word[i+1:]
                        if newWord in fronts[1]:
                            return levels[0]+levels[1]
                        if newWord in wordList:
                            newLevel.add(newWord)
                            wordList.remove(newWord)
            fronts[0] = newLevel
            levels[0] += 1
        return 0
    # TODO right solution
    def ladderLengthRight(self, beginWord, endWord, wordDict):
        if endWord not in wordDict:
            return 0
        front, back = set([beginWord]), set([endWord])
        length = 2
        width = len(beginWord)
        charSet = list(string.ascii_lowercase)
        wordDict = set(wordDict)
        wordDict.discard(beginWord)
        wordDict.discard(endWord)
        while front:
            newFront = set()
            for phrase in front:
                for i in range(width):
                    for c in charSet:
                        nw = phrase[:i] + c + phrase[i + 1:]
                        if nw in back:
                            return length
                        if nw in wordDict:
                            newFront.add(nw)
            front = newFront
            if len(front) > len(back):
                front, back = back, front
            wordDict -= front
            length += 1
        return 0