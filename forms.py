"""
    Author: Hasen il Judy
    License: GPL v2
"""

class HarfForms:
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
    harf = HarfForms(*args)
    harf_list[harf.standard] = harf
    harf_list[harf.isolated] = harf
    harf_list[harf.initial] = harf
    harf_list[harf.medial] = harf
    harf_list[harf.final] = harf
    
def get_harf(char):
    try:
        return harf_list[char]
    except:
        return HarfForms(char, char, char, char, char, False, False)
    
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


    
merges = [
        ('',''),
        ]

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

next = lambda x: unichr(ord(x)+1)

def add_connecting_harf(standard, isolated):
    final = next(isolated)
    initial = next(final)
    medial = next(initial)
    add_harf(standard, isolated, final, initial, medial, True, True)

def add_non_connecting_harf(standard, isolated):
    final = next(isolated)
    initial = isolated
    medial = final
    add_harf(standard, isolated, final, initial, medial, True, False)

add_harf(None, None, None, None, None, False, False)
# Hamza groups
add_non_connecting_harf(u'\u0622', u'\uFE81')
add_non_connecting_harf(u'\u0623', u'\uFE83')
add_non_connecting_harf(u'\u0624', u'\uFE85')
add_non_connecting_harf(u'\u0625', u'\uFE87')
add_connecting_harf(u'\u0626', u'\uFE89')
# Main letters
add_non_connecting_harf(u'\u0627', u'\uFE8D')
add_connecting_harf(u'\u0628', u'\uFE8F')
add_connecting_harf(u'\u062A', u'\uFE95')
add_connecting_harf(u'\u062B', u'\uFE99')
add_connecting_harf(u'\u062C', u'\uFE9D')
add_connecting_harf(u'\u062D', u'\uFEA1')
add_connecting_harf(u'\u062E', u'\uFEA5')
add_non_connecting_harf(u'\u062F', u'\uFEA9')
add_non_connecting_harf(u'\u0630', u'\uFEAB')
add_non_connecting_harf(u'\u0631', u'\uFEAD')
add_non_connecting_harf(u'\u0632', u'\uFEAF')
add_connecting_harf(u'\u0633', u'\uFEB1')
add_connecting_harf(u'\u0634', u'\uFEB5')
add_connecting_harf(u'\u0635', u'\uFEB9')
add_connecting_harf(u'\u0636', u'\uFEBD')
add_connecting_harf(u'\u0637', u'\uFEC1')
add_connecting_harf(u'\u0638', u'\uFEC5')
add_connecting_harf(u'\u0639', u'\uFEC9')
add_connecting_harf(u'\u063A', u'\uFECD')
add_connecting_harf(u'\u0641', u'\uFED1')
add_connecting_harf(u'\u0642', u'\uFED5')
add_connecting_harf(u'\u0643', u'\uFED9')
add_connecting_harf(u'\u0644', u'\uFEDD')
add_connecting_harf(u'\u0645', u'\uFEE1')
add_connecting_harf(u'\u0646', u'\uFEE5')
add_connecting_harf(u'\u0647', u'\uFEE9')
add_non_connecting_harf(u'\u0648', u'\uFEED')
add_connecting_harf(u'\u064A', u'\uFEF1')
# Letters that are not directly in the alphabet
add_non_connecting_harf(u'\u0629', u'\uFE93')
# This one is problematic, as its medial form is not available, and it doesn't have an initial form, so for that I'm using the ـ kashida/tatweel 
add_harf(u'\u0649', u'\uFEEF', u'\uFEF0', u'\u0640', u'\u0640', False, False) 

