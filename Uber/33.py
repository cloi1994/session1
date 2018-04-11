class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            
            mid = i + (j - i) // 2
            
            if nums[mid] == target:
                return mid
            #case 1:
            # 4 5 6 7 0 1 2
            if nums[mid] > nums[j]:
                if target < nums[mid] and target >= nums[i]:
                    j -= 1
                else:
                    i += 1
            #case 2:
            # 6 7 0 1 2 4 5
            else:
                if target > nums[mid] and target <= nums[j]:
                    i += 1
                else:
                    j -= 1
        return -1
