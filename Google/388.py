class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        
        st = [0]
        
        res = 0
        
        for s in input.split("\n"):
            level = s.rfind('\t') + 1
            
            #keep poping until that level + 1 == len(st)
            # level + 1 because base stack is 0
            while level + 1 < len(st):
                st.pop()
            
            curLen = st[-1] + len(s) - level + 1
            st.append(curLen)
            
            if '.' in s:
                res = max(res,curLen-1)
                
        return res
