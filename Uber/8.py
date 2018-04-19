class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        
        if not s:
            return 0
        s = s.replace(" ", "")
        if s[0].isalpha():
            return 0
        
        ans = 0
        sign = 1
        
        if s[0] == '-':
            sign = -1
                
        for i in range(len(s)):
            if s[i] == '.':
                break
            if s[i].isdigit():
                ans = ans * 10 + int(s[i])
              
        if ans >= 2**31:
            return 2147483648 * sign
            
        return ans * sign
