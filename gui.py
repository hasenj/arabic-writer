import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(250, 180))

        vbox = wx.BoxSizer(wx.VERTICAL)
        inp = wx.TextCtrl(vbox, -1)
        oup = wx.TextCtrl(vbox, -1)

        self.Centre()
        self.Show(True)

app = wx.App(0)
MyFrame(None, -1, 'Free(dom) Writer') 
app.MainLoop()

