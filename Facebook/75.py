class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        right = len(nums) - 1
        
        
        left = 0
        
        
        while i <= right:
            if nums[i] == 2:
                nums[i] , nums[right] = nums[right] , nums[i]
                right -= 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[left] , nums[i] = nums[i] , nums[left]
                i += 1
                left += 1
