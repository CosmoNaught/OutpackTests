import numpy as np
import pandas as pd

def generate_gaussian_data(means, std_devs, sizes):
    all_data = []
    for mean, std, size in zip(means, std_devs, sizes):
        data = np.random.normal(loc=mean, scale=std, size=size)
        all_data.append(data)
    
    df = pd.DataFrame({f'Distribution_{i}': data for i, data in enumerate(all_data, start=1)})
    return df

means = [0, 10, 20] 
std_devs = [1, 2, 3]
sizes = [100, 100, 100] 

# Generate the data
df = generate_gaussian_data(means, std_devs, sizes)

# csv_filename = 'src\data\gaussian_distributions.csv'
# df.to_csv(csv_filename, index=False)
# print(f'Data saved to {csv_filename}')
