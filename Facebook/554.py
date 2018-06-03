class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        dic = {}
        
        for i in range(len(wall)):
            summ = 0
            for j in range(len(wall[i])-1):
                summ += wall[i][j]
                dic[summ] = dic.get(summ,0) + 1
        
        max_gaps = 0
        
        for v in dic.values():
            max_gaps = max(max_gaps,v)
        
        return len(wall) - max_gaps
                
