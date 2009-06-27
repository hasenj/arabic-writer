"""
    Author: Hasen il Judy
    License: GPL v2
"""
import wx
from process import rtlize

language = 'arabic'

t_text = dict(
        arabic = dict(
            copy = u'نسخ',
            reset = u'مسح',
            quit = u'خروج',
            help = u'تعليمات',
            help_info = u'اكتب اي شيء في مربع النصوص ثم اضغط زر النسخ و بعدها السق النص في اي برنامج لا يدعم اللغة العربية',
            ),
        english = dict(
            copy = 'Copy',
            reset = 'Reset',
            quit = 'Quit',
            help = 'Help',
            help_info = '''Write some Arabic text in the text box, press 'Copy', then paste in a program that doesn't support Arabic''',
                   )
        )

def get_text(name):
    return t_text[language][name]

def CopyText(text):
    """Set text into the system clipboard"""
    ok = False
    if wx.TheClipboard.Open():
        wx.TheClipboard.SetData(wx.TextDataObject(text))
        wx.TheClipboard.Close()
        ok = True
    return ok

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        style = wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, parent, id, title, size=(780, 650), style = style)

        font = self.GetFont()
        font.SetPointSize(14)
        font.SetFaceName("Arial")
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        self.SetFont(font)

        panel = wx.Panel(self)

        inp = wx.TextCtrl(panel, pos=(40, 40), size=(700, 330))

        btn = wx.Button(panel, pos=(60, 400), size=(200, 80), label=get_text("copy"))
        reset_btn = wx.Button(panel, pos=(270, 400), size=(200, 80), 
                label=get_text("reset"))
        quit_btn = wx.Button(panel, pos=(540, 400), size=(200, 80), 
                label=get_text("quit"))
        help_btn = wx.Button(panel, pos=(150, 500), size=(500, 40), 
                label=get_text("help")) 
        help_text = wx.StaticText(panel, pos=(50, 560), size=(700, 150),
                label=get_text("help_info"))
        help_labels = [help_text]

        def toggle_help(evt=None):
            for label in help_labels:
                label.Show(not label.IsShown())
        help_btn.Bind(wx.EVT_BUTTON, toggle_help)
        toggle_help()

        def copy(evt):
            rtl = rtlize(inp.GetValue())
            copied = CopyText(rtl)
        btn.Bind(wx.EVT_BUTTON, copy)

        def reset(evt):
            inp.SelectAll()
            inp.Clear()
            inp.SetSelection(0,0)
        reset_btn.Bind(wx.EVT_BUTTON, reset)

        def quit(evt):
            self.Close()
        quit_btn.Bind(wx.EVT_BUTTON, quit)

        self.Centre()
        self.Show(True)

def main():
    app = wx.App(0)
    MyFrame(None, -1, u'الرسام الحر')
    app.MainLoop()

if __name__ == '__main__': main()

