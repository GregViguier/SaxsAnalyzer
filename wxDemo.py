__author__ = 'GregViguier'

import wx

import matplotlib

import hdfReader

matplotlib.use('WXAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(550, 450))

        # SLIT THE WINDOW IN 2
        self.sp = wx.SplitterWindow(self)

        # INIT IMAGE VIEWER
        self.p1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.figure = plt.figure(figsize=(5, 5), dpi=80, facecolor='w', edgecolor='w', frameon=True)
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.p1, -1, self.figure)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Hide()

        # SLIDER + BUTTON
        self.p2 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.zoom_button = wx.Button(self.p2, -1, "Play", size=(40, 20), pos=(60, 10))
        self.zoom_button.Bind(wx.EVT_BUTTON, self.play)
        self.slider = wx.Slider(self.p2, value=0, minValue=0, maxValue=50, style=wx.SL_LABELS)
        self.Bind(wx.EVT_SCROLL_CHANGED, self.OnImageChange, self.slider)

        # LAYOUT LOWER PANEL
        self.box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.box_sizer.Add(self.slider, 1, wx.EXPAND)
        self.box_sizer.Add(self.zoom_button, 1, wx.GROW)
        self.p2.SetSizer(self.box_sizer)

        self.sp.SplitHorizontally(self.p1, self.p2, 470)
        self.Show(True)

        self.imAx = plt.imshow(self.load_data(0), origin='lower', interpolation='nearest', cmap=plt.get_cmap('jet'))

    def zoom(self, event):
        self.canvas.toolbar.zoom()


    def play(self, event):
        ani = animation.FuncAnimation(self.figure, self.plot_image, xrange(0, 50), interval=0, blit=True)

    def plot_image(self, index):
        print index
        image_data = self.load_data(index)
        self.imAx.set_array(image_data)
        # self.figure.colorbar(imAx, pad=0.01, fraction=0.1, shrink=1.00, aspect=20)
        # self.canvas.draw()
        return image_data

    def load_data(self, index):
        file_name = r'/home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs'
        image_data = hdfReader.load_image_at_index(file_name, 'buffer_0044', index)
        return image_data

    def OnImageChange(self, e):
        self.plot_image(self.slider.GetValue())



app = wx.App(False)
frame = MainWindow(None, "Small Editor")
app.MainLoop()
