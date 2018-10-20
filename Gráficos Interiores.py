import matplotlib.pyplot as plt #importar módulo
import numpy as np
plt.ion() # Nos ponemos en modo interactivo 
plt.axes(facecolor='w') #crear ventana de gráfico con color de fondo
plt.plot(np.exp(np.linspace(0,10,100))) #linspace: secuencia de datos
plt.axes([0.2,0.55,0.3,0.3],facecolor='gray')#crear ventana de gráfico interior con color de fondo
plt.plot(np.sin(np.linspace(0,10,100)), 'b-o', linewidth = 2,color='blue')
