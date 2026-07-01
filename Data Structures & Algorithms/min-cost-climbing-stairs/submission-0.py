class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0, 0]
        for c in cost + [0]:
            memo.append(min(memo.pop(0), memo[-1]) + c)
            # print (memo, "cost", c)
        return memo[-1]