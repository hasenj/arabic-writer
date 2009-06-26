"""
    Author: Hasen il Judy
    License: GPL v2
"""
import forms
       
def iter_context(string):
    """Iterate over a string, returning a context, not just a letter
    
    @returns a tuple (before, current, after)
    
    On "edge" cases, the missing letter is returned as None
    """
    for i in range(len(string)):
        if i == 0:
            prev = None
        else:
            prev = string[i-1]
        if i + 1 == len(string):
            next = None
        else:
            next = string[i+1]
        curr = string[i]
        yield prev, curr, next

R, L, N = range(3)

def get_dir(letter):
    if forms.is_harf(letter): return R # Note: only checks for Arabic
    elif letter.isalpha(): return L # XXX: Test this, it should be the rest of unicode letters, not just English
    else: return N

def uni_segments(string):
    """ Break the string down into uni-directional segments.

    Put sequential R chars into a segment, 
    sequential L chars into a segment,
    and each N char into its own segment 
    """
    segments = [""]
    dir = N
    for char in string:
        old_dir = dir
        dir = get_dir(char)
        if dir == N:
            segments += [char] # New segment
        else:
            if dir == old_dir:
                segments[-1] += char # Append to current segment
            else:
                segments += [char] # New segment
    return segments
        
def shape(string):
    if not string: return ""
    return ''.join(forms.get_contextual_shape(*context) for context in iter_context(string))

def mirror(string):
    """Assumes a uni-directional segment"""
    if not string: return ""
    dir = get_dir(string[0])
    if dir == R:
        return string[::-1]
    return string

def rtlize(string):
    """Call this on a raw string, and it will process it"""
    segs = uni_segments(string)
    segs = [mirror(shape(seg)) for seg in segs]
    return ''.join(segs)

if __name__ == '__main__':
    print "Testing"
    print rtlize("hello")
    print rtlize("تجربة")

