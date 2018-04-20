# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        
        self.hm = {}
        return self.dfs(node)
        
    def dfs(self,node):
        
        if node == None:
            return None
        
        if node.label in self.hm:
            return self.hm[node.label]
        
        clone = UndirectedGraphNode(node.label)
        
        self.hm[node.label] = clone
        
        for n in node.neighbors:
            clone.neighbors.append(self.dfs(n))
            
            
        return clone
            
            
        
