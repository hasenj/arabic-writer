﻿"""
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
        self.SetFont(font)

        panel = wx.Panel(self)

        inp_lbl = wx.StaticText(panel, pos=(10, 10), 
                label=u'Write Here - اكتب هنا')
        inp = wx.TextCtrl(panel, pos=(40, 40), size=(700, 200))

        btn = wx.Button(panel, pos=(60, 540), size=(200, 80), label=u'Copy / نسخ')
        reset_btn = wx.Button(panel, pos=(270, 540), size=(200, 80), label=u'Reset / مسح')
        quit_btn = wx.Button(panel, pos=(540, 540), size=(200, 80), label=u'Quit / خروج')

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

