class Solution:
    """
    @param ages: The ages
    @return: The answer
    """
    def friendRequest(self, ages):
        # Write your code here
        
        n = len(ages)
        count = 0
       
        for i in range(n):
            for j in range(i+1,n):
                if self.check(ages[i] , ages[j]):
                    count += 1
                if self.check(ages[j] , ages[i]):
                    count += 1
                           
        return count
           
    def check(self,a,b):
        if b <= (a/2) + 7:
            return False
        if b > a:
            return False
        if b < 100 and a > 100:
            return False
        return True
