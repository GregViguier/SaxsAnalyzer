import numpy as np
import matplotlib.pyplot as plt
import pyFAI.azimuthalIntegrator
import hdfReader
import time
import threading
import multiprocessing


plt.style.use('ggplot')


def worker(index):
    data = hdfReader.load_image_at_index(
        r'/home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs',
        'buffer_0044', index)
    q, I, Sigma = ai.integrate1d(
        data, 1024, mask=mask, unit="q_A^-1", error_model="poisson",
        polarization_factor=None, method="cython")
    qValues[index] = q
    iValues[index] = I
    sValues[index] = Sigma


class computeThread(threading.Thread):

    def __init__(self, index, mask):
        threading.Thread.__init__(self)
        self.index = index
        self.mask = mask

    def run(self):
        data = hdfReader.load_image_at_index(
            r'/home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs',
            'buffer_0044', x)
        q, I, Sigma = ai.integrate1d(
            data, 1024, mask=self.mask, unit="q_A^-1", error_model="poisson",
            polarization_factor=None, method="cython")
        qValues[x] = q
        iValues[x] = I
        sValues[x] = Sigma

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
# ai.set_mask(mask)
ai.set_poni2(0)
ai.set_poni1(0)


# pool = multiprocessing.Pool(processes=8)
# pool.map(worker, range(49))

for x in range(0, 49):
    #threads[x] = multiprocessing.Process(target=worker, args=(x,))
    threads[x] = computeThread(x, mask)
    threads[x].start()


for x in range(0, 49):
    threads[x].join()
#     plt.errorbar(qValues[x], iValues[x], sValues[x])
#     plt.plot(qValues[x], iValues[x])

print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
