"""
    Author: Hasen il Judy
    License: GPL v2
"""

class Iterator:
    def __init__(self, list):
        self.list = list
        self.i = 0
    def reset(self):    
        self.i = 0
    def get(self):
        return self.list[self.i]
    def in_range(self, index = None):
        if index == None: index = self.i
        return index in range(0,len(self.list))
    def peek_index(self, index):
        if self.in_range(index) : return self.list[index]
        else: return None        
    def peek_next(self):
        return self.peek_index(self.i + 1)
    def peek_prev(self):
        return self.peek_index(self.i - 1)
    def move(self):
        self.i = self.i+1        
