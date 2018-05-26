

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        
        if not root:
            return []
        
        q = [[root,0]]
        
        dic = {}
        
        res = []
        
        while q != []:
            node,level = q.pop(0)
            
            dic[level] = dic.get(level,[]) + [node.val]
            
            if node.left:
                q.append([node.left,level-1])
            if node.right:
                q.append([node.right,level+1])
                
        
        keys = dic.keys()
        
        keys.sort()

        for k in keys:
            res.append(dic[k])
            
        return res
