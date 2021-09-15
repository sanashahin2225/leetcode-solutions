def singleNumber(self, nums: List[int]) -> int:
        
        if nums:
            if len(nums) == 1:
                return nums[0]
            res = [x for x in set(nums) if nums.count(x) == 1]
            return res[0]
