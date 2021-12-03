import numpy as np
def lerp(p1,p2,n):
    resx=[];resy=[]
    x1,y1 = p1
    x2,y2 = p2
    t=0
    while(t<1):
        resx.append(x2*t-x1*(t-1))
        resy.append(y2*t-y1*(t-1))
        t+=(1/n)
    return resx,resy



def interpolate(coord_x,coord_y,n):
    resx=[]; resy=[]
    x,y=(0,0)
    for i in range(len(coord_x)-1):
        x,y = lerp((coord_x[i],coord_y[i]),(coord_x[i+1],coord_y[i+1]),n)
        resx+=x
        resy+=y
    return resx,resy

def plot_sin(plt):
    x = np.linspace(0,np.pi*2,10)
    y = np.sin(x)
    xval,yval = interpolate(x,y,10)
    plt.title('Linear Interpolation Without Packages')
    plt.xlabel('input values (t)',fontsize=12)
    plt.ylabel('sin(t)',fontsize=12)
    plt.legend(['interpolated value','input values'],loc =  "upper center")
    plt.plot(xval,yval,'o')
    plt.plot(x,y,'o')
    plt.legend(['interpolated value','input values'],loc =  "upper center")
    plt.show()

def  plot_exp(plt):
    x1 = np.linspace(0,1,10)
    y1 = np.exp(-x1)
    xval, yval =interpolate(x1,y1,10)
    plt.title('Linear Interpolation Without Packages')
    plt.xlabel('input values (t)',fontsize=12)
    plt.ylabel('exp(-t)',fontsize=12)
    plt.plot(xval,yval,'o')
    plt.plot(x1,y1,'o')
    plt.legend(['interpolated value','input values'],loc =  "upper center")
    plt.show()

def plot_sin_numpy(plt):
    x = np.linspace(0,np.pi*2,10)
    y = np.sin(x)
    y_new = []
    x_new = []
    for p in range(len(x)-1):
        x1 = [x[p+1]*(i/10) - x[p]*(i/10 -1) for i in range(10)]
        for i in x1:
            y_new.append(np.interp(i,x,y))
            x_new.append(i)
    plt.title('Linear Interpolation With Numpy')
    plt.xlabel('input values (t)',fontsize=12)
    plt.ylabel('sin(t)',fontsize=12)
    plt.plot(x_new,y_new,'o')
    plt.plot(x,y,'o')
    plt.legend(['interpolated value','input values'],loc =  "upper center")
    plt.show()

def  plot_exp_numpy(plt):
    x = np.linspace(0,1,10)
    y = np.exp(-x)
    y_new = []
    x_new = []
    for p in range(len(x)-1):
        x1 = [x[p+1]*(i/10) - x[p]*(i/10 -1) for i in range(10)]
        for i in x1:
            y_new.append(np.interp(i,x,y))
            x_new.append(i)
    plt.title('Linear Interpolation With Numpy')
    plt.xlabel('input values (t)',fontsize=12)
    plt.ylabel('exp(-t)',fontsize=12)
    plt.plot(x_new,y_new,'o')
    plt.plot(x,y,'o')
    plt.legend(['interpolated value','input values'],loc =  "upper center")
    plt.show()
def main():
    import matplotlib.pyplot as plt
    plot_sin(plt)
    plot_exp(plt)
    plot_sin_numpy(plt)
    plot_exp_numpy(plt)




if __name__=="__main__":
    main()