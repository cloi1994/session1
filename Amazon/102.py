# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.res = []
        
        self.dfs(root,0)
        
        return self.res
        
    def dfs(self,root,step):
        
        if not root:
            return
        
        if len(self.res) == step:
            self.res.append([])
        
        self.res[step].append(root.val)
        
        self.dfs(root.left,step+1)
        self.dfs(root.right,step+1)
