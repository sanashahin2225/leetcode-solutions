class Solution:
    def mySqrt(self, x: int) -> int:
        
        def sqrtSearch(low, high, N):
            if (low <= high) :
                mid = (low + high) // 2
                if ((mid * mid <= N) and ((mid + 1) * (mid + 1) > N)):
                    return mid
                elif (mid * mid < N):
                    return sqrtSearch(mid + 1, high, N)
                else:
                    return sqrtSearch(low, mid - 1, N)
            
            return low
        
        output = sqrtSearch(0,x,x)
        return output
