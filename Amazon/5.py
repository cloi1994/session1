class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.maxLen = 0
        self.low = 0
        
        for i in range(len(s)):
            self.expandFromCenter(i,i,s) #odd
            self.expandFromCenter(i,i+1,s) #even
        return s[self.low:self.low + self.maxLen]
        
            
    def expandFromCenter(self,left,right,s):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
            
        left += 1
        right -= 1
            
        if self.maxLen < right - left + 1:
            self.maxLen = right - left + 1
            self.low = left
            
            
