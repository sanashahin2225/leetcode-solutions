class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def BinarySearch(nums, target): 
            first = 0 
            last = len(nums)-1 
            

            while first<=last:        
                midpoint = first + (last - first)//2   
                if (midpoint-1>=0 and nums[midpoint-1] < target and nums[midpoint] > target):
                    return midpoint
                if nums[midpoint] == target:             
                    return midpoint      
                else:             
                    if target < nums[midpoint]:                 
                        last = midpoint-1             
                    else:           
                        first = midpoint+1     
            if target < nums[midpoint]:
                return midpoint
            else:
                return midpoint+1
        if nums:
            return BinarySearch(nums,target)
        else:
            return None
