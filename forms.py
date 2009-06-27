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
        (u'\u0644\u0627',u'\uFEFB'), # لا
        (u'\u0644\u0622',u'\uFEF5'), # لآ
        (u'\u0644\u0623',u'\uFEF7'), # لأ
        (u'\u0644\u0625',u'\uFEF9'), # لإ
        ]

def fuse(string):
    """Fuse together lam-alef sequences"""
    for merge in merges:
        string = string.replace(merge[0], merge[1])
    return string

harakat_ranges = [ # Note: ranges are inclusive
        (u'\u0610', u'\u061A'),
        (u'\u064B', u'\u065E'),
        (u'\u0670', u'\u0670'),
        (u'\u06D6', u'\u06DC'),
        (u'\u06DF', u'\u06E8'),
        (u'\u06EA', u'\u06ED'),
        ]

def is_haraka(char):
    for a,b in harakat_ranges:
        if char >= a and char <= b: # inclusive
            return True
    return False

def split_harakat(string):
    """Split the string into a tuple harakat_info, string
    harakat_info is a data structure that can be used as input
    to put_harakat, which is used after shaping the string
    """
    harakat = []
    plain = u''
    for index, char in enumerate(string):
        if(is_haraka(char)):
            harakat += [(index, char)]
        else:
            plain += char
    return harakat, plain

def put_harakat(harakat_info, plain):
    """Put back the harakat that were extracted from split_harakat"""
    res = ''
    index = 0
    while True:
        if not plain:
            for _, char in harakat_info:
                res += char
            break
        if not harakat_info:
            res += plain
            break
        h_index, h_char = harakat_info[0]
        if index == h_index:
            res += h_char
            harakat_info = harakat_info[1:]
        else:
            res += plain[0]
            plain = plain[1:]
        index += 1
    return res

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
# Lam-Aleft
add_non_connecting_harf(u'\uFEFB', u'\uFEFB')
add_non_connecting_harf(u'\uFEF9', u'\uFEF9')
add_non_connecting_harf(u'\uFEF7', u'\uFEF7')
add_non_connecting_harf(u'\uFEF5', u'\uFEF5')
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
add_non_connecting_harf(u'\u0649', u'\uFEEF')
# tatweel
add_harf(u'\u0640', u'\u0640', u'\u0640', u'\u0640', u'\u0640', True, True)

