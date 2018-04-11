class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hm = {}
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1
        for c in t:
            if c not in hm:
                return False
            else:
                hm[c] -= 1
        for k in hm:
            if hm[k] != 0:
                return False
        return True
        
