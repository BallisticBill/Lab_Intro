import matplotlib.pyplot as plt
import numpy as np
def extrapolate(p0,p1,x):
    x0,y0 = p0
    x1,y1 = p1
    return y0 + (x-x0)/(x1-x0) * (y1-y0)



x = [i/10 for i in range(11)]
f = [np.exp(j) for j in x]
y=[]
for i in [1.1,1.2,1.3]:
    y.append(extrapolate((x[8],f[8]),(x[9],f[9]),i))
x_new=[1.1,1.2,1.3]

plt.title('Linear Extrapolation of exp(x) Without Packages')
plt.xlabel("x values")
plt.ylabel("exp(x)")
plt.plot(x,f,'o')
plt.plot(x_new,y,'x')
plt.plot(x_new,np.exp(x_new),'>')
plt.legend(['input values','extrapolated values','actual values'])
plt.show()
#with package
from numpy import polyfit

x = [i/10 for i in range(11)]
f = [np.exp(j) for j in x]
res  = polyfit(x,f,1)
p = np.poly1d(res)
f_new=[p(1.1),p(1.2),p(1.3)]
plt.title('Linear Extrapolation of exp(x)')
plt.xlabel("x values")
plt.ylabel("exp(x)")
plt.plot(x,f,'o')
plt.plot(x_new,np.exp(x_new),'<')
plt.plot(x_new,f_new,'x')
plt.legend(['input values','actual values','extrapolated values'])
plt.show()

x = [i/10 for i in range(11)]
f = [np.exp(j) for j in x]
res  = polyfit(x,f,3)
p = np.poly1d(res)
x_new=[1.1,1.2,1.3]
f_new=[p(1.1),p(1.2),p(1.3)]
plt.title('Cubic Extrapolation of exp(x)')
plt.xlabel("x values")
plt.ylabel("exp(x)")
plt.plot(x,f,'o')
plt.plot(x_new,np.exp(x_new),'<')
plt.plot(x_new,f_new,'x')
plt.legend(['input values','actual values','extrapolated values'])
plt.show()






