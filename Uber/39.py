class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(0,candidates,target,[],res)
        return res
        
    def dfs(self,level,candidates,target,tmp,res):
        
        if target == 0:
            res.append(tmp[:])
            return
        if target < 0:
            return
        
        for i in range(level,len(candidates)):
            tmp.append(candidates[i])
            self.dfs(i,candidates,target-candidates[i],tmp,res)
            tmp.pop()
