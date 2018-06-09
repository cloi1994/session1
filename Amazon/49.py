class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hm = {}
        
        res = []
        
        for s in strs:
            key = ''.join(sorted(s))
            
            if key in hm:
                hm[key].append(s)
            else:
                hm[key] = [s]
        
        
        for k in hm.keys():
            res.append(hm[k])
        
        
        return res
