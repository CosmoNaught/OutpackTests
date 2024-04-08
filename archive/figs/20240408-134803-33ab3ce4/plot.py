import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_distributions_from_csv(df):
    plt.figure(figsize=(12, 8))
    
    for column in df.columns:
        distribution_data = df[column].dropna()
        
        mean = np.mean(distribution_data)
        std = np.std(distribution_data)
        
        sns.histplot(distribution_data, kde=True, stat='density', label=f'{column} Mean: {mean:.2f}, Std: {std:.2f}')
    
    plt.title('Gaussian Distributions from CSV')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()