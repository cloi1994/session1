# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i = 0 
        j = n
        
        first = -1
        
        while i <= j:
            
            mid = i + (j - i) // 2
            
            if isBadVersion(mid):
                first = mid
                j =  mid - 1
            else:
                i = mid + 1
                
                
        return first
        
