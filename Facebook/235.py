# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root or not p or not q:
            return root
        
        if(p.val > q.val):
            return self.dfs(root, q, p);
        
        return self.dfs(root,p,q)
    
    def dfs(self,root,p,q):
        
        if not root:
            return root
        
        if root.val > p.val and root.val > q.val:
            return self.dfs(root.left,p,q)
        elif root.val < p.val and root.val < q.val:
            return self.dfs(root.right,p,q)
        else:
            return root
            
        
        
        
        
        
        
        
