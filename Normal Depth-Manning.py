# importamos primeramente los módulos a usar
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin

# definimos variables
n = 0.015
S0 = 0.025
Q = 9.26
B = 2

# definiendo la función para el cálculo del tirante normal
def flow(y):
    Q_estiamted = (1.49/n)*(S0**0.5)*((B*y)**(5/3))/((B+y)**(2/3))
    epsilon = np.abs(Q_estiamted - Q)
    return epsilon
y_optimum = fmin(flow,0.5) 

#veamos algunos detalles del cálculo
print(y_optimum)
