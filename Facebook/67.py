class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        
        carry = 0
        res = ""
        
        while carry or i >= 0 or j >= 0:
            summ = carry
            
            if i >= 0:
                summ += int(a[i])
                i -= 1
            if j >= 0:
                summ += int(b[j])
                j -= 1
            
            carry = summ / 2
            summ = summ % 2
            
            res = str(summ) + res
            
        return res
        
        
        
