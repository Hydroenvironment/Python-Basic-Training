import numpy as np
time = np.linspace(0,100,21) # create time variable
time
array([ 0., 5., 10., 15., 20., 25., 30., 35., 40.,
       45., 50., 55., 60., 65., 70., 75., 80., 85.,
       90., 95., 100.])
rainfall = np.random.rand(21) # generate rainfall
rainfall
array([ 0.08155645, 0.88821997, 0.33355457, 0.49600859, 0.6315054 ,
        0.0722053 , 0.06165701, 0.96105307, 0.56483934, 0.5194715 ,
        0.35780167, 0.98950575, 0.67866578, 0.31274527, 0.80022389,
        0.53321842, 0.82370443, 0.73212013, 0.77039599, 0.06392391,
        0.53481488])
import matplotlib.pyplot as plt
plt.bar(time,rainfall)
plt.xlabel('Time')
plt.ylabel('Incremental rainfall')
plt.savefig('rain.png') #buscar en la ruta C:\Users\monte\.spyder-py3 ó en C:\Users\monte\.spyder-py2
