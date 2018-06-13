# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        self.hm = {}
        
        self.helper(root)
        
        res = []
        
        maxFreq = max(self.hm.values())
        
        for k in self.hm:
            if self.hm[k] == maxFreq:
                res.append(k)
        
        return res
        
        
    def helper(self,root):
        
        if not root:
            return
        
        val = self.dfs(root)
        
        self.hm[val] = self.hm.get(val,0) + 1
        self.helper(root.left)
        self.helper(root.right)
        
        
    def dfs(self,root):
        
        if not root:
            return 0
        
        return root.val + self.dfs(root.left) + self.dfs(root.right)
        
