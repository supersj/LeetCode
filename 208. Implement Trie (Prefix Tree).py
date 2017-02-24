class TrieNode(object):
    def __init__(self):
        self.isChild = 0
        self.next = {}


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.TrieNode = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        head = self.TrieNode
        if word == "":
            head.isChild = 1
        for s in word:
            if head.next.has_key(s):
                head = head.next[s]
            else:
                head.next[s] = TrieNode()
                head = head.next[s]
        head.isChild = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        head = self.TrieNode
        if word == "":
            if head.isChild == 1:
                return True
            return False
        for s in word:
            if head.next.has_key(s):
                head = head.next[s]
            else:
                return False
        if head.isChild == 0:
            return False
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        head = self.TrieNode
        for s in prefix:
            if head.next.has_key(s):
                head = head.next[s]
            else:
                return False
        return True
