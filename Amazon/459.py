class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool 
        """
        for i in range(1, len(s)):
            if len(s) % i == 0 and int(len(s)/i) * s[:i] == s:
                return True
        return False
