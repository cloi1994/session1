class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        self.ans = 0
        
        self.dfs(0,nums,S,[])
        
        
        return self.ans
    
    def dfs(self,i,nums,S,tmp):
        
        if i == len(nums): # len(tmp) == len(nums)
            if S == 0:
                self.ans += 1
            return
                
        self.dfs(i+1,nums,S-nums[i],tmp)
        self.dfs(i+1,nums,S+nums[i],tmp)
        
