from __future__ import division
import numpy as np
# define the variables
theta_e = 0.486
psi = 16.7
K = 0.65
S_e = 0.3
t = 1

#calcular dtheta
dtheta = (1-S_e)*theta_e

# Primera iteración para F
F_old = K*t
epsilon = 1
F = []
while epsilon > 1e-4:
    F_new = psi*dtheta * np.log(1+F_old/(psi*dtheta)) + K*t
    epsilon = F_new - F_old
    F_old = F_new
    F.append(F_new)
#El valor iterado de F se almacena utilizando el método de adjuntar (append)
#append adjunta el array por un solo elemento y coloca la variable de entrada en ella.

#Ahora graficamos
import matplotlib.pyplot as plt
plt.plot(F,'-ok')
plt.xlabel('Number of iteration',fontsize=25)
plt.ylabel('F',fontsize=20)
plt.savefig('F.png')
