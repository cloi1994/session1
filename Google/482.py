class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        cnt = 0
        
        S = S.upper()
        
        res = ""
        
        for i in range(len(S)-1,-1,-1):
            
            if S[i] == "-":
                continue
            res += S[i]
            cnt += 1
            if cnt % K == 0:
                res += '-'
        
        if res[-1] == "-":
            res = res[:-1]
        
        return res[::-1]
            
            
            
        
