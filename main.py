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

if __name__ == "__main__":    
    if 0:
        test_string = u"تجربة test لكتابة عربية"
        ltr = BidiString( test_string )
        rtl = ltr.get_rtl()
        print test_string
        print rtl

    


        
