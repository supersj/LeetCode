def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    len1 = len(word1)
    len2 = len(word2)
    step = [[0 for i in range(len2+1)] for j in range(len1+1)]
    for i in range(len2+1):
        step[0][i] = i
    for j in range(len1+1):
        step[j][0] = j
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if word2[j-1] == word1[i-1]:
                step[i][j] = step[i-1][j-1]
            else:
                step[i][j] = min(step[i-1][j-1],step[i-1][j],step[i][j-1]) + 1
    return step[len1][len2]

def minDistanceII(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    len1 = len(word1)
    len2 = len(word2)
    step = [j for j in range(len1+1)]
    for j in range(1,len2+1):
        pre = step[0]
        for i in range(1,len1+1):
            temp = step[i]
            if word2[j-1] == word1[i-1]:
                step[j] = pre
            else:
                step[j] = min(step[j-1],pre,step[j]) + 1
            pre = temp
    return step[len1]