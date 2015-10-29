import numpy as np
import matplotlib.pyplot as plt
import pyFAI.azimuthalIntegrator
import hdfReader
import time
import threading
import multiprocessing
from multiprocessing import Pool


plt.style.use('ggplot')

filename = r'/home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs'
entryname = 'buffer_0044'


def worker(index):
    data = hdfReader.load_image_at_index(filename, entryname, index)
    q, I, Sigma = ai.integrate1d(
        data, 1024, mask=mask, unit="q_A^-1", error_model="poisson",
        polarization_factor=None, method="cython")
    qValues[index] = q
    iValues[index] = I
    sValues[index] = Sigma
    return q, I, Sigma


class computeThread(threading.Thread):

    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index

    def run(self):
        data = hdfReader.load_image_at_index(filename, entryname, self.index)
        q, I, Sigma = ai.integrate1d(
            data, 1024, mask=mask, unit="q_A^-1", error_model="poisson",
            polarization_factor=None, method="cython")
        qValues[self.index] = q
        iValues[self.index] = I
        sValues[self.index] = Sigma

start_time = time.time()
qValues = [None] * 50
iValues = [None] * 50
sValues = [None] * 50
threads = [None] * 50

# Load MASK
mask = np.genfromtxt("GV2.txt", delimiter=";", dtype=int)
ai = pyFAI.AzimuthalIntegrator()

ai.set_wavelength(0.0000000001033)
ai.set_dist(1.499)
ai.set_pixel1(0.000004)
ai.set_pixel2(0.000004)
ai.set_poni2(0)
ai.set_poni1(0)

# with Pool(processes=8) as pool:
#     mapResult = pool.map(worker, range(49))

# for t in mapResult:
# 	plt.plot(t[0], t[1])


for x in range(0, 49):
    #threads[x] = multiprocessing.Process(target=worker, args=(x,))
    threads[x] = computeThread(x)
    threads[x].start()

for x in range(0, 49):
	threads[x].join()
	# plt.errorbar(qValues[x], iValues[x], sValues[x])
	plt.plot(qValues[x], iValues[x])

print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
