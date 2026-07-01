class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        res = []
        for skip in range (3):
            a, b, c = 0, 0, 0
            for i in range(skip + 1, skip + len(nums)):
                money = nums[i%len(nums)]
                a, b, c = b, c, max(a, b) + money
            res.append(max(a, b, c))
        print(res)
        return max(res)