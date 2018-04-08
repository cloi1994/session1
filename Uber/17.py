class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        hm = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        tmp = ""
        res = []
        self.dfs(0,digits,tmp,res,hm)
        return res
        
    def dfs(self,level,digits,tmp,res,hm):
        
        if len(tmp) == len(digits):
            res.append(tmp)
            return
        
        for c in hm[digits[level]]:
            self.dfs(level+1,digits,tmp+c,res,hm)
        
    # Time : O(c^len(digits))
    # Space : O(len(digits))
