class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        
        res = "1"
        
        for _ in range(n-1):
            tmp = ""
            count = 1
            for i in range(1,len(res)):
                if res[i-1] == res[i]:
                    count += 1
                else:
                    tmp += str(count) + res[i-1]
                    count = 1
                prev = res[i]
            res = tmp + str(count) + res[-1]
        return res
