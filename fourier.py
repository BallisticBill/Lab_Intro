import math
from scipy import integrate

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

a0,an,bn = fourier_coeff(lambda x: x**2,(0,2*math.pi),5)
print(" Numerically Generated Fourier Coefficients :\n")
print((a0))
for i, n in zip(an,range(1,len(an))):
    print(str((math.pi**2 * i))+'cos('+str(n/math.pi)+'*pi*t)'+'/pi**2 + ')
print()
for j, n in zip(bn,range(1,len(bn))):
    print(str((math.pi * j))+'sin('+str(n/math.pi)+'*pi*t)'+'/pi + ')
print()
import sympy as sym
from sympy import fourier_series
from sympy.abc import t
s = fourier_series(t**2, (t, 0, 2*math.pi),finite=True)

print("Fourier Coefficients Generated Analytically\n")
print((s.a0))
for i in range(1,5):
    print(str(s.an.coeff(i))+'+ ')
print()
for i in range(1,5):
    print(str(s.bn.coeff(i))+'+ ')
 