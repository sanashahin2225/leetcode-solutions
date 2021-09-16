class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return nums[0]
        major = len(nums) // 2 if len(nums) % 2 == 0 else len(nums) // 2 + 1
        res = [x for x in set(nums) if nums.count(x) >= major]
        return res[0] if res else None
