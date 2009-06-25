import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        style = wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, parent, id, title, size=(950, 580), style = style)

        panel = wx.Panel(self)

        inp = wx.TextCtrl(panel, pos=(10, 10), size=(700, 200))
        oup = wx.TextCtrl(panel, pos=(10, 220), size=(700, 200))

        self.Centre()
        self.Show(True)

app = wx.App(0)
MyFrame(None, -1, u'المهئ الحر')
app.MainLoop()

