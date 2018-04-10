class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        l = 0
        t = 0
        
        r = len(matrix[0]) - 1
        b = len(matrix) - 1
        
        res = []
        
        while t <= b and l <= r:
            
            #one row left
            if t == b:
                for i in range(l,r+1):
                    res.append(matrix[t][i])
                break
            #one col left
            elif l == r:
                for i in range(t,b+1):
                    res.append(matrix[i][l])
                break
            
            else:
                
                for i in range(l,r+1):
                    res.append(matrix[t][i])
                t += 1
                for i in range(t,b+1):
                    res.append(matrix[i][r])
                r -= 1
                for i in range(r,l-1,-1):
                    res.append(matrix[b][i])
                b -= 1
                for i in range(b,t-1,-1):
                    res.append(matrix[i][l])
                l += 1
                
        return res
            
            
            
                
            
