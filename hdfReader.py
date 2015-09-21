import h5py

__author__ = 'gregory'


def open_file(file_name):
    f = h5py.File('/home/gregory/' + file_name, 'r')
    return f


def load_image_stack(file_name):
    h5_file = open_file(file_name)
    group1 = h5_file['group1']
    dset1 = group1.get('dset1')
    print dset1.shape


# def load_image_stack:

if __name__ == "__main__":
    load_image_stack('test.h5')
