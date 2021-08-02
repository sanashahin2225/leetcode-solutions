class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        if len(nums) != 0 and val != None:
            for i in range(len(nums)):
                if nums[i] == val:
                    nums[i] = '_'
                    count += 1
                else:
                    nums[i-count] = nums[i]
                    
            actual_length = len(nums) - count
            
            return actual_length
        else:
            return 0
