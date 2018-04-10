class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hm = {}
        
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[target - nums[i]] = i
            else:
                return [hm[nums[i]],i]
        return []
        
