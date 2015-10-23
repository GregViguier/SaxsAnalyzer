import numpy as np

import matplotlib.pyplot as plt
import pyFAI.azimuthalIntegrator

import hdfReader

data = hdfReader.load_image_at_index(r'/home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs', 'buffer_0044', 5)

ai = pyFAI.AzimuthalIntegrator()

ai.set_wavelength(0.0007)
ai.set_pixel1(0.056)
ai.set_pixel2(0.056)

q, I, Sigma = ai.integrate1d(data, np, unit="q_nm^-1", error_model="poisson", polarization_factor=1.0)
plt.plot(q, I)
