# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
#
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.
#
# Subscribe to see which companies asked this question

# LCS problem
# No LCS problem I misunderstand the problem

# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         def LCS(S,n,T,m):
#             result = 0
#             if n == 0 or m == 0:
#                 return 0
#             if S[n-1] == T[m-1]:
#                 result = 1 + LCS(S,n-1,T,m-1)
#             else:
#                 result = max(LCS(S,n-1,T,m),LCS(S,n,T,m-1))
#             return result
#         lens1 = len(s1)
#         lens2 = len(s2)
#         if lens1 == 0 and lens2 == 0:
#             return False
#         if lens1 == LCS(s1,lens1,s3,len(s3)) and lens2 == LCS(s2,lens2,s3,len(s3)):
#             return True
#         return False
#
#

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len3 != len1+len2:
            return False
        table = [[False for i in range(len2+1)] for j in range(len1+1)]
        for i in range(len1+1):
            for j in range(len2+1):
                if i == 0 and j == 0:
                    table[i][j] = True
                elif i == 0:
                    table[i][j] = table[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    table[i][j] = table[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    table[i][j] = (table[i-1][j] and s1[i-1] == s3[i+j-1]) or (table[i][j-1] and s2[j-1] == s3[i+j-1])
        return table[len1][len2]

s1 = "a"
s2 = "b"
s3 = "ab"

hh = Solution()
hh.isInterleave(s1,s2,s3)
"""
If we expand the two strings s1 and s2 into a chessboard, then this problem can be transferred into a path seeking problem from the top-left corner to the bottom-right corner. The key is, each cell (y, x) in the board corresponds to an interval between y-th character in s1 and x-th character in s2. And adjacent cells are connected with like a grid. A BFS can then be efficiently performed to find the path.

Better to illustrate with an example here:

Say s1 = "aab" and s2 = "abc". s3 = "aaabcb". Then the board looks like

o--a--o--b--o--c--o
|     |     |     |
a     a     a     a
|     |     |     |
o--a--o--b--o--c--o
|     |     |     |
a     a     a     a
|     |     |     |
o--a--o--b--o--c--o
|     |     |     |
b     b     b     b
|     |     |     |
o--a--o--b--o--c--o
Each "o" is a cell in the board. We start from the top-left corner, and try to move right or down. If the next char in s3 matches the edge connecting the next cell, then we're able to move. When we hit the bottom-right corner, this means s3 can be represented by interleaving s1 and s2. One possible path for this example is indicated with "x"es below:

x--a--x--b--o--c--o
|     |     |     |
a     a     a     a
|     |     |     |
o--a--x--b--o--c--o
|     |     |     |
a     a     a     a
|     |     |     |
o--a--x--b--x--c--x
|     |     |     |
b     b     b     b
|     |     |     |
o--a--o--b--o--c--x
Note if we concatenate the chars on the edges we went along, it's exactly s3. And we went through all the chars in s1 and s2, in order, exactly once.

Therefore if we view this board as a graph, such path finding problem is trivial with BFS. I use an unordered_map to store the visited nodes, which makes the code look a bit complicated. But a vector should be enough to do the job.

Although the worse case timeis also O(mn), typically it doesn't require us to go through every node to find a path. Therefore it's faster than regular DP than average.

struct MyPoint {
    int y, x;
    bool operator==(const MyPoint &p) const {
        return p.y == y && p.x == x;
    }
};
namespace std {
    template <>
    struct hash<MyPoint> {
        size_t operator () (const MyPoint &f) const {
            return (std::hash<int>()(f.x) << 1) ^ std::hash<int>()(f.y);
        }
    };
}

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size()) return false;

        queue<MyPoint> q;
        unordered_set<MyPoint> visited;
        bool isSuccessful = false;
        int i = 0;

        q.push(MyPoint { 0, 0 });
        q.push(MyPoint { -1, -1 });
        while (!(1 == q.size() && -1 == q.front().x)) {
            auto p = q.front();
            q.pop();
            if (p.y == s1.size() && p.x == s2.size()) {
                return true;
            }
            if (-1 == p.y) {
                q.push(p);
                i++;
                continue;
            }
            if (visited.find(p) != visited.end()) { continue; }
            visited.insert(p);

            if (p.y < s1.size()) { // down
                if (s1[p.y] == s3[i]) { q.push(MyPoint { p.y + 1, p.x }); }
            }
            if (p.x < s2.size()) { // right
                if (s2[p.x] == s3[i]) { q.push(MyPoint { p.y, p.x + 1 }); }
            }
        }
        return false;
    }
};
"""