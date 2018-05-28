class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        
        if not s or len(s) < len(p):
            return []
        
        hmP = [0] * 256
        hmS = [0] * 256
        
        res = []
        
        for i in range(len(p)):
            hmP[ord(p[i])] += 1
            hmS[ord(s[i])] += 1
            
            
        if hmP == hmS:
            res.append(0)
            
            
        for i in range(len(p),len(s)):
            hmS[ord(s[i])] += 1
            hmS[ord(s[i - len(p)])] -= 1

            if hmP == hmS:
                res.append(i - len(p) + 1)
            
        return res
