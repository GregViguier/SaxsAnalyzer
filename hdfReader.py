import h5py

__author__ = 'GregViguier'


def open_file(file_name):
    result = h5py.File(file_name, 'r')
    return result


def load_image_at_index(file_name, root_name, index):
    h5_file = open_file(file_name)
    root_dict = h5_file[root_name]
    image_group = root_dict.get('image#' + str(index))
    image_data = image_group.__getitem__('data')
    return image_data.value

if __name__ == "__main__":
    load_image_at_index(
        '/home/gregory/Work/Samples/NeXuS/ImageReducer/200Images/elisabeth_0043_2013-10-05_03-36-44.nxs',
        'R16-19iso_0043', 5)
    # load_image_stack('test.h5')
