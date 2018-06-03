class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(0,nums,[],res)
        
        return res
        
    def dfs(self,level,nums,tmp,res):
        
        res.append(tmp[:])
        
        for i in range(level,len(nums)):
            
            if i > level and nums[i] == nums[i-1]:
                continue
            
            tmp.append(nums[i])
            self.dfs(i+1,nums,tmp,res)
            tmp.pop()
