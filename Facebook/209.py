class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        i = 0
        j = 0
        
        summ = 0
        
        best = float('inf')
        
        while j < len(nums):
            
            while summ < s and j < len(nums):
                summ += nums[j]
                j += 1

            while summ >= s:
                best = min(best,j-i)
                summ -= nums[i]
                i += 1
        
        if best == float('inf'):
            return 0
        
        return best
            
            
        
