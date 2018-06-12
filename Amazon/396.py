class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        if not A:
            return 0
        
        
        #F(i) = F(i-1) + sum - n*A[n-i]
        
        summ = 0
        
        t = 0
        
        n = len(A)
        
        for i in range(n):
            summ += A[i]
            t += i * A[i]
            
        res = t
        
        for i in range(1,n):
            t += summ - n * A[n-i]
            res = max(res,t)
        
        
        return res
            
            
