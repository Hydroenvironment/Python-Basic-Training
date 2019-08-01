##Importamos Librerias##
import numpy as np
import matplotlib.pyplot as plt

#Creamos la nube de puntos
x = np.array([0, 1, 2, 3])
y = np.array([1, 1.5, 1.8, 2.6])

#Construimos una matriz
A = np.vstack([x, np.ones(len(x))])
A = A.T #Hacemos su traspuesta

#Obtenemos parametros de la recta
m, c = np.linalg.lstsq(A, y)[0]
print ("La recta obtenida es:  y = " + str(m) + "x + " + str(c))


plt.plot(x, y, 'o', label='Nube puntos', markersize=15)
plt.plot(x, m*x + c, 'r', label='Regresion Lineal')
plt.legend()
plt.show()

raw_input("Enter para salir")
