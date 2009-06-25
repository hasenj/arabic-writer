"""
    Author: Hasen il Judy
    License: GPL v2
"""
from harf import Harf
from segments import DefaultSegmentBuilder
       
class BidiString:
    def __init__(self,str):
        self.segments = DefaultSegmentBuilder().build_segments(str)            
        
    def get_rtl(self):
        result = u""
        rsegments = self.segments
        rsegments.reverse()
        for segment in rsegments:
            result += segment.get_processed()
        return result

def rtlize(string):
    return BidiString(string).get_rtl()

