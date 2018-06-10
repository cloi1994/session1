class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        res = 0
                
        for i in range(2,n):
            isPrime = True
            for j in range(2,i):
                if i % j == 0:
                    isPrime =  False
            if isPrime:
                res += 1
        return res
