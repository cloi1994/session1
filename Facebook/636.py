class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        prev = 0

        s = []
        
        res = [0] * n
        
        for l in logs:
            fid, action, cur = l.split(':')
            
            cur = int(cur)
            
            if action == 'start':
                if s != []:
                    res[s[-1]] += cur - prev
                s.append(int(fid))
                prev = cur
            else:
                res[s[-1]] += cur - prev + 1
                s.pop()
                prev = cur + 1
                
        return res
        
