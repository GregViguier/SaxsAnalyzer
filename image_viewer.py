import matplotlib.pyplot as plt

import hdfReader


def plot_image(arr):
    fig = plt.figure(figsize=(5, 5), dpi=80, facecolor='w', edgecolor='w', frameon=True)
    imAx = plt.imshow(arr, origin='lower', interpolation='nearest')
    fig.colorbar(imAx, pad=0.01, fraction=0.1, shrink=1.00, aspect=20)


if __name__ == '__main__':
    file_name = r'/home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs'

    imageData = hdfReader.load_image_at_index(file_name, 'buffer_0044', 5)
    # Put it in the viewer
    plot_image(imageData)
    # Show it
    plt.show()
