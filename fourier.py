import math
from scipy import integrate
from numpy import linspace

def simp_integrate(func,range,iter=1000000):
    a,b = range
    delta = (b-a)/iter
    x, i= (a,True)
    res= func(a)+func(b)
    while x<b:
        x+=delta
        res+= (4*i + 2*(not i))*func(x)             # using the fact that boolean values are either 1 or 0 to avoid branching
        i = not i
    return delta/3 * res

def fourier_coeff(func,limit,n):
    l,u = limit
    a,b = ([],[])
    c = 2/(u-l)
    a_0 = c/2 * simp_integrate(func, (l,u))
    for i in range(1,n+1):
        a_n = c * simp_integrate(lambda x: func(x)*math.cos(c*i*x*math.pi),(l,u))
        b_n = c * simp_integrate(lambda x: func(x)*math.sin(c*i*x*math.pi),(l,u))
        a.append(a_n)
        b.append(b_n)
    return a_0,a, b

def fourier_func(val, x, limit):
    a0, an, bn = val
    l,u = limit
    L = (u-l)/2
    sinval, cosval = (0,0)
    for i in range(len(an)):
        sinval += bn[i]*math.sin((i+1)*math.pi*x/L)
        cosval += an[i]*math.cos((i+1)*math.pi*x/L)
    return a0+ sinval + cosval


import sympy as sym
from sympy import fourier_series
from sympy import plot as sym_plot
from sympy.abc import t

s = fourier_series(t**2, (t, 0, 2*math.pi),finite=True)
s1 = s.truncate(n=10)
import matplotlib.pyplot as plt
arr = linspace(0,2*math.pi,1000)
pack_y = [s1.evalf(subs={t:i}) for i in arr]
y = [i**2 for i in arr]
plt.title('Fourier Series With Packages',fontsize=12)
plt.xlabel("x",fontsize=12)
plt.ylabel("x^2",fontsize=12)
plt.plot(arr,pack_y)
plt.plot(arr,y)
plt.legend(['Fourier series of x^2','x^2'],)
plt.show()
coeff = fourier_coeff(lambda x : x**2,(0,2*math.pi),10)
res = [fourier_func(coeff,i,(0,2*math.pi)) for i in arr]
plt.title('Fourier Series Without Packages',fontsize=12)
plt.xlabel("x",fontsize=12)
plt.ylabel("x^2",fontsize=12)
plt.plot(arr,res,color='r')
plt.plot(arr,y,color='g')
plt.legend(['Fourier series of x^2','x^2'],)
plt.show()
 
