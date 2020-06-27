from __future__ import division
from osgeo import gdal
from osgeo.gdalconst import*
import numpy as np
import matplotlib.pyplot as plt
driver = gdal.GetDriverByName('GTiff')
file_name = "C:\\TEMPORAL\\LE07_L1TP_002071_20120211_20161204_01_T1_sr_band3.tif" #debes cargar el archivo ráster de la banda 3
dataset = gdal.Open("C:\\TEMPORAL\\LE07_L1TP_002071_20120211_20161204_01_T1_sr_band3.tif",1)
geotransform = dataset.GetGeoTransform()
projection = dataset.GetProjection()
band3 = dataset.GetRasterBand(1).ReadAsArray()
dataset = None
file_name = "C:\\TEMPORAL\\LE07_L1TP_002071_20120211_20161204_01_T1_sr_band4.tif" #debes cargar el archivo ráster de la banda 4
dataset = gdal.Open("C:\\TEMPORAL\\LE07_L1TP_002071_20120211_20161204_01_T1_sr_band4.tif",1)
band4 = dataset.GetRasterBand(1).ReadAsArray()
dataset = None
print(geotransform)
print(projection)
print(band3.dtype)
ndvi = (band4-band3)/(band4+band3)
#En caso hayan divisiones entre cero: "Divide by zero encountered"
#np.seterr(divide='ignore')
#mask = (band4+band3)==0
#ndvi = np.zeros(band3.shape)
#ndvi[  mask ] = -99
#ndvi[ ~mask ] = ((band4-band3)/(band4+band3))[ ~mask ]
plt.matshow(ndvi,cmap=plt.cm.jet, vmin=-1, vmax=1)
plt.colorbar(shrink=0.8)
#Acceso a archivos .tif: https://drive.google.com/drive/folders/1KX5c4gp1NY2M-Yi8Ztdlc7GukdsC9rU1?usp=sharing
