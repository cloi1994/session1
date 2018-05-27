# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
            
        if not root:
            return []
        
        res = []
        
        self.dfs(root,"",res)
        
        return res
        
    def dfs(self,root,tmp,res):
        
        tmp += str(root.val)
        
        if not (root.left or root.right):
            res.append(tmp)
            return
                
        tmp += "->"
        
        
        if root.left:
            self.dfs(root.left,tmp,res)
        if root.right:
            self.dfs(root.right,tmp,res)
