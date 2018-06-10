from heapq import heappush, heappop

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        res = []
        
        for i in range(len(nums)):

            heappush(res,nums[i])
        
            if len(res) > k:
                heappop(res)
                
        return heappop(res)
