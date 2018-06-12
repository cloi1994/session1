class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        res = []
        self.tel = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.dfs(0,digits,[],res)
        
        return res
        
    def dfs(self,i,digits,tmp,res):
        
        if len(tmp) == len(digits):
            res.append(''.join(tmp[:]))
            return
        
        
        for ele in self.tel[digits[i]]:
            tmp.append(ele)
            self.dfs(i+1,digits,tmp,res)
            tmp.pop()
            
            
