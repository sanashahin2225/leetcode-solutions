class Solution:
    def trailingZeroes(self, n: int) -> int:
        if(n < 0):
            return -1
 
        # Initialize result
        count = 0

        # Keep dividing n by
        # 5 & update Count
        while(n >= 5):
            n //= 5
            count += n

        return count
