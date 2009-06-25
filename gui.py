import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(950, 580))

        panel = wx.Panel(self)

        inp = wx.TextCtrl(panel, pos=(10, 10), size=(700, 200))
        oup = wx.TextCtrl(panel, pos=(10, 220), size=(700, 200))

        self.Centre()
        self.Show(True)

app = wx.App(0)
MyFrame(None, -1, u'المهئ الحر')
app.MainLoop()

