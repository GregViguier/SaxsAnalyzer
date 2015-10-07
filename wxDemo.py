__author__ = 'GregViguier'

import wx
import os
from numpy import arange, sin, pi

import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(550, 450))
        self.figure = plt.figure(figsize=(5, 5), dpi=80, facecolor='w', edgecolor='w', frameon=True)
        self.axes = self.figure.add_subplot(111)
        self.control = FigureCanvas(self, -1, self.figure)
        self.CreateStatusBar()

        # FILE MENU
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "Open File", "Open a file")
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.slider = wx.Slider(self, value=50, minValue=0, maxValue=100, style=wx.SL_LABELS)
        self.sizer2.Add(self.slider, 1, wx.GROW)
        self.Bind(wx.EVT_SCROLL_CHANGED, self.OnImageChange, self.slider)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 0, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.GROW)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        # MENU BAR
        menubar = wx.MenuBar()
        menubar.Append(filemenu, "File")
        self.SetMenuBar(menubar)
        self.Show(True)

    def OnExit(self, e):
        self.Close(True)

    def OnOpen(self, e):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)

    def OnImageChange(self, e):
        print str(self.slider.GetValue())


app = wx.App(False)
frame = MainWindow(None, "Small Editor")
frame.draw()
app.MainLoop()
