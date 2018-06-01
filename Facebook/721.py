class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        owner = {}
        root = {}
        
        m = {}
        
        res = []
        
        for a in accounts:
            
            for i in range(1,len(a)):
                root[a[i]] = a[i]
                owner[a[i]] = a[0]
                
        for a in accounts:
            
            p = self.find(a[1],root)
            
            for i in range(2,len(a)):
                root[self.find(a[i], root)] = p
                
        for a in accounts:
                        
            for i in range(1,len(a)):
                key = self.find(a[i], root)
                m[key] = m.get(key,[]) + [a[i]]
                
        for k in m.keys():
            v = sorted(list(set(m[k])))
            res.append([owner[k]] + v)

        return res
    def find(self,s,root):
        if root[s] == s:
            return s
        else:
            return self.find(root[s],root)
