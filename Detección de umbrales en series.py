plt.ion() 
x = np.arange(100) 
y = np.random.rand(100) 
plt.plot(x,y, color = 'black', label = '(x, f(x)’)
plt.plot(x[y > 0.9], y[y > 0.9], 'bo', label = 'f(x) > 0.9’) -> marcador azul 
plt.axhspan(0.9, 1, alpha = 0.1) -> borrar el área del gráfico
plt.ylim(0,1.2) 
plt.legend()
plt.title(u'Representación de (x, f(x))’) 
plt.xlabel('valores x
plt.ylabel('valores f(x)')
