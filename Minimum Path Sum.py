def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    n = 1
    m = len(grid)
    if m >= 1:
        n = len(grid[0])
    if m > 1:
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
    if n > 1:
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += max(grid[i - 1][j] , grid[i][j - 1])

    return grid[m-1][n-1]

