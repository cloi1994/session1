from heapq import heappush, heappop , nsmallest


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        hq = []
        
        res = []
        
        i = 0
        j = 0
        
        while j < len(nums):
            
            if len(hq) < k:
                heappush(hq,-nums[j])
                  
            if len(hq) >= k:
                res.append(-nsmallest(1,hq)[0])
                hq.remove(-nums[i])
                i += 1
            j += 1
            
        return res
                
            
        
        
