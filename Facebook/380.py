import random
class RandomizedSet(object):
    
    #[1,3,2]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.arr = []
        self.hm = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hm:
            return False
        
        self.arr.append(val)
        self.hm[val] = len(self.arr) - 1
        
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hm:
            return False
        
        last = self.arr[-1]
        
        val_index = self.hm[val]
        
        self.hm[last] = val_index
        self.arr[val_index] = last
        
        self.hm.pop(val)
        self.arr.pop()
        
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        return self.arr[random.randint(0,len(self.arr)-1)]
        
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
