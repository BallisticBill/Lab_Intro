import matplotlib.pyplot as plt

x = []
y = []
err = []

file =  open('data.txt','r')
for l in file:
    vals = l.split(' ')
    x.append(float(vals[0]))
    y.append(float(vals[1]))
    err.append(float(vals[2]))
plt.title('Data Plotting and Error Bar')
plt.xlabel('x axis',fontsize=14)
plt.ylabel('y axis',fontsize=14)
plt.plot(x,y,'o')
plt.errorbar(x,y, yerr = err,label='error in y',fmt='x')
plt.legend(loc ='upper left')
plt.show()
