import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k <= 0:
            return []
        
        h = []
        ans = []
        
        i = 0
        
        while i < len(nums1) and i < k:
            heapq.heappush(h,(nums1[i]+nums2[0], nums1[i], nums2[0] , 0))
            i += 1
        
        while h != [] and k > 0:
            cur = heapq.heappop(h)
            ans.append([cur[1],cur[2]])
            k -= 1
            if cur[3] == len(nums2) - 1:
                continue
            heapq.heappush(h,(cur[1]+nums2[cur[3]+1], cur[1], nums2[cur[3]+1] , cur[3]+1))
        return ans
            
        
