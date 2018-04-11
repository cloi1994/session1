class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(0,nums,[],res)
        
        return res
        
    def dfs(self,level,nums,tmp,res):
        
        res.append(tmp[:])
        
        for i in range(level,len(nums)):
            tmp.append(nums[i])
            self.dfs(i+1,nums,tmp,res)
            tmp.pop()
