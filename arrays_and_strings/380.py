import random

class RandomizedSet(object):

    def __init__(self):
        self.set = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            self.set.add(val)
            return True
        return False
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.set)) # cast to list to be able to index values in set and each value has equal probability
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()