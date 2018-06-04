# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        
        return self.isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    def isSame(self,s,t):
        
        if not s and t:
            return False
        if not t and s:
            return False
        
        if not t and not s:
            return True
        
        if s.val != t.val:
            return False
        

        
        return self.isSame(s.left,t.left) and self.isSame(s.right,t.right)

        
