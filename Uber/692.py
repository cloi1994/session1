from heapq import *

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        hm = {}
        
        heap = []
        
        res = []
        
        for w in words:
            if w in hm:
                hm[w] += 1
            else:
                hm[w] = 1
                
        for key in hm:
            heappush(heap, (-hm[key],key))

        for i in range(k):
            res.append(heappop(heap)[1])
            
        return res
        
        
        
        
