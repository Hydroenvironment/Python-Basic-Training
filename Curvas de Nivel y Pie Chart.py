import matplotlib.pyplot as plt
import numpy as np
plt.ion() 
visitas = [43.97, 9.70, 7.42, 6.68, 3.91, 3.85, 
3.62, 3.43, 3.16, 3.04]
# Definimos un vector con el % de visitas del top ten de países 
visitas = np.append(visitas, 100. - np.sum(visitas))
paises = [u'España', u'México', 'Chile', 'Argentina’, 'Colombia’, 
'Ecuador', u'Perú', 'USA', 'Islandia', 'Venezuela', 'Otros’]
explode = [0, 0, 0, 0, 0, 0, 0, 0.2, 0.2, 0, 0]
plt.pie(visitas, labels = paises, explode = explode)
plt.title(u'Porcentaje de visitas por país')


Ahora nos apoyaremos de plt.contour y plt.contourf: 

plt.ion()
x = np.random.rand(20)
y = np.random.rand(20)
t = np.random.rand(20)*3000
plt.tricontourf(x, y, t)
plt.tricontour(x, y, t, colors = 'k’)
plt.scatter(x, y)



