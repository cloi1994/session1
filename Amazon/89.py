class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        if n < 0:
            return []
        
        res = [0]
        
        inc = 1
        
        for _ in range(n):
            for i in range(len(res)-1,-1,-1):
                res.append(res[i] + inc)
            inc = inc << 1
            
        return res
            
            
        
