import numpy as np
import matplotlib.pyplot as plt
time = np.linspace(0,100,21) # create time variable
rainfall = np.random.rand(21) # generate rainfall
cum_rainfall = np.cumsum(rainfall)
plt.clf()
plt.plot(time,cum_rainfall)
plt.xlabel('Time')
plt.ylabel('Cummulative rainfall')
plt.savefig('cum_rain.png') #buscar el archivo en la ruta C:\Users\monte\.spyder-py3 ó C:\Users\monte\.spyder-py2
