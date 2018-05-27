class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        :type s: str
        :rtype: bool
        """
                        
        i = 0 
        j = len(s) - 1
        
        allowOnce = 0
        
        while i <= j:      
            if s[i].lower() != s[j].lower():
                return self.isPalindromeCheck(s,i+1,j) or self.isPalindromeCheck(s,i,j-1)
            i += 1
            j -= 1
            
        return True
    
    def isPalindromeCheck(self,s,i,j):
        
        while i <= j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
            
        return True
            
        
        
