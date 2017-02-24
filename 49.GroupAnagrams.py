class Solution(object):
    # prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    # def primeKey(self,str):
    #     primekey = 1;
    #     for ch in str:
    #         primekey *= self.prime[ord(ch) - ord('a')]
    #     return primekey
    # def strsSort(self,data):
    #     count = [0]*26
    #     for i in range(len(data)):
    #         count[ord(data[i]) - ord('a')] += 1
    #     result = ""
    #     for i in range(0,26):
    #         for j in range(0,count[i]):
    #             result+=chr(ord('a')+i)
    #     return result

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashtable = {}
        for ele in strs:
            key = ''.join(sorted(ele))
            if hashtable.has_key(key):
                hashtable[key].append(ele)
            else:
                hashtable[key] = [ele]
        return hashtable.values()
