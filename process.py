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
    """Get the direction of a character, either Right, Left, or Neutral.

    Neutral characters don't have an intrinsic direction on their own, it depends
    on their context
    """
    if letter is None: return N
    if letter.isdigit(): return L
    if forms.is_harf(letter): return R # Note: only checks for Arabic
    elif letter.isalpha(): return L # XXX: Test this, it should be the rest of unicode letters, not just English
    else: return N

def uni_segments(string):
    """Break the string down into uni-directional segments.

    Put sequential R chars into a segment, 
    sequential L chars into a segment,
    and each N char into its own segment 
    """
    segments = [""]
    dir = R
    prev = R
    for context in iter_context(string):
        _, char, _ = context
        real_prev, dir, next = [get_dir(c) for c in context]
        if ((dir == prev) or 
            (dir == N and next in [N, prev])):
            segments[-1] += char # Append to current segment
            dir = prev
        else:
            segments += [char] # New segment
        prev = dir
    return segments
        
def get_segment_direction(string):
    """Find the direction of a uni-directional segment
    by finding the first non-N character, or returning N
    """
    for char in string:
        dir = get_dir(char)
        if dir in [L,R]:
            return dir
    return N

def shape_plain(string):
    """Substitute Arabic letters with a form that represents their shape
    depending on their context.

    Only works with plain text that has no harakat
    """
    if not string: return ''
    return ''.join(forms.get_contextual_shape(*context) for context in iter_context(string))

def shape(string):
    """Substitute Arabic letters with a form that represents their shape
    depending on their context.

    wrapper around shape_plain that adds support for harakat
    """
    if not string: return ''
    harakat_info, plain = forms.split_harakat(string)
    plain = shape_plain(plain)
    return forms.put_harakat(harakat_info, plain)

def mirror_brackets(string):
    """Mirror brackets"""
    swap = { '(':')', '[':']', '{':'}', ')':'(', ']':'[', '}':'{' }
    return ''.join((swap.get(char,char) for char in string))

def mirror_segment(string):
    """Assumes string is a uni-directional segment; reverses an R string"""
    if not string: return ""
    dir = get_segment_direction(string)
    if dir in [R,N]:
        string = mirror_brackets(string)
        return string[::-1]
    return string

def mirror(string):
    """Mirror a whole string, by dividing it into segments first"""
    segs = uni_segments(string)
    segs = [mirror_segment(seg) for seg in segs]
    return ''.join(segs[::-1])

def func_lines(string, func):
    """Apply a function to multiple lines in reverse"""
    return '\r\n'.join([func(line) for line in string.splitlines()])
    
def rtlize_line(string):
    string = forms.fuse(string)
    string = shape(string)
    string = mirror(string)
    return string

def rtlize(string):
    """Call this on a raw string, and it will process it"""
    return func_lines(string, rtlize_line)

def unshape(string):
    """convert shaped characters back to standard characters"""
    return ''.join(forms.get_std_shape(char) for char in string)

def restore_line(string):
    """Restore a string by reverse-processing it"""
    string = mirror(string)
    string = unshape(string)
    string = forms.unfuse(string)
    return string

def restore(string):
    """Reverse Processing"""
    return func_lines(string, restore_line)

if __name__ == '__main__':
    print "Testing"
    print rtlize("hello")
    print rtlize("تجربة")

