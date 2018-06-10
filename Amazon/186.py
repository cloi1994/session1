class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s or len(s) == 0 or s == " ":
            return ""
        
        
        left = 0
        
        
        s = list(s)
        
        for i in range(len(s)+1):
            if i == len(s) or s[i] == ' ':
                self.reverse(s,left,i-1)
                left = i + 1
                
        self.reverse(s,0,len(s)-1)
        
        
        
        
        return ''.join(s)
        
    def reverse(self,s,left,right):
                
        while left < right:
        
            s[left] , s[right] = s[right] , s[left]
            left +=1
            right -= 1
        
        
        
        
