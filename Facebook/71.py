class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        pathList = path.split('/')
        
        s = []
        
        for p in pathList:
            if p == '.' or p == '':
                continue
            elif p == '..':
                if s != []:
                    s.pop()  
            else:
                s.append(p)
        
        return '/' + '/'.join(s)
