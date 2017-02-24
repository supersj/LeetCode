from collections import Counter
from bisect import *
class Solution(object):

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s):
            if not s:
                return ""
            lnum = Counter()
            for l in s:
                lnum[l] += 1
            tmp = []
            hashmap = {}
            indexs = []
            for i in range(len(s)):
                if lnum[s[i]] == 1:
                    tmp.append(s[i])
                    indexs.append(i)
                if s[i] in hashmap.keys():
                    hashmap[s[i]].append(i)
                else:
                    hashmap[s[i]] = [i]
            keys = sorted(hashmap.keys())
            if not tmp:
                tmp.append(keys[0])
                indexs.append(hashmap[keys[0]][0])
                hashmap[keys[0]] = [hashmap[keys[0]][0]]
            for k in keys:
                if len(hashmap[k]) == 1:
                    continue
                for i in range(len(hashmap[k])):
                    tmpindex = bisect_left(indexs,hashmap[k][i])
                    if tmpindex == len(tmp):
                        tmp.append(k)
                        indexs.insert(tmpindex,hashmap[k][i])
                        break
                    if k < tmp[tmpindex]:
                        tmp.insert(tmpindex,k)
                        indexs.insert(tmpindex, hashmap[k][i])
                        break
                    if i == len(hashmap[k]) - 1:
                        tmp.insert(tmpindex,k)
                        indexs.insert(tmpindex,hashmap[k][i])
            result = ''.join(tmp)
            return result
        t = reversed(s)
        a = list(t)
        t = ''.join(a)
        rs = helper(s)
        rt = helper(t)
        if rs < rt:
            return rs
        r = list(reversed(rt))
        return ''.join(r)
def removeDuplicateLetters(self, s):
    result = ''
    while s:
        i = min(map(s.rindex, set(s)))
        c = min(s[:i+1])
        result += c
        s = s[s.index(c):].replace(c, '')
    return result

hh = Solution()
s = "bccab"
print(hh.removeDuplicateLetters(s))