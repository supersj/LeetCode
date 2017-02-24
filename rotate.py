
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    sumEnd = len(matrix)-1
    for i in range(len(matrix)//2):
        for j in range(i,sumEnd-i):
            a = matrix[i][j]
            matrix[i][j] = matrix[sumEnd-j][i]
            matrix[sumEnd-j][i] = matrix[sumEnd-i][sumEnd-j]
            matrix[sumEnd-i][sumEnd-j] = matrix[j][sumEnd-i]
            matrix[j][sumEnd-i] = a
def generateMatrix(n):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    matrix = [[0 for x in range(n)] for y in range(n)]
    sumEnd = n-1
    order = 1
    for i in range(n//2):
        for j in range(i,sumEnd-i):
            matrix[i][j] = order
            order+=1
        for j in range(i, sumEnd - i):
            matrix[j][sumEnd-i] = order
            order += 1
        for j in range(i, sumEnd - i):
            matrix[sumEnd-i][sumEnd - j] = order
            order += 1
        for j in range(i, sumEnd - i):
            matrix[sumEnd - j][i] = order
            order += 1
    if n%2 == 1:
        matrix[n//2][n//2] = order
    return matrix


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    rows = len(matrix)
    columns = len(matrix[0])
    rowEnd = rows -1
    columnEnd = columns -1
    length = min(rows,columns)
    result = []
    for i in range(length // 2):
        for j in range(i, columnEnd - i):
            result.append(matrix[i][j])
        for j in range(i, rowEnd - i):
            result.append(matrix[j][columnEnd - i])
        for j in range(i, columnEnd - i):
            result.append(matrix[rowEnd - i][columnEnd - j])
        for j in range(i, rowEnd - i):
            result.append(matrix[rowEnd - j][i])
    if length % 2 == 1:
        if rows > columns:
            for i in range(length//2,rowEnd-length//2+1):
                result.append(matrix[i][columns//2])
        else:
            for i in range(length//2,columnEnd-length//2+1):
                result.append(matrix[rows//2][i])
    return result

matrix = [[2,5],[8,4],[0,-1]]

print(spiralOrder(matrix))



print(generateMatrix(3))
# print(matrix)