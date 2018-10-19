from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#generamos datos meteorológicos
Rn = 150+100*np.random.rand(100) # lower bound = 150, upper boun = 250 #Radiación neta
T = 25+3*np.random.randn(100) # mean = 25, std = 3 #Temperatura en grados celsius
Rh = 0.2+0.6*np.random.rand(100) # lower bound = 0.2, upper boun = 0.8 #
u2 = 3+np.random.randn(100) # mean = 3, std = 1 #velocidad del viento

#define constants
rho_w = 997; rho_a = 1.19; p = 101.1e3; z2 = 2
z0 = 0.03e-2; k = 0.4; Cp = 1005

#Aplicamos el método de balance energético para estimar la evaporación
lv = (2500-2.36*T)*1000 # multiplicado por mil para convertir de KJ/kg a J/kg
Er = 200/(lv*997) # tasa de evaporación usando el balance energético
Er *= 1000*86400 # convertimos las unidades de m/s a mm/día

B = 0.622*k**2*rho_a*u2/(p*rho_w*(np.log(z2/z0))**2)
e_s = 611*np.exp(17.27*T/(237.3+T)) # presión de vapor de saturación
e_a = Rh*e_s #presión de vapor
Ea = B*(e_s-e_a)  # Tasa de evaporación usando el método aerodinámico
Ea *= 1000*86400 # convertimos las unidades de m/s a mm/día

gamma = Cp*p/(0.622*lv) # ya que las difusividades de vapor kh/kw = 1, se simplifican en la ecuación.
delta = 4098*e_s/(237.3+T)**2 #gradiente de la curva de presión de vapor de saturación
w = delta/(delta+gamma)

#Ahora calculamos la evaporación combinando el balance energético y método aerodinámico
E = w*Er + (1-w)*Ea

plt.clf()
plt.subplot(2,2,1)
plt.plot(Er)
plt.xlabel('Time')
plt.ylabel('Er')
plt.subplot(2,2,2)
plt.plot(Ea)
plt.xlabel('Time')
plt.ylabel('Ea')
plt.subplot(2,2,3, facecolor='y')

#Porque no usar plt.subplot(2,2,3, axisbg='y')?? pasó algo con la librería??
#revisar : https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html

plt.plot(E)
plt.xlabel('Time')
plt.ylabel('E')
plt.subplot(2,2,4, facecolor='g')
plt.plot(w)
plt.xlabel('Time')
plt.ylabel('Er/E')
plt.savefig('E.png')
