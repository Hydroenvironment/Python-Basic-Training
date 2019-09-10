#VEjemplo de crear dos gráficos en una misma ventana:
plt.ion() #Nos ponemos en modo interactivo 
plt.subplot(1,2,1) #Una fila y dos columnas
plt.plot((1,2,3,4,5)) 
plt.subplot(1,2,2) #Una fila y dos columnas 
plt.plot((5,4,3,2,1))

#Ahora daremos unas “letras” más en nuestros gráficos:
plt.figure('valores por defecto')
plt.suptitle('Titulo valores por defecto')
plt.plot((1,2,3,4,5), label = 'por defecto')
plt.legend(loc = 2)
plt.rc('lines', linewidth = 2)
plt.rc('font', size = 18) #Mayor tamaño desde ahora
plt.figure('valores modificados')
plt.suptitle('Titulo valores modificados')
plt.plot((1,2,3,4,5),label = u'linea más ancha y letra más grande')
plt.legend(loc = 2)

#Ahora podremos embeber un área de gráfico dentro de otra:
plt.ion()
plt.axes()
plt.plot(np.exp(np.linspace(0,10,100)))
plt.axes([0.2,0.55,0.3,0.3], facecolor = 'gray')
plt.plot(np.sin(np.linspace(0,10,100)), 'b-o', linewidth = 2)

#Veamos ahora un gráfico de doble eje vertical:
plt.ion()
plt.plot(np.arange(100), 'b')
plt.xlabel('Valores de x')
plt.ylabel(u'Línea azul')
plt.twinx() 
plt.plot(np.exp(np.linspace(0,5,100)), 'g')
plt.ylabel(u'Línea verde')
plt.xlim(-10,110)


#Funciones útiles:
#plt.delaxes()-> borrar el área del gráfico
#plt.cla() -> borrar el contenido que hay en el área del gráfico 
#plt.box() -> No aparecerá la 'caja' donde se dibuja el gráfico
#plt.box() -> Volverá a aparecer la 'caja‘
