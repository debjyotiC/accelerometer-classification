import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

win_size = 20

df = pd.read_csv('data/Accelerometer.csv').drop(columns=['Timestamp'])
x, y, z = df['X'].to_numpy(dtype='float64'), df['Y'].to_numpy(dtype='float64'), df['Z'].to_numpy(dtype='float64')
t = df['Milliseconds'].to_numpy(dtype='float64')  # time


def window_rms(a, window_size=2):
    return np.sqrt(sum([a[window_size - i - 1:len(a) - i] ** 2 for i in range(window_size - 1)]) / window_size)


x_rms, y_rms, z_rms = window_rms(x, window_size=win_size), \
                      window_rms(y, window_size=win_size), window_rms(z, window_size=win_size)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_rms, y_rms, z_rms, color='blue', s=60)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.view_init(30, 185)
plt.legend()
plt.show()
