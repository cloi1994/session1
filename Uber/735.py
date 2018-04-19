class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        st = [] 
        
        for a in asteroids:
            if not st or a > 0:
                st.append(a)
            else:
                while len(st) > 0 and st[-1] > 0:
                    if -st[-1] == a:
                        st.pop()
                        break
                    elif st[-1] < -a:
                        st.pop()
                        continue
                    elif st[-1] > -a:
                        break
                else:
                    st.append(a)
                        
                        
                    
                    
        return st
                    
            
        
