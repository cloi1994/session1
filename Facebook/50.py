class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.power(x,-n)
        
        return self.power(x,n)
    
    def power(self,x,n):
        
        if n == 0:
            return 1
        
        res = self.power(x,n/2)
        
        res *= res
        
        if n % 2 == 1:
            res *= x
        return res
