# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.hm = {}
        
        return self.dfs(root,k)
        
        
    def dfs(self,root,k):
        
        if not root:
            return False
        
        if root.val in self.hm:
            return True
        
        self.hm[k - root.val] = 1 
        
        return self.dfs(root.left,k) or self.dfs(root.right,k)
        
