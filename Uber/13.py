class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        
        
        summ = d[s[-1]]
        
        for i in range(len(s)-2,-1,-1):
            v1 = d[s[i]]
            v2 = d[s[i+1]]
            
            if v2 > v1:
                summ -= v1;  
            else:
                summ += v1
                
        return summ
        
