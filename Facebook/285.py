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
    def inorderSuccessor(self, root, p):
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
        
            def inorderSuccessor(self, root, p):
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
