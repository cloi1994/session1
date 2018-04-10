class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        s = str.split()
        p = pattern
        
        if len(s) != len(p):
            return False
        
        pHm = {}
        sHm = {}
        
        for i in range(len(s)):
            if p[i] not in pHm and s[i] not in sHm:
                pHm[p[i]] = s[i]
                sHm[s[i]] = p[i]
            elif p[i] in pHm and s[i] != pHm[p[i]]:
                return False
            elif s[i] in sHm and p[i] != sHm[s[i]]: 
                return False
            
        return True
        
        
