class Solution(object):
    def reversePairs(self, A):
        def mergeSort(tmp, A, l, r):
            if l >= r:
                return 0
            m = (l + r) >> 1
            ans = mergeSort(tmp,A, l, m) + mergeSort(tmp,A, m + 1, r)
            i, j, k = l, m + 1, l
            _i, _j, _k = i, j, k
            while _j <= r:
                while _i <= m:
                    if A[_i] <= 2 * A[_j]:
                        _i += 1
                    else:
                        break
                ans += m - _i + 1
                if _i > m:
                    break
                _j += 1
            while i <= m and j <= r:
                if A[i] > A[j]:
                    tmp[k] = A[j]
                    j += 1
                else:
                    tmp[k] = A[i]
                    i += 1
                k += 1
            while i <= m:
                tmp[k] = A[i]
                k += 1
                i += 1
            while j <= r:
                tmp[k] = A[j]
                k += 1
                j += 1
            for i in range(l, r + 1):
                A[i] = tmp[i]
            return ans
        tmp = [0] * len(A)
        return mergeSort(tmp,A, 0, len(A) - 1)


hh = Solution()
A = [3,1,1]
print(hh.reversePairs(A))