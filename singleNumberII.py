class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dic = dict()
        
        for i in nums:
            if i in dic.keys():
                dic[i] = dic[i]+1
            else:
                dic[i] = 1
            
        for i,j in dic.items():
            if j == 1:
                return i
