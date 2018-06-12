class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        hm = {}
        res = []

        
        for ele in s:
            if ele not in hm:
                hm[ele] = ele
            else:
                hm[ele] += ele
            
            
        for v in hm.values():
            res.append(v)
            
        res.sort(key= lambda x:-len(x))
        
            
        return ''.join(res)
        
