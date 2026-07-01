class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [None for _ in range(m*n)]
        res[0] = 1
        for i in range(m):
            for j in range(n):
                if (i, j) == (0, 0):
                    continue
                num = 0
                if i > 0:
                    num += res[n*(i-1) + j]
                if j > 0:
                    num += res[n*i + j-1]
                res[n*i + j] = num
        return res[-1]

