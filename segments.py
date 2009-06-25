"""
    Author: Hasen il Judy
    License: GPL v2
"""
from iterator import Iterator
from harf import Harf

class SegmentBuilder:
    def build_segments(self, string):
        segments = []
        iter = Iterator(string)
        while iter.in_range():
            segments.append(self.build_segment(iter))
        return segments
        
    def get_dir(self, letter):
        if Harf.is_harf(letter): return "R" #only checks for arabic characterss .. other right-to-left languages are not checked
        elif letter.isalpha(): return "L"
        else: return "N"        

class DefaultSegmentBuilder(SegmentBuilder):
    def build_segment(self, iterator):
        dir = self.get_dir(iterator.get())
        str = u""
        while iterator.in_range() and self.get_dir(iterator.get()) == dir:
            str = str + (iterator.get())
            iterator.move()
        return Segment(str, dir)                

class Segment:
    def __init__(self, str, dir):
        self.str = str
        self.dir = dir
    def __unicdoe__(self):
        return self.str
        
    def get_processed(self):
        if self.dir == "R":
            #set shapings
            shaped = u""
            iter = Iterator(self.str)
            while iter.in_range():
                #get Harf objects for the surrounding letters
                prev = Harf.get(iter.peek_prev())
                current = Harf.get(iter.get())
                next = Harf.get(iter.peek_next())
                #get the shape for the current letter
                shaped = shaped + current.get_contextual_shape(prev, next)
                iter.move()
            return shaped[::-1] #return reversed version .. 
        else:
            return self.str
