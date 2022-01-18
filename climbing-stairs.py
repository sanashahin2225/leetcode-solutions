class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        memo = [1,2]
        
        for i in range(2,n+1):
            memo.append(memo[i-1]+memo[i-2])
        
        return memo[n-1]
