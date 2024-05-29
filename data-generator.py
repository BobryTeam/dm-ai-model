import numpy as np
import pandas as pd

# Simulated data generation
num_components = 1
num_data_points = 50000
cpu_usage = np.random.rand(num_data_points)
memory_usage = np.random.rand(num_data_points)
network_traffic = np.random.rand(num_data_points)
predict = []

for i in range(num_data_points):
    metrics_limit = 0
    res = 0.
    if cpu_usage[i] >= 0.9 or memory_usage[i] >= 0.9 or network_traffic[i] >= 0.9:
        res = 1.5 + 0.2 * (0.5 - np.random.rand())

    elif cpu_usage[i] < 0.5 or memory_usage[i] < 0.5 or network_traffic[i] < 0.5:
        res = 0.5 + 0.2 * (0.5 - np.random.rand())

    else:
        res = 1
    predict.append(res)


df = pd.DataFrame({
    'cpu': cpu_usage,
    'memory': memory_usage, 
    'traffic': network_traffic, 
    'predict': predict,
})

df.to_csv('test-data.csv', index=False)
