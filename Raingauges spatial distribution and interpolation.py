# import required modules
import numpy as np
import matplotlib.pyplot as plt

#generar ubicaciones y valores de lluvia
x = np.random.rand(10)
y = np.random.rand(10)
rain = 10*np.random.rand(10)

#graficar la distribución espacial
plt.scatter(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('ubicación_estaciones.png')

#Ahora interpolaremos
from scipy.interpolate import griddata # usaremos la función griddata de la librería scipy.interpolate
>>> #generate the desired grid, where rainfall is to be interpolated
>>> X,Y = np.meshgrid(np.linspace(0,1,1000), np.linspace(0,1,1000)) #usaremos la función meshgrid de la librería numpy
>>>
>>> #perform the gridding
>>> grid_rain = griddata((x,y), rain, (X, Y))
