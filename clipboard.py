"""
    Found on http://mrlauer.wordpress.com/2007/12/31/python-and-the-clipboard/
    With modifications

    Lincense unknown
"""

try:
    import win32clipboard as wcb

    def setcbtext(text):
        wcb.OpenClipboard()
        wcb.EmptyClipboard()
        wcb.SetClipboardText(text)
        wcb.CloseClipboard()

except ImportError, e:
    # try gtk.  If that doesn't work, just let the exception go
    import gtk

    def setcbtext(text):
        cb = gtk.Clipboard()
        cb.set_text(text)
        cb.store()

if __name__ == '__main__':
    setcbtext("copy wil ya?")

