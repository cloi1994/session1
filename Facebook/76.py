class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        curDic = {}
        tDic = {}
        
        for ele in t:
            tDic[ele] = tDic.get(ele,0) + 1
            
        i = 0
        j = 0
        
        left = -1
        right = -1
            
        ans = float('inf')
        while j < len(s):
            
            curDic[s[j]] = curDic.get(s[j],0) + 1
            j += 1
            
            while i < len(s) and self.hasAllEle(curDic,tDic):
                
                if j - i < ans:
                    left = i
                    right = j
                    ans = j - i
                    
                curDic[s[i]] -= 1 
                i += 1
                
            
            
        return s[left:right]
    
    def hasAllEle(self,curDic,tDic):
        for ele in tDic.keys():
            if ele not in curDic or curDic[ele] < tDic[ele]:
                return False
        return True
