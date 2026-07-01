class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0, 1]
        for _ in range (n):
            memo.append(memo.pop(0) + memo[-1])
        return memo[-1]