import random as rnd 
import matplotlib.pyplot as plt 
import numpy as np

def generate_gaussian(length):
    res=[]
    for i in range(length):
        res.append(rnd.gauss(0,1))
    return res

def histogram(list):
    fig,ax = plt.subplots(1,1)
    xval = np.linspace(-4,4,200)
    ax.text(-4, 40000, r'$\mu=0,\ \sigma=1$')
    ax.hist(list,bins=xval)
    ax.set_title("histogram of result")
    ax.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ax.set_xlabel('marks')
    ax.set_ylabel('no. of students')
    plt.show()

def main():
    val=generate_gaussian(3000000)
    histogram(val)





if __name__=="__main__":
    main()
