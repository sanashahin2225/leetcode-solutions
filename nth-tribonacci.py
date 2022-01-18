class Solution:
    def tribonacci(self, n: int) -> int:
        def trib(n,memo={}):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            memo[n] = trib(n-1,memo)+trib(n-2,memo)+trib(n-3,memo)
            return memo[n]
        
        return trib(n)
