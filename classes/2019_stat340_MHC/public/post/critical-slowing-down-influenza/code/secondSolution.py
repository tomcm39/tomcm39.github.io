#mcandrew

import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
 
    
    fig,axs = plt.subplots(1,2)

    domy = np.linspace(-5,5,15)
    domt = np.linspace(-5,5,15)

    Y,T = np.meshgrid(domy,domt)


    n=0
    for r in [0,5]:
        ax = axs[n]
        n+=1

        def d(y,t,r):
            row,col = y.shape
            r = r*np.ones((row,col))
            return r-y**2
        f = d(Y,T,r)

        ax.quiver(T,Y,np.ones(T.shape),f)

        def sol(t,init,r):
            t0,y0 = init
            r=np.sqrt(r)
            k = (r+y0)/(r-y0)*np.exp(-2*r*t0)
            return r*(k*np.exp(2*r*t) -1)/(k*np.exp(2*r*t) +1) 

        ax.plot([0],[-np.sqrt(r)],'ro',mfc='none')
        ax.plot([-5,5],[-np.sqrt(r)]*2,'r-')

        ax.plot([0],[np.sqrt(r)],'ro')
        ax.plot([-5,5],[np.sqrt(r)]*2,'r-')

        for _ in range(25):
            tStart = -5+5*np.random.random()
            domt = np.linspace(tStart,5,100)
            print(-5+10*np.random.random())
            ys = sol(domt,[tStart,-2.+6*np.random.random()],5)
            ax.plot( domt,ys,'r-'  )

        ax.set_ylabel("y(t)")
        ax.set_xlabel("t")

    plt.savefig('sol2.png')
    plt.close()
