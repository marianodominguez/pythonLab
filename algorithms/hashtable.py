'''
Created on Feb 5, 2011

@author: mariano
'''

class Hashtable:
    def __init__(self):            
        self.currentSize = 100
        self.storage = [None for x in range(self.currentSize)]
    def put(self, x):
        index = (self._hash(x)) % self.currentSize
        self.storage[index] = x
    def _hash(self, x):
        result = 0
        for i in x:
            result += ord(i) * 31
        return result
    def __str__(self):
        return ''.join(filter(lambda x : x is not None , self.storage))
    def get(self, x):
        index = (self._hash(x)) % self.currentSize
        if self.storage[index] == x: return self.storage[index]
        return None
