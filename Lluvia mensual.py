import matplotlib.pyplot as plt
import numpy as np
plt.ion() 
import calendar
dias = [np.array(calendar.mdays)[0:i].sum() + 1 for i in np.arange(12)+1] 
meses = calendar.month_name[1:13]
plt.axes([0.1,0.2,0.8,0.65])
plt.plot(np.arange(1,366),np.random.rand(365), label = 'valores al azar') 
plt.xlim(-5,370) 
plt.ylim(0,1.2) 
plt.legend() 
plt.title(u'Ejemplo de título') 
plt.suptitle(u'Ejemplo de título superior') 
plt.minorticks_on() 
plt.xticks(dias, meses, size = 'small', color = 'b', rotation = 45) 
plt.xlabel(u't (días)') 
plt.ylabel('Media diaria')
