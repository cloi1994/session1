class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        mult = 1
        
        p = [1]
        
        for i in range(1,len(nums)):
            mult *= nums[i-1]
            p.append(mult)
        
        mult = 1
        
        for i in range(len(nums)-2,-1,-1):
            mult *= nums[i+1]
            p[i] *= mult
            
        
        return p
        
