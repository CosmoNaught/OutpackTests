import matplotlib.pyplot as plt
import seaborn as sns
import orderly
import pandas as pd

# Function to plot the distributions
def plot_distributions(all_data, means, std_devs):
    plt.figure(figsize=(12, 8))
    for i, data in enumerate(all_data):
        sns.histplot(data, kde=True, stat='density', label=f'Mean: {means[i]}, Std: {std_devs[i]}')
    plt.title('Gaussian Distributions')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

orderly.dependency(None, "latest(name == 'data')",
                {"data.csv" : "gaussian_distributions.csv"})

data = pd.read_csv("gaussian_data.csv")
