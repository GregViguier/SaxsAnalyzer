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
    data = load_image_at_index(
        'home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs', 'buffer_0044',
        5)
    # load_image_stack('test.h5')
