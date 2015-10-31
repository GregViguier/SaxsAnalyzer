import h5py

__author__ = 'GregViguier'


def open_file(file_name):
    result = h5py.File(file_name, 'r')
    return result


def load_image_at_index(file_name, entry_name, index):
    h5_file = open_file(file_name)
    root_dict = h5_file[entry_name]
    image_group = root_dict.get('image#' + str(index))
    image_data = image_group.__getitem__('data')
    return image_data.value
