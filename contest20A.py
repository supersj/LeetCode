class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        small = "abcdefghijklmnopqrstuvwxyz"
        big = 'QWERTYUIOPASDFGHJKLZXCVBNM'

        if len(word) <= 1:
            return True
        if word[0] in small:
            for i in range(1,len(word)):
                if word[i] not in small:
                    return False
            return True
        if word[0] in big and word[1] in big:
            for i in range(2,len(word)):
                if word[i] not in big:
                    return False
            return True
        if word[0] in big and word[1] in small:
            for i in range(2, len(word)):
                if word[i] not in small:
                    return False
            return True

