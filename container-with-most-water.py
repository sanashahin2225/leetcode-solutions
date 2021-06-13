class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxm = 0
        ptr_small = 0
        ptr_high = len(height)-1
        while ptr_small < ptr_high:
            min_bar = min(height[ptr_small],height[ptr_high])
            res = (ptr_high - ptr_small) * min_bar
            if maxm < abs(res):
                maxm = abs(res)
            if height[ptr_small] < height[ptr_high]:
                ptr_small += 1
            else:
                ptr_high -= 1
        return maxm
