class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = x
        if self.st != []:
            curMin = min(self.st[-1][1],x)
            
        self.st.append([x,curMin])
         

    def pop(self):
        """
        :rtype: void
        """
        self.st.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.st[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
