import numpy as np
# generate data
x = np.linspace(0,10)
y = 1 + 2*x - 3*x**2 + 15*np.random.randn(50) #aquí deberían ir los datos obtenidos experimentalmente
# fit the polynomial
z = np.polyfit(x,y,2) # aquí se hace el ajuste polinómico con regresión,cambiando el exponente
print(z)

import matplotlib.pyplot as plt
# evaluate polynomial
p = np.poly1d(z)
z_true = np.array([-3, 2, 1]) # coefficient of true polynomial
p_true = np.poly1d(z_true) # true polynomial
# plot
plt.plot(x, y,'.r', label='noisy data')
plt.plot(x, p_true(x), label='True curve')
plt.plot(x, p(x), label='Fitted curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
