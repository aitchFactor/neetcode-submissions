class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = [0, 1]
        # for _ in range (n):
        #     memo.append(memo.pop(0) + memo[-1])
        # return memo[-1]

        return fib(n+1)

    
def fib(k2):
    if k2 == 0:
        return 0
    if k2 == 1:
        return 1 
    if k2 == 2:
        return 1
    k = k2 // 2
    if k2 % 2:
        return fib(k)**2 + fib(k+1)**2
    else:
        return fib(k) * (2*fib(k+1) - fib(k))