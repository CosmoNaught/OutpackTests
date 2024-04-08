import matplotlib.pyplot as plt
import orderly
import pandas as pd
from plot_distribution import plot_distributions_from_csv

orderly.dependency(None, "latest(name == 'data')",
                {"data.csv" : "gaussian_distributions.csv"})

data = pd.read_csv("data.csv")

plt.savefig('Gaussian Distribution.png')
plot_distributions_from_csv(data)