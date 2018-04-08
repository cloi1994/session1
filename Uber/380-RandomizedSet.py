import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hm = {}
        self.num = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hm:
            return False
        
        self.num.append(val)
        self.hm[val] = len(self.num) - 1
        
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hm:
            return False
        
        target_idx = self.hm[val]
        last_idx = self.hm[self.num[-1]]
        
        self.hm[self.num[last_idx]] = target_idx
        
        self.num[target_idx] , self.num[last_idx] = self.num[last_idx] , self.num[target_idx]
        
        self.num.pop()
        self.hm.pop(val,0)
        
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.num == []:
            return None
        return self.num[random.randint(0,len(self.num)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
