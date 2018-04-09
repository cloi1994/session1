class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        ans = "" + A
        
        count = 1
        while ans.find(B) < 0:
            if len(ans) - len(A) > len(B) :
                return -1
            
            ans += A
            count += 1
        
        return count
