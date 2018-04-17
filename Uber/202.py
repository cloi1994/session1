class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hm = {}
        n = str(n)
        while n not in hm:
            hm[n] = 1
            digits = []
            summ = 0
            for c in n:
                digits.append(c)
            for d in digits:
                summ += int(d)**2
            if summ == 1:
                return True 
            n = str(summ)
            
        return False
