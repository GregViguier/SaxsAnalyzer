import numpy as np
import matplotlib.pyplot as plt
import pyFAI.azimuthalIntegrator
import hdfReader
import time
import concurrent.futures
from matplotlib.font_manager import FontProperties
from bokeh.models import HoverTool, BoxSelectTool
from bokeh.plotting import figure, show, output_file, vplot, output_server
from bokeh.palettes import Spectral11

filename = r'/home/gregory/Dropbox/elisabeth_0044_2013-10-05_04-10-19.nxs'
entryname = 'buffer_0044'


def worker(index):
    data = hdfReader.load_image_at_index(filename, entryname, index)
    q, I, Sigma = ai.integrate1d(data, 1024,
                                 mask=mask, unit="q_A^-1",
                                 error_model="poisson",
                                 polarization_factor=None,
                                 method="cython")
    return q, I

start_time = time.time()

# Load MASK
mask = np.genfromtxt("GV2.txt", delimiter=";", dtype=int)
ai = pyFAI.AzimuthalIntegrator()

ai.set_wavelength(0.0000000001033)
ai.set_dist(1.499)
ai.set_pixel1(0.000004)
ai.set_pixel2(0.000004)
ai.set_poni2(0)
ai.set_poni1(0)

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    mapResult = executor.map(worker, range(49))


output_file("legend.html", title="legend.py example")
#output_server("line")
tools = "pan,wheel_zoom,box_zoom,reset,resize"

p = figure(title="CircleGathering", tools=tools)

mypalette = Spectral11[0:49]

for index, t in enumerate(mapResult):
    p.line(t[0], t[1], legend="Radial Intensity " +
           str(index), line_color=mypalette[index % 11])

print("--- %s seconds ---" % (time.time() - start_time))

show(p)
