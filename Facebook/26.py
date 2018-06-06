class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        s = 0
        
        for j in range(1,len(nums)):
            if nums[s] != nums[j]:
                s += 1
                nums[s] = nums[j]
                
        return s+1
            
