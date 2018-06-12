import random 

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.index = {}
        self.arr = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val in self.index:
            return False
        
        self.arr.append(val)
        self.index[val] = len(self.arr) - 1
        
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val not in self.index:
            return False
        
        
        oldValIndex = self.index[val]
        
        
        lastVal = self.arr[-1]
        
        self.index[lastVal] = oldValIndex
        self.arr[oldValIndex] = lastVal
        
        
        self.index.pop(val)

        self.arr.pop()
        
        
        
        
        
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
                
        
        randindex = random.randint(0,len(self.arr) - 1)
        
        return self.arr[randindex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
