class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 1
        l = num 
        ans = 0
        while s <= l:
            mid = s + (l - s) // 2
            square = mid * mid
            if (square > num):
                l = mid - 1
            else:
                ans = mid
                s = mid + 1
        if ans * ans == num:
            return True
        else:
            return False
