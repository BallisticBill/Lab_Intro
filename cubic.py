from scipy import interpolate
import numpy as np
import matplotlib.pyplot as  plt

x = np.linspace(0,np.pi*2,10)
y = np.sin(x)
f = interpolate.interp1d(x, y,kind = 'cubic')
x_new =  np.linspace(0,np.pi*2,100)
y_new = f(x_new)
plt.title("Cubic Interpolation of sin(x)",fontsize=12)
plt.xlabel('Angle x (Radian)',fontsize=12)
plt.ylabel('sin(x)',fontsize=12)
plt.plot(x_new,y_new,'o')
plt.plot(x,y,'o')
plt.legend(['interpolated','input'])
plt.show()

x = np.linspace(0,1,10)
y = np.exp(-x)
f = interpolate.interp1d(x, y,kind = 'cubic')
x_new =  np.linspace(0,1,100)
y_new = f(x_new)
plt.title("Cubic Interpolation of exp(x)",fontsize=12)
plt.xlabel('x Values',fontsize=12)
plt.ylabel('exp(x)',fontsize=12)
plt.plot(x_new,y_new,'o')
plt.plot(x,y,'o')
plt.legend(['interpolated','input'])
plt.show()
