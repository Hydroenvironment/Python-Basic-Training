import matplotlib.pyplot as plt
import numpy as np
import scipy as sp #debemos de importar scipy

x = np.random.rand(5)
y = np.random.rand(5)
pet = 2+2*np.random.rand(5)
rbfi = sp.interpolate.Rbf(x, y, pet)

xi = np.linspace(0,1)
yi = np.linspace(0,1)
XI, YI = np.meshgrid(xi,yi) # gridded locations
di = rbfi(XI, YI) # interpolated values
plt.imshow(di, extent=(0,1,0,1), origin='lower')
plt.scatter(x,y, color='k')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis((0,1,0,1))
plt.savefig('rbf.png')
