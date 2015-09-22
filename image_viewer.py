import numpy as np

from matplotlib.widgets import Cursor, Button
import matplotlib.pyplot as plt

import hdfReader

plt.rcParams['font.size'] = 8


class image_viewer(object):
    def __init__(self, z, x=None, y=None):
        """
        Shows a given array in a 2d-viewer.
        Input: z, an 2d array.
        x,y coordinters are optional.
        """
        if x == None:
            self.x = np.arange(z.shape[0])
        else:
            self.x = x
        if y == None:
            self.y = np.arange(z.shape[1])
        else:
            self.y = y
        self.z = z
        self.fig = plt.figure()
        # Doing some layout with subplots:
        self.fig.subplots_adjust(0.05, 0.05, 0.98, 0.98, 0.1)
        self.overview = plt.subplot2grid((8, 4), (0, 0), rowspan=7, colspan=2)
        self.overview.pcolormesh(self.x, self.y, self.z)
        self.overview.autoscale(1, 'both', 1)
        self.x_subplot = plt.subplot2grid((8, 4), (0, 2), rowspan=4, colspan=2)
        self.y_subplot = plt.subplot2grid((8, 4), (4, 2), rowspan=4, colspan=2)

        # Adding widgets, to not be gc'ed, they are put in a list:

        cursor = Cursor(self.overview, useblit=True, color='black', linewidth=2)
        but_ax = plt.subplot2grid((8, 4), (7, 0), colspan=1)
        reset_button = Button(but_ax, 'Reset')
        but_ax2 = plt.subplot2grid((8, 4), (7, 1), colspan=1)
        legend_button = Button(but_ax2, 'Legend')
        self._widgets = [cursor, reset_button, legend_button]
        # connect events
        reset_button.on_clicked(self.clear_xy_subplots)
        legend_button.on_clicked(self.show_legend)

    def show_legend(self, event):
        """Shows legend for the plots"""
        for pl in [self.x_subplot, self.y_subplot]:
            if len(pl.lines) > 0:
                pl.legend()
        plt.draw()

    def clear_xy_subplots(self, event):
        """Clears the subplots."""
        for j in [self.overview, self.x_subplot, self.y_subplot]:
            j.lines = []
            j.legend_ = None
        plt.draw()


if __name__ == '__main__':
    A = hdfReader.load_image_at_index(
        '/home/gregory/Work/Samples/NeXuS/ImageReducer/200Images/elisabeth_0043_2013-10-05_03-36-44.nxs',
        'R16-19iso_0043', 5)
    # Put it in the viewer
    fig_v2 = image_viewer(A)
    # Show it
    plt.show()
