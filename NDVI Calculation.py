from __future__ import division
from osgeo import gdal
from osgeo.gdalconst import*
import matplotlib.pyplot as plt
driver = gdal.GetDriverByName('GTiff')
file_name = "C:\LE07_L1TP_002071_20120211_20161204_01_T1_sr_band3.tif" #debes cargar el archivo ráster de la banda 3
dataset = gdal.Open(file_name, GA_ReadOnly)
geotransform = dataset.GetGeoTransform()
projection = dataset.GetProjection()
band3 = dataset.GetRasterBand(1).ReadAsArray()
dataset = None
file_name = "C:\LE07_L1TP_002071_20120211_20161204_01_T1_sr_band4.tif" #debes cargar el archivo ráster de la banda 4
dataset = gdal.Open(file_name, GA_ReadOnly)
band4 = dataset.GetRasterBand(1).ReadAsArray()
dataset = None
print(geotransform)
print(projection)
print(band3.dtype)
ndvi = (band4-band3)/(band4+band3)
plt.matshow(ndvi,cmap=plt.cm.jet, vmin=-1, vmax=1)
plt.colorbar(shrink=0.8)
plt.savefig("C:\NDVI\indice.png", dpi=1000) #debes crear una carpeta en el disco del sistema operativo


#Link de descarga de los archivos de banda: https://we.tl/t-DNgOFgGHte
