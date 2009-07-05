"""
    Author: Hasen il Judy
    License: GPL v2
"""

class HarfForms:
    """
        Forms of an arabic harf (letter)
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
rev_list = {}
def add_forms(*args):
    harf = HarfForms(*args)
    harf_list[harf.standard] = harf
    rev_list[harf.isolated] = harf.standard
    rev_list[harf.final] = harf.standard
    rev_list[harf.initial] = harf.standard
    rev_list[harf.medial] = harf.standard
    
def get_forms(char):
    try:
        return harf_list[char]
    except:
        return HarfForms(char, char, char, char, char, False, False)
    
def is_harf(char):
    return ord(char) in range(0x0600, 0x06FF+1) or ord(char) in range(0xFE70, 0xFEFF+1) #numbers from unicode charts (links below)


def get_contextual_shape(prev, harf, next):
    """return unicode representation of contextual shape"""
    prev = get_forms(prev)
    harf = get_forms(harf)
    next = get_forms(next)
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

def unfuse(string):
    """Break-apart lam-alef merges"""
    for merge in merges:
        string = string.replace(merge[1], merge[0])
    return string

def get_std_shape(char):
    """The opposite of get_contextual_shape"""
    return rev_list.get(char, char)


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
        

# Get the next unicode character
next = lambda x: unichr(ord(x)+1)

def forms4(standard, isolated):
    """Register a harf. short-cut to add_forms"""
    final = next(isolated)
    initial = next(final)
    medial = next(initial)
    add_forms(standard, isolated, final, initial, medial, True, True)

def forms2(standard, isolated):
    """Register a harf that only has two forms. short-cut to add_forms"""
    final = next(isolated)
    initial = isolated
    medial = final
    add_forms(standard, isolated, final, initial, medial, True, False)

# Listing all arabic letters and their shapes

add_forms(None, None, None, None, None, False, False)
# Lam-Aleft
forms2(u'\uFEFB', u'\uFEFB')
forms2(u'\uFEF9', u'\uFEF9')
forms2(u'\uFEF7', u'\uFEF7')
forms2(u'\uFEF5', u'\uFEF5')
# Hamza groups
forms2(u'\u0622', u'\uFE81')
forms2(u'\u0623', u'\uFE83')
forms2(u'\u0624', u'\uFE85')
forms2(u'\u0625', u'\uFE87')
forms4(u'\u0626', u'\uFE89')
# Main letters
forms2(u'\u0627', u'\uFE8D')
forms4(u'\u0628', u'\uFE8F')
forms4(u'\u062A', u'\uFE95')
forms4(u'\u062B', u'\uFE99')
forms4(u'\u062C', u'\uFE9D')
forms4(u'\u062D', u'\uFEA1')
forms4(u'\u062E', u'\uFEA5')
forms2(u'\u062F', u'\uFEA9')
forms2(u'\u0630', u'\uFEAB')
forms2(u'\u0631', u'\uFEAD')
forms2(u'\u0632', u'\uFEAF')
forms4(u'\u0633', u'\uFEB1')
forms4(u'\u0634', u'\uFEB5')
forms4(u'\u0635', u'\uFEB9')
forms4(u'\u0636', u'\uFEBD')
forms4(u'\u0637', u'\uFEC1')
forms4(u'\u0638', u'\uFEC5')
forms4(u'\u0639', u'\uFEC9')
forms4(u'\u063A', u'\uFECD')
forms4(u'\u0641', u'\uFED1')
forms4(u'\u0642', u'\uFED5')
forms4(u'\u0643', u'\uFED9')
forms4(u'\u0644', u'\uFEDD')
forms4(u'\u0645', u'\uFEE1')
forms4(u'\u0646', u'\uFEE5')
forms4(u'\u0647', u'\uFEE9')
forms2(u'\u0648', u'\uFEED')
forms4(u'\u064A', u'\uFEF1')
# Letters that are not directly in the alphabet
forms2(u'\u0629', u'\uFE93')
forms2(u'\u0649', u'\uFEEF')
# tatweel
add_forms(u'\u0640', u'\u0640', u'\u0640', u'\u0640', u'\u0640', True, True)

