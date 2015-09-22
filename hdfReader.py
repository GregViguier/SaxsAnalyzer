import h5py
import fnmatch
__author__ = 'gregory'


def open_file(file_name):
    result = h5py.File(file_name, 'r')
    return result


def load_image_stack(file_name):
    h5_file = open_file(file_name)
    rootName = 'R16-19iso_0043'
    root = h5_file[rootName]

    imagesGroup = fnmatch.filter(root, "image*")
    for group in imagesGroup:
        print group


# def load_image_stack:

if __name__ == "__main__":
    load_image_stack('/home/gregory/Work/Samples/NeXuS/ImageReducer/200Images/elisabeth_0043_2013-10-05_03-36-44.nxs')
    # load_image_stack('test.h5')
