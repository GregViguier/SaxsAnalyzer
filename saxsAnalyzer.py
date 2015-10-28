import numpy as np
import matplotlib.pyplot as plt
import pyFAI.azimuthalIntegrator
import hdfReader
import time

start_time = time.time()
# Load MASK
mask = np.genfromtxt("GV2.txt", delimiter=";", dtype=int)
ai = pyFAI.AzimuthalIntegrator()

ai.set_wavelength(0.0000000001033)
ai.set_dist(1.499)
ai.set_pixel1(0.000004)
ai.set_pixel2(0.000004)
ai.set_mask(mask)
ai.set_poni2(0)
ai.set_poni1(0)


for x in range(0, 49):
    # DATA
    data = hdfReader.load_image_at_index(
        r'/home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs',
        'buffer_0044', x)

    q, I, Sigma = ai.integrate1d(
        data, 1024, unit="q_nm^-1", error_model="poisson",
        polarization_factor=None, method="cython")
    plt.errorbar(q, I, Sigma)

print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
