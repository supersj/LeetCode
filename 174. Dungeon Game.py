# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
#
# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
#
# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
#
#
# Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
#
# For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
#
# -2 (K)	-3	3
# -5	-10	1
# 10	30	-5 (P)
#
# Notes:
#
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
import sys
# todo  interesting wrong solution
class Solution(object):
    def calculateMinimumHP1(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = 0
        if m > 0:
            n = len(dungeon[0])

        table = [0 for i in range(n)]
        result = [0 for i in range(n)]
        table[0] = dungeon[0][0]
        result[0] = dungeon[0][0]
        for i in range(1,n):
            table[i] = table[i-1] + dungeon[0][i]
            result[i] = min(result[i-1],table[i])
        for row in range(1,m):
            table[0] = table[0] + dungeon[row][0]
            result[0] = min(result[0],table[0])
            for i in range(1,n):
                if result[i] > result[i-1]:
                    result[i] = result[i]
                    table[i] = table[i] + dungeon[row][i]
                    result[i] = min(result[i], table[i])
                else:
                    result[i] = result[i-1]
                    table[i] = table[i-1] + dungeon[row][i]
                    result[i] = min(result[i], table[i])
        if result[n-1] > 0:
            return 1
        else:
            return 1-result[n-1]
# """
# int calculateMinimumHP(vector<vector<int> > &dungeon) {
#
#     if(dungeon.size()==0) return 0;
#
#     int row=dungeon.size();
#     int col=dungeon[0].size();
#
#     for(int i=row-1; i>=0; i--) {
#
#         for(int j=col-1; j>=0; j--) {
#
#             if(i==row-1 && j==col-1) dungeon[i][j]=max(1, 1-dungeon[i][j]);
#             else if(i==row-1) dungeon[i][j]=max(1, dungeon[i][j+1]-dungeon[i][j]);
#             else if(j==col-1) dungeon[i][j]=max(1, dungeon[i+1][j]-dungeon[i][j]);
#             else dungeon[i][j]=max(1, min(dungeon[i+1][j], dungeon[i][j+1])-dungeon[i][j]);
#         }
#     }
#
#     return dungeon[0][0];
# }
# """
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row = len(dungeon)
        col = 0
        if row > 0:
            col = len(dungeon[0])
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if i == row - 1 and j == col - 1:
                    dungeon[i][j]=max(1, 1-dungeon[i][j])
                elif i == row-1:
                    dungeon[i][j]=max(1, dungeon[i][j+1]-dungeon[i][j])
                elif j == col - 1:
                    dungeon[i][j]=max(1, dungeon[i+1][j]-dungeon[i][j])
                else:
                    dungeon[i][j]=max(1, min(dungeon[i+1][j], dungeon[i][j+1])-dungeon[i][j])
        return dungeon[0][0]


hh = Solution()
dungeon = [[1,-2,3],[2,-2,-2]]
print(hh.calculateMinimumHP(dungeon))