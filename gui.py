"""
    Author: Hasen il Judy
    License: GPL v2
"""
import wx
from main import rtlize

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        style = wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, parent, id, title, size=(750, 700), style = style)

        panel = wx.Panel(self)

        inp = wx.TextCtrl(panel, pos=(10, 10), size=(700, 200))
        oup = wx.TextCtrl(panel, pos=(10, 220), size=(700, 200))
        oup.SetEditable(False)

        btn = wx.Button(panel, pos=(20, 450), size=(200, 80), label=u'نسخ')

        def process(evt):
            oup.SetValue( rtlize(inp.GetValue()) )
            evt.Skip()

        inp.Bind(wx.EVT_KEY_DOWN, process)
        inp.Bind(wx.EVT_KEY_UP, process)

        def copy(evt):
            oup.SelectAll()
            oup.Copy()
            oup.SetSelection(0,0)

        btn.Bind(wx.EVT_BUTTON, copy)

        self.Centre()
        self.Show(True)

app = wx.App(0)
MyFrame(None, -1, u'المهئ الحر')
app.MainLoop()

