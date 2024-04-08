import matplotlib.pyplot as plt
import orderly
import pandas as pd
from plot import plot_distributions_from_csv
import os
import sys
from importlib import import_module

figs_dir = os.path.dirname(os.path.abspath(__file__))

if figs_dir not in sys.path:
    sys.path.append(figs_dir)

plot = import_module('plot')

orderly.dependency(None, "latest(name == 'data')",
                {"data.csv" : "gaussian_distributions.csv"})

data = pd.read_csv("data.csv")

plt.savefig('Gaussian Distribution.png')
plot.plot_distributions_from_csv(data)