class TrieNode(object):
    def __init__(self):
        self.isChild = 0
        self.next = {}

# TODO awful solution you need to improve it by c++ and by a more concise recursive way
class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.TrieNode = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        head = self.TrieNode
        if word == "":
            head.isChild = 1
        for s in word:
            if s in head.next.keys():
                head = head.next[s]
            else:
                head.next[s] = TrieNode()
                head = head.next[s]
        head.isChild = 1

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def searchHelp(word, start, end, root):
            if start == end:
                for node in root:
                    if word[start] in node.next.keys() and node.next[word[start]].isChild == 1:
                        return True
                return False
            for i in range(start,len(word)):
                s = word[i]
                if s == '.':
                    tmp = []
                    for node in root:
                        for k in node.next:
                            tmp.append(node.next[k])
                    root = tmp
                    if searchHelp(word, start + 1, end, root):
                        return True
                else:
                    tmp = []
                    for node in root:
                        if s in node.next.keys():
                            tmp.append(node.next[s])
                    root = tmp
                    if len(tmp) == 0:
                        return False
                    return searchHelp(word, start + 1, end, root)

        return searchHelp(word, 0, len(word) - 1, [self.TrieNode])

hh = WordDictionary()
hh.addWord("bad")
if hh.search("bads"):
    print("yes")