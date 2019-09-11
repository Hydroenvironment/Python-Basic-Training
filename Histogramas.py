#Un histograma es un gráfico de barras donde se representa la ocurrencia de datos 
#(frecuencia) en intervalos definidos. Lo que hace plt.hist es dibujar el histograma de 
#un vector en función del número de intervalos (bins) que definamos:

plt.ion()
x = np.random.randn(10000) #vector de números aleatorios de una distribución normal 
plt.hist(x, bins = 20) #histograma en 20 intervalos del mismo ancho

#Para los gráficos de barras recurrimos a plt.bar :

import datetime as dt
prima = 600 + np.random.randn(5) * 10
fechas=(dt.date.today()-dt.timedelta(5))+dt.timedelta(1)*np.arange(5)
plt.axes((0.1, 0.3, 0.8, 0.6)) 
plt.bar(np.arange(5), prima)
plt.ylim(550,650)
plt.title('prima de riesgo’)
plt.xticks(np.arange(5), fechas, rotation = 45)


