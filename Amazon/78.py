class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        tmp = []
        res = []
        
        
        self.dfs(0,nums,tmp,res)
        
        return res
        
    def dfs(self,index,nums,tmp,res):
        
        res.append(tmp[:])
        
        
        for i in range(index,len(nums)):
            tmp.append(nums[i])
            self.dfs(i+1,nums,tmp,res)
            tmp.pop()
        
        
        
    
