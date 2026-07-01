class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b, c = 0, 0, 0
        for money in nums:
            a, b, c = b, c, max(a, b) + money
        
        return max(a, b, c)