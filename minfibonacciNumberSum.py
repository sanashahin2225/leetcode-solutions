class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        def binarySearch(dp,k):
            start = 0
            end = len(dp)-1
            
            while start <= end:
                mid = start+(end-start)//2
                
                if dp[mid] == k:
                    return k
                elif dp[mid] > k:
                    end = mid-1
                else:
                    start = mid+1
            return dp[end]
                    
        dp = [0,1]
        if k == 1:
            return 1
        ans = 0
        i = 2
        while ans < k:
            ans = dp[i-1]+dp[i-2]
            i += 1
            dp.append(ans)
            
        count = 0
        while k != 0:
            floor = binarySearch(dp,k)
            count += 1
            k -= floor
        return count
