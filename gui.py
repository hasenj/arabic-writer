"""
    Author: Hasen il Judy
    License: GPL v2
"""
import wx
import os
import webbrowser
from process import rtlize

language = 'arabic'

t_text = dict(
        arabic = dict(
            title = u'الرسام الحر',
            copy = u'نسخ',
            reset = u'مسح',
            quit = u'خروج',
            help = u'تعليمات',
            help_doc = 'help_arabic.html',
            ),
        english = dict(
            title = 'The Free Ressam (Er Ressam il Hur)',
            copy = 'Copy',
            reset = 'Reset',
            quit = 'Quit',
            help = 'Help',
            help_doc = 'help_english.html',
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

        inp = wx.TextCtrl(panel, pos=(40, 40), size=(700, 330), style=wx.TE_MULTILINE)

        btn = wx.Button(panel, pos=(60, 400), size=(200, 80), label=get_text("copy"))
        reset_btn = wx.Button(panel, pos=(270, 400), size=(200, 80), 
                label=get_text("reset"))
        quit_btn = wx.Button(panel, pos=(540, 400), size=(200, 80), 
                label=get_text("quit"))
        help_btn = wx.Button(panel, pos=(150, 500), size=(500, 40), 
                label=get_text("help")) 

        def show_help(evt=None):
            help_doc = get_text('help_doc')
            webbrowser.open(os.path.join('docs', help_doc))
        help_btn.Bind(wx.EVT_BUTTON, show_help)

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
    MyFrame(None, -1, get_text('title'))
    app.MainLoop()

if __name__ == '__main__': main()

