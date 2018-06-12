class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.minStack = []
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        self.stack.append(x)
        
        if not self.minStack:
            self.minStack.append(x)
        elif self.minStack[-1] >= x:
            self.minStack.append(x)
            
        

    def pop(self):
        """
        :rtype: void
        """
        
        if self.stack[-1] == self.minStack:
            self.minStack.pop()
        
        
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
