import numpy as np
time = np.linspace(0,100,21) # create time variable
rainfall = np.random.rand(21) # generate rainfall
import matplotlib.pyplot as plt
plt.bar(time,rainfall)
plt.xlabel('Time')
plt.ylabel('Incremental rainfall')
plt.savefig('rain.png') #buscar en la ruta C:\Users\monte\.spyder-py3 ó en C:\Users\monte\.spyder-py2
