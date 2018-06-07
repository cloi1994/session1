# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        data = []
        
        self.serializOp(root,data)
        
        return data
      
    def serializOp(self,root,data):
        
        if not root:
            data.append('#')
            return
        
        data.append(str(root.val))
        
        self.serializOp(root.left,data)
        self.serializOp(root.right,data)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        return self.deserializOp(data)
    
    def deserializOp(self,data):
                    
        val = data.pop(0)
        
        if val == '#':
            return None
              
        root = TreeNode(val)
        
        root.left = self.deserializOp(data)
        root.right = self.deserializOp(data)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
