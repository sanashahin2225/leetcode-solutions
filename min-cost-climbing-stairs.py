class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return min(cost[0], cost[1])
            
            if n in memo:
                return memo[n]
            
            res = min(cost[n] + dp(n - 1), cost[n - 1] + dp(n - 2))
            memo[n] = res
            
            return res
 
        return dp(len(cost) - 1)
