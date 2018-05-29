"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor1(self, root, p):
        # write your code here
        
        if not root or not p:
            return None
        
        s = [root]
        
        found = 0
        
        while root or s:
            
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                if found:
                    return root
                if root.val == p.val:
                    found = 1
                root = root.right
                
        return None
        
    def inorderSuccessor2(self, root, p):
        # write your code here
        
        if not root or not p:
            return None
        
        success = None
        
        while root:
            
            if root.val > p.val:
                success = root
                root = root.left
            else:
                root = root.right
                
        return success
    
    def inorderSuccessor3(self, root, p):
        # write your code here

        return self.dfs(root,p,None)
        
    def dfs(self,root,p,success):
        
        if not root:
            return success
        
        if root.val > p.val:
            success = root
            return self.dfs(root.left,p,success)
        else:
            return self.dfs(root.right,p,success)
            
