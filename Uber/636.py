class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        s = []
        
        res = [0] * n
        
        prev = 0
                
        for l in logs:
            l_split = l.split(':')
            fid = l_split[0]
            status = l_split[1]
            time = int(l_split[2])
                    
            if status == 'start':
                if s:
                    res[s[-1]] += int(time) - prev
                    
                s.append(int(fid))
                prev = time
            else:
                end_fid = s.pop()
                res[end_fid] += time - prev + 1
                prev = time + 1
                
        return res
                
                
                
        
