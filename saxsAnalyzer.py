import numpy as np
import pyFAI.azimuthalIntegrator
import hdfReader
import concurrent.futures
from itertools import repeat


def getdata(nb_images=49):
    # Load MASK
    mask = np.genfromtxt("GV2.txt", delimiter=";",
                         dtype=int)
    ai = pyFAI.AzimuthalIntegrator()
    ai.set_wavelength(0.0000000001033)
    ai.set_dist(1.499)
    ai.set_pixel1(0.000004)
    ai.set_pixel2(0.000004)
    ai.set_poni1(0)
    ai.set_poni2(0)

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    mapresult = executor.map(
        worker, *(range(nb_images), repeat(ai), repeat(mask)))
    return mapresult


def worker(index, ai, mask):
    filename = r'/home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs'
    data = hdfReader.load_image_at_index(filename, 'buffer_0044', index)
    q, I, Sigma = ai.integrate1d(data, 1024,
                                 mask=mask, unit="q_A^-1",
                                 error_model="poisson",
                                 polarization_factor=None,
                                 method="cython")
    return q, I

if __name__ == '__main__':
    result = getdata()
