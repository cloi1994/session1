class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        
        for i in range(len(s)):
            res += self.extend(i,i,s)
            res += self.extend(i,i+1,s)

        return res
        
        
    def extend(self,left,right,s):
        count = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        
        return count
