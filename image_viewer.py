import matplotlib.pyplot as plt

import hdfReader


def plotImage(arr):
    fig = plt.figure(figsize=(5, 5), dpi=80, facecolor='w', edgecolor='w', frameon=True)
    imAx = plt.imshow(arr, origin='lower', interpolation='nearest')
    fig.colorbar(imAx, pad=0.01, fraction=0.1, shrink=1.00, aspect=20)

if __name__ == '__main__':
    imageData = hdfReader.load_image_at_index(
        '/home/gregory/Work/Samples/NeXuS/ImageReducer/200Images/elisabeth_0043_2013-10-05_03-36-44.nxs',
        'R16-19iso_0043', 5)
    # Put it in the viewer
    plotImage(imageData)
    # Show it
    plt.show()
