class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        innode = {}
        graph = {}
        haszero = 0
        for i in range(numCourses):
            graph[i] = []
            innode[i] = 0
        for ele in prerequisites:
            graph[ele[0]].append(ele[1])
            innode[ele[1]] += 1
        while innode:
            haszero = 0
            for k,v in innode.items():
                if v == 0:
                    haszero = 1
                    for ele in graph[k]:
                        innode[ele] -= 1
                    del innode[k]
                    del graph[k]
                    break
            if haszero == 0:
                return False
        if graph:
            return False
        return True
