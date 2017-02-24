from operator import itemgetter
# todo insert order thinking
class Solution1(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = itemgetter(1,0))
        result = []
        start = 0
        for ele in people:
            if ele[1] == 0:
                result.append(ele)
                start += 1
            else:
                break
        _last = start
        _lastlevel = 0
        for i in range(start,len(people)):
            cnt = people[i][1]
            if cnt != _lastlevel:
                _last = 0
            _lastlevel = cnt
            _index = 0
            for num in result:
                if cnt == 0:
                    break
                if num[0] >= people[i][0]:
                    cnt -= 1
                _index += 1
            _last = max(_last+1,_index)
            result.insert(_last,people[i])
        return result
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x: x[1])
        people.sort(key = lambda x: x[0],reverse= True)
        result = []
        print(people)
        for ele in people:
            result.insert(ele[1],ele)
        return result

p = [[8,2],[4,2],[4,5],[2,0],[7,2],[1,4],[9,1],[3,1],[9,0],[1,0]]
hh = Solution()
hh.reconstructQueue(p)