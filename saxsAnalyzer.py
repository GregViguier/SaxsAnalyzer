import numpy as np
import matplotlib.pyplot as plt
import pyFAI.azimuthalIntegrator
import hdfReader

ai = pyFAI.AzimuthalIntegrator()

# DATA
data = hdfReader.load_image_at_index(
    r'/home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs',
    'buffer_0044', 5)


# MASK
foxtrotmask = np.genfromtxt("GV2.txt", delimiter=";", dtype=int)
mask = foxtrotmask

ai.set_wavelength(0.0000000001033)
ai.set_dist(1.499)
ai.set_pixel1(0.000004)
ai.set_pixel2(0.000004)
ai.set_mask(mask)
ai.set_poni2(680)
ai.set_poni1(850)

ai.set_poni2(0)
ai.set_poni1(0)

print ai
q, I, Sigma = ai.integrate1d(
    data, 1448, unit="q_nm^-1", error_model="poisson",
    polarization_factor=1.0, method="numpy")

plt.errorbar(q, I, Sigma)
plt.show()
