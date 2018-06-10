class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not s or not t:
            return True
        
        if len(s) != len(t):
            return False
        
        hm = [0] * 256
        
        for i in range(len(s)):
            hm[ord(s[i])] += 1
            hm[ord(t[i])] -= 1
        
        for h in hm:
            if h != 0:
                return False
            
        return True
