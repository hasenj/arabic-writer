"""
    Author: Hasen il Judy
    License: GPL v2
"""

class HarfShapes:
    """
        Forms of an arabic harf
    """
    def __init__(self, standard, isolated, final, initial, medial, prev_connect, next_connect):
        self.standard = standard
        self.isolated = isolated
        self.final = final
        self.initial = initial
        self.medial = medial
        self.prev_connect = prev_connect
        self.next_connect = next_connect

harf_list = {}
def add_harf(*args):
    harf = HarfShapes(*args)
    harf_list[harf.standard] = harf
    harf_list[harf.isolated] = harf
    harf_list[harf.initial] = harf
    harf_list[harf.medial] = harf
    harf_list[harf.final] = harf
    
def get_harf(char):
    try:
        return harf_list[char]
    except:
        return HarfShapes(char, char, char, char, char, False, False)
    
def is_harf(char):
    return ord(char) in range(0x0600, 0x06FF+1) or ord(char) in range(0xFE70, 0xFEFF+1) #numbers from unicode charts (links below)


def get_contextual_shape(prev, harf, next):
    """return unicode representation of contextual shape"""
    prev = get_harf(prev)
    harf = get_harf(harf)
    next = get_harf(next)
    next_connection = harf.next_connect and next.prev_connect
    prev_connection = harf.prev_connect and prev.next_connect
    if next_connection and prev_connection: return harf.medial
    elif next_connection and not prev_connection: return harf.initial
    elif prev_connection and not next_connection: return harf.final
    else: return harf.isolated 

"""
    Unicode codes acquired from:
        Standard forms (isolated):
            http://www.unicode.org/charts/PDF/U0600.pdf
        Presentation forms (contextual):
            http://www.unicode.org/charts/PDF/UFE70.pdf
"""
        
# Harf Shapes list/table
# Form:
# add_harf(standard, isolated, final, initial, medial, connects to previous?, connects to next?)

add_harf(None, None, None, None, None, False, False)
# Main letters
add_harf(u'\u0627', u'\uFE8D', u'\uFE8E', u'\uFE8D', u'\uFE8E', True, False)
add_harf(u'\u0628', u'\uFE8F', u'\uFE90', u'\uFE91', u'\uFE92', True, True)
add_harf(u'\u062A', u'\uFE95', u'\uFE96', u'\uFE97', u'\uFE98', True, True)
add_harf(u'\u062B', u'\uFE99', u'\uFE9A', u'\uFE9B', u'\uFE9C', True, True)
add_harf(u'\u062C', u'\uFE9D', u'\uFE9E', u'\uFE9F', u'\uFEA0', True, True)
add_harf(u'\u062D', u'\uFEA1', u'\uFEA2', u'\uFEA3', u'\uFEA4', True, True)
add_harf(u'\u062E', u'\uFEA5', u'\uFEA6', u'\uFEA7', u'\uFEA8', True, True)
add_harf(u'\u062F', u'\uFEA9', u'\uFEAA', u'\uFEA9', u'\uFEAA', True, False)
add_harf(u'\u0630', u'\uFEAB', u'\uFEAC', u'\uFEAB', u'\uFEAC', True, False)
add_harf(u'\u0631', u'\uFEAD', u'\uFEAE', u'\uFEAD', u'\uFEAE', True, False)
add_harf(u'\u0632', u'\uFEAF', u'\uFEB0', u'\uFEAF', u'\uFEB0', True, False)
add_harf(u'\u0633', u'\uFEB1', u'\uFEB2', u'\uFEB3', u'\uFEB4', True, True)
add_harf(u'\u0634', u'\uFEB5', u'\uFEB6', u'\uFEB7', u'\uFEB8', True, True)
add_harf(u'\u0635', u'\uFEB9', u'\uFEBA', u'\uFEBB', u'\uFEBC', True, True)
add_harf(u'\u0636', u'\uFEBD', u'\uFEBE', u'\uFEBF', u'\uFEC0', True, True)
add_harf(u'\u0637', u'\uFEC1', u'\uFEC2', u'\uFEC3', u'\uFEC4', True, True)
add_harf(u'\u0638', u'\uFEC5', u'\uFEC6', u'\uFEC7', u'\uFEC8', True, True)
add_harf(u'\u0639', u'\uFEC9', u'\uFECA', u'\uFECB', u'\uFECC', True, True)
add_harf(u'\u063A', u'\uFECD', u'\uFECE', u'\uFECF', u'\uFED0', True, True)
add_harf(u'\u0641', u'\uFED1', u'\uFED2', u'\uFED3', u'\uFED4', True, True)
add_harf(u'\u0642', u'\uFED5', u'\uFED6', u'\uFED7', u'\uFED8', True, True)
add_harf(u'\u0643', u'\uFED9', u'\uFEDA', u'\uFEDB', u'\uFEDC', True, True)
add_harf(u'\u0644', u'\uFEDD', u'\uFEDE', u'\uFEDF', u'\uFEE0', True, True)
add_harf(u'\u0645', u'\uFEE1', u'\uFEE2', u'\uFEE3', u'\uFEE4', True, True)  
add_harf(u'\u0646', u'\uFEE5', u'\uFEE6', u'\uFEE7', u'\uFEE8', True, True)
add_harf(u'\u0647', u'\uFEE9', u'\uFEEA', u'\uFEEB', u'\uFEEC', True, True)      
add_harf(u'\u0648', u'\uFEED', u'\uFEEE', u'\uFEED', u'\uFEEE', True, False)
add_harf(u'\u064A', u'\uFEF1', u'\uFEF2', u'\uFEF3', u'\uFEF4', True, True)
# Letters that are not directly in the alphabet
add_harf(u'\u0629', u'\uFE93', u'\uFE94', u'\uFE93', u'\uFE94', True,  False)
# This one is problematic, as its medial form is not available, and it doesn't have an initial form, so for that I'm using the ـ kashida/tatweel 
add_harf(u'\u0649', u'\uFEEF', u'\uFEF0', u'\u0640', u'\u0640', False, False) 
