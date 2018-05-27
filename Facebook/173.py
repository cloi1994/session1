# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.q = []
        self.push(root)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0
        

    def next(self):
        """
        :rtype: int
        """
        return self.q.pop(0)
        
    def push(self,root):
        
        if not root:
            return
        
        self.push(root.left)
        self.q.append(root.val)
        self.push(root.right)
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
