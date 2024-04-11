import matplotlib.pyplot as plt
import orderly
import pandas as pd
import os
import sys
from plot import plot_distributions_from_csv

def main():

    data = pd.read_csv("data.csv")

    plot_distributions_from_csv(data)
    plt.savefig('Gaussian Distribution.png')

    plt.show()

if __name__ == "__main__":
    orderly.dependency(None, "latest(name == 'data')",
                    {"data.csv" : "gaussian_distributions.csv"})
    main()