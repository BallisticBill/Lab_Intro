import matplotlib.pyplot as  plt
import numpy as np

t=np.linspace(0,np.pi*2)

f1 = np.sin(t)
f2 = np.sin(2*t)
f3 = np.cos(t)

plt.title("Plot of sin(t), sin(2t) and cos(t)")
plt.xlabel("Angle (radians)")
plt.ylabel("Value of function")
plt.plot(t,f1,marker='o')
plt.plot(t,f2,marker='o')
plt.plot(t,f3,marker='o')
plt.legend(['sin(t)','sin(2t)','cos(t)'])
plt.show()
 
#3D plot
def surface_plot(func,title):
    x = np.outer(np.linspace(-np.pi, np.pi, 50), np.ones(50))
    y = x.copy().T
    z = func(x,y)
    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    ax.plot_surface(x, y, z, cmap ='viridis', edgecolor ='green')
    ax.set_title(title)
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('f(x,y)')
    plt.show()
#heatmap
def heatmap(func,title):
    x = np.outer(np.linspace(-np.pi, np.pi, 50), np.ones(50))
    y = x.copy().T
    z = func(x,y)
    z = z[:-1, :-1]
    z_min, z_max = -np.abs(z).max(), np.abs(z).max()
    fig, ax = plt.subplots()
    c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
    ax.set_title(title)
    ax.axis([x.min(), x.max(), y.min(), y.max()])
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    fig.colorbar(c, ax=ax)
    plt.show()

surface_plot(lambda x, y: y*np.sin(x),'3D Plot of f(x,y) = ysin(x)')
surface_plot(lambda x, y: x**2 * y**2, '3D Plot of f(x,y) = x^2 y^2')

heatmap(lambda x, y: y*np.sin(x),'Heatmap of f(x,y) = ysin(x)')
heatmap(lambda x, y: x**2 * y**2, 'Heatmap of f(x,y) = x^2 y^2')