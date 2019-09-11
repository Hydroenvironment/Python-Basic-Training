# importamos primeramente los módulos a usar
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin

# definimos variables
n = 0.015 #coeficiente de rugosidad de Manning
S0 = 0.025 # Pendiente de fondo=línea de energía en flujo uniforme
Q = 9.26 #Caudal que escurre por el canal
B = 2 #Base del canal

# definiendo la función para el cálculo del tirante normal
def flow(y):
    Q_estimated = (1.49/n)*(S0**0.5)*((B*y)**(5/3))/((B+y)**(2/3))
    epsilon = np.abs(Q_estimated - Q)
    return epsilon
y_optimum = fmin(flow,0.1) 

#veamos algunos detalles del cálculo
print(y_optimum)
