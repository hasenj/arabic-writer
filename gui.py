"""
    Author: Hasen il Judy
    License: GPL v2
"""
import wx
from main import rtlize

def CopyText( text):
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
        wx.Frame.__init__(self, parent, id, title, size=(780, 700), style = style)

        font = self.GetFont()
        font.SetPointSize(14)
        font.SetFaceName("Arial")
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        self.SetFont(font)

        panel = wx.Panel(self)

        help_text_1 = wx.StaticText(panel, pos=(10, 10), 
                label=u'Write Here - اكتب هنا')
        inp = wx.TextCtrl(panel, pos=(40, 40), size=(700, 200))

        btn = wx.Button(panel, pos=(60, 500), size=(200, 80), label=u'Copy / نسخ')
        reset_btn = wx.Button(panel, pos=(270, 500), size=(200, 80), 
                label=u'Reset / مسح')
        quit_btn = wx.Button(panel, pos=(540, 500), size=(200, 80), 
                label=u'Quit / خروج')

        help_btn = wx.Button(panel, pos=(120, 600), size=(500, 40), 
                label=u'Help / تعليمات')

        help_text_arabic = wx.StaticText(panel, pos=(90, 280), size=(700, 100),
                label=u""" ثم اضغط زر النسخ, و بعدها يمكنك لصق النص في اي برنامج لا يدعم العربية """) 
        help_text_english = wx.StaticText(panel, pos=(50, 330), size=(700, 100),
                label=u""" Then press "Copy", and then go and paste it in a program that doesn't support Arabic properly """) 

        help_labels = [help_text_1, help_text_arabic, help_text_english]

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

app = wx.App(0)
MyFrame(None, -1, u'الرسام الحر')
app.MainLoop()

