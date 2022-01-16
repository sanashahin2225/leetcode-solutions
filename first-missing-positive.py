class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minN = min(nums)
        maxN = max(nums)
        if minN > 1 or maxN < 1:
            return 1
        else:
            nums = list(set([n for n in nums if n > 0]))
            if maxN == len(nums):
                return maxN+1
            else:
                return min(list(set([n for n in range(1, len(nums)+1)]) - set(nums)))
