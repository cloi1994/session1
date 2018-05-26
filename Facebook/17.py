class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        res = []
        
        self.dic = {'9':'wxyz','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','1':'','0':'','*':'','':'#'}
        
        self.dfs(0,digits,[],res)
        
        return res
        
    def dfs(self,level,digits,tmp,res):
        if len(tmp) == len(digits):
            res.append(''.join(tmp[:]))
            return
        
        for ele in self.dic[digits[level]]:
            tmp.append(ele)
            self.dfs(level+1,digits,tmp,res)
            tmp.pop()
