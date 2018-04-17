# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.hm = {}

        return self.rob1(root)

        
    def rob1(self,root):
        if root == None:
            return 0
        if root in self.hm:
            return self.hm[root]
        
        left_sub = 0
        right_sub = 0
        
        if root.left:
            left_sub += self.rob1(root.left.left) + self.rob1(root.left.right)
            
        if root.right:
            right_sub += self.rob1(root.right.left) + self.rob1(root.right.right)
            
        curMax = max(root.val +left_sub + right_sub, self.rob1(root.left) + self.rob1(root.right))
        self.hm[root] = curMax
        return curMax
        
