"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        
        iMap = {}
        sMap = {}
                
        for e in employees:
            sMap[e.id] = e.subordinates
            iMap[e.id] = e.importance
            
            
        self.ans = 0
        
        self.dfs(id,iMap,sMap)
                
        return self.ans
    
    def dfs(self,id,iMap,sMap):
        
        self.ans += iMap[id]
        
        for i in sMap[id]:
            self.dfs(i,iMap,sMap)
        
        
