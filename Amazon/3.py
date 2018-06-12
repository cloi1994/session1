class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        i = 0
        j = 0
        
        sset = set()
        
        best = 0
        
        while j < len(s):
            
            while s[j] in sset:
                sset.remove(s[i])
                i += 1
            
            
            sset.add(s[j])
            j += 1
            
            best = max(best,j-i)
            
        
        
        return best
        
                
            
            
