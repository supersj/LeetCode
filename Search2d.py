def searchMatrix( matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m = len(matrix)
    n = 0
    if m > 0:
        n = len(matrix[0])
    mu = 0
    md = m - 1
    mid = 0
    while mu <= md:
        mid = (mu + md) // 2
        if target >= matrix[mid][0] and target <= matrix[mid][n - 1]:
            break
        elif target < matrix[mid][0]:
            md = mid - 1
        else:
            mu = mid + 1
    if md < 0 or mu >= m:
        return False
    nl = 0
    nr = n - 1
    while nl <= nr:
        nmid = (nl + nr) // 2
        if matrix[mid][nmid] == target:
            return True
        elif matrix[mid][nmid] > target:
            nr = nmid - 1
        else:
            nl = nmid + 1
    return False

matrix = [[1],[3]]
searchMatrix(matrix,2)