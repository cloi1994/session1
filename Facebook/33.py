class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # [4,5,6,7,8,1,2]  target = 4
        
        # [7,0,1,2,4,5,6]  
        
        i = 0
        j = len(nums) - 1
        
        
        while i <= j:
            
            mid = i + (j - i) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[j]: #left sorted
                
                if nums[mid] > target and nums[i] <= target:
                    j = mid - 1
                else:
                    i = mid + 1
                
            else: # right sorted
                
                if nums[mid] < target and nums[j] >= target:
                    i = mid + 1
                else:
                    j = mid - 1
                    
        return -1
