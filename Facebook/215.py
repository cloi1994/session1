from heapq import heappush,heappop

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        pq = []
        
        
        for i in range(len(nums)):
            heappush(pq,nums[i])
            if len(pq) > k:
                heappop(pq)
            
        return heappop(pq)
        
        
        
