class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dic = {}
        
        res = []
        
        for s in strs:
            key = ''.join(sorted(s))
            dic[key] = dic.get(key,[]) + [s]
            
        for val in dic.values():
            res.append(val)
            
            
        return res
