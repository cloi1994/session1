class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        v = [float('-inf'),float('-inf'),float('-inf')]
        
        
        for i in range(len(nums)):
            if nums[i] not in v:
                if nums[i] > v[0]:
                    v[2] = v[1]
                    v[1] = v[0]
                    v[0] = nums[i]

                elif nums[i] > v[1]:
                    v[2] = v[1]
                    v[1] = nums[i]

                elif nums[i] > v[2]:
                    v[2] = nums[i]
        
        if v[2] !=  float('-inf'):
            return v[2]
        else:
            return v[0]
        
