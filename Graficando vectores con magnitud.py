plt.ion()
lon = np.arange(15) - 10.
lat = np.arange(15) + 30.
lon, lat = np.meshgrid(lon, lat)
u = np.random.randn(15 * 15)
v = np.random.randn(15 * 15)
colores = ['k','r','b','g','c','y','gray’]
plt.title('Flechas de un viento un poco loco') plt.xlabel('longitud')
plt.ylabel('latitud')
plt.quiver(lon, lat, u, v, color = colores)
