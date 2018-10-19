# importar los módulos requeridos en este ejemplo
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

#generamos la malla de interpolación
X,Y = np.meshgrid(np.linspace(0,1,1000), np.linspace(0,1,1000)) #usaremos la función meshgrid de la librería numpy

#generamos el elemento grillado de precipitación
grid_rain = griddata((x,y), rain, (X, Y))

#Ahora graficamos
plt.clf()
plt.contourf(X,Y,grid_rain)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
