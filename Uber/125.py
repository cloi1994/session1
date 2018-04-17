class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 0:
            return True
        i = 0
        j = len(s) - 1
        
        while i <= j:
            if not s[i].isalpha() and not s[i].isdigit():
                i += 1
                continue
            if not s[j].isalpha() and not s[j].isdigit():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        
