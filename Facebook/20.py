class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []      
        
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                stack.append(s[i])
            else:
                if stack == [] or abs(ord(stack[-1]) - ord(s[i])) > 2 :
                    return False
                stack.pop()
        
        return len(stack) == 0
                
                
        
