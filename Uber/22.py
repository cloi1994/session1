class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        tmp = ""
        res = []
        self.dfs(0,0,n,tmp,res)
        
        return res
        
    def dfs(self,left,right,n,tmp,res):
        
        if len(tmp) == 2*n:
            res.append(tmp)
            return
        
        if left < n:
            self.dfs(left+1,right,n,tmp+'(',res)
        
        if left > right:
            self.dfs(left,right+1,n,tmp+')',res)
        
    # time : O(n!) because 654321
    # space : O(2n)
