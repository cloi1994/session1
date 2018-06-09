# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        
        self.dfs(root,res,0)
        
        return res
        
        
    def dfs(self,root,res,depth):
        if not root:
            return 
        
        if depth == len(res):
            res.append(root.val)
            
        self.dfs(root.right,res,depth+1)
        self.dfs(root.left,res,depth+1)
        
# iterative

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        q = [root]
        
        res = []
        
        
        while q != []:
            size = len(q)
            
            for i in range(size):
                node = q.pop(0)
                
                if i == 0:
                    res.append(node.val)
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                    
        return res
                    
        
        

        
     
        
