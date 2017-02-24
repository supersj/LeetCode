def uniquePathsWithObstacles(obstacleGrid):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    n = 1
    m = len(obstacleGrid)
    if m >= 1:
        n = len(obstacleGrid[0])
    result = [[1 for i in range(n)] for j in range(m)]

    for i in range(m):
        if obstacleGrid[i][0] == 1:
            for j in range(i, m):
                result[j][0] = 0
            break

    for j in range(n):
        if obstacleGrid[0][j] == 1:
            for i in range(j, n):
                result[0][i] = 0
            break

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1 or obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] == 1:
                result[i][j] = 0
            else:
                result[i][j] = result[i - 1][j] + result[i][j - 1]
    return result[m - 1][n - 1]
a = [[1]]
print(uniquePathsWithObstacles(a))