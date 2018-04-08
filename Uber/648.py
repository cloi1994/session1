class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        
        res = []
        
        sList = sentence.split()
        
        for s in sList:
            found = False
            for prefix in dict:
                if self.startWith(prefix,s):
                    found = True
                    res.append(prefix)
                    break
            if not found:
                res.append(s)
                
        return ' '.join(res)
                
    def startWith(self,prefix,s):
        if len(prefix) > len(s):
            return False
        
        for i in range(len(prefix)):
            if prefix[i] != s[i]:
                return False
        return True
        
