class Solution(object):

    #Solution 1
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        curNoneZero = 0
        
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[curNoneZero] = nums[cur]
                curNoneZero += 1
                
        for i in range(curNoneZero,len(nums)):
            nums[i] = 0


    #Solution 2
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        curNoneZero = 0
        
        for cur in range(len(nums)):
            print curNoneZero , cur
            if nums[cur] != 0:
                nums[curNoneZero] , nums[cur] =  nums[cur] , nums[curNoneZero]
                curNoneZero += 1
            
