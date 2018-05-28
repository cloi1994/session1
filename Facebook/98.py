# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        
        return self.dfs(root,float('-inf'),float('inf'))
    
    
    def dfs(self,root,leftLimit,rightLimit):
        
        if not root:
            return True
        
        if root.val < leftLimit or root.val > rightLimit:
            return False
        
        
        return self.dfs(root.left,leftLimit,root.val-1) and self.dfs(root.right,root.val+1,rightLimit)
        
        
        
