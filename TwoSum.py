'''
Leetcode Solution-1 TWO SUM
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                total = nums[i] + nums[j]
                if total == target:
                    return[i,j]
        # res = [seq for seq in combinations(nums,2) if sum(seq) == target]
        # for i,j in res:
        #     return[nums.index(i),nums.index(j)]