class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        innode = {}
        graph = {}
        result = []
        for i in range(numCourses):
            graph[i] = []
            innode[i] = 0
        for ele in prerequisites:
            graph[ele[1]].append(ele[0])
            innode[ele[0]] += 1
        while innode:
            haszero = 0
            for k,v in innode.items():
                if v == 0:
                    haszero = 1
                    result.append(k)
                    for ele in graph[k]:
                        innode[ele] -= 1
                    del innode[k]
                    del graph[k]
                    break
            if haszero == 0:
                return []
        if graph:
            return []
        return result
hh = Solution()
co = [[1,0]]
hh.canFinish(2,co)