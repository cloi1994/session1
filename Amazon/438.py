class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if not s or len(p) > len(s):
            return []
        
        smap = [0] * 256
        pmap = [0] * 256
        
        for i in range(len(p)):
            smap[ord(s[i])] += 1
            pmap[ord(p[i])] += 1
            
        res = [] 
        
        
        if smap == pmap:
            res.append(0)
        
        
        i = 0
        
        for j in range(len(p),len(s)):
            
             
            smap[ord(s[j])] += 1
            smap[ord(s[i])] -= 1
            
            if smap == pmap:
                res.append(i+1)            
            i += 1
            
            
        return res
                
            
