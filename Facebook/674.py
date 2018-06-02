class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        length = 1
        
        best = 1
        
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                length += 1
            else:
                length = 1
            best = max(length,best)
            
        return best
        
