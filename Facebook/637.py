# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        q = [root]
        
        res = []
        
        while q != []:
            summ = 0.0
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                summ += node.val
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                
            res.append(summ/size)
        
        return res
