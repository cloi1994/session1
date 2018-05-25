from heapq import heappush, heappop

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        dic = {}
        
        pq = []
        
        res = 0
        
        for t in tasks:
            dic[t] = dic.get(t,0) + 1
            
        #inserting to heap
        
        
        # max heap is negative
        for v in dic.values():
            heappush(pq,-v)
                  
        
        while pq:
            k = 0
            tmpTask = []
            
            for i in range(n+1):
                if pq:
                    tmpTask.append(heappop(pq)+1)
                    k += 1        
            
            for t in tmpTask:
                if t < 0:
                    heappush(pq,t)
                    
            if not pq:
                res += k
            else:
                res += (n + 1)
            
        return res
        
            
        
            
        
