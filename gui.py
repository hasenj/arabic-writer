import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(250, 180))

        vbox = wx.BoxSizer(wx.VERTICAL)
        inp = wx.TextCtrl(self)
        oup = wx.TextCtrl(self)

        self.Centre()
        self.Show(True)

app = wx.App(0)
MyFrame(None, -1, u'الرسم الحر')
app.MainLoop()

