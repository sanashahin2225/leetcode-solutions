class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        dup = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target = - (nums[i] + nums[j])
                if target in dup:
                    res.add((nums[i],nums[j],target))
            dup.add(nums[i])
        return list(res)
