#mcandrew

import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
 
    
    fig,ax = plt.subplots()

    domy = np.linspace(-5,5,15)
    domt = np.linspace(-5,5,15)

    Y,T = np.meshgrid(domy,domt)

    def d(y,t):
        return y*np.sin(t)

    f = d(Y,T)
    
    ax.quiver(T,Y,np.ones(T.shape),f)

    def sol(t,init):
        t0,y0 = init
        k = y0*np.exp(np.cos(t0))
        return k*np.exp(-1*np.cos(t))

    for _ in range(15):
        tStart = -5+5*np.random.random()
        domt = np.linspace(tStart,5,100)
        ys = sol(domt,[tStart,-1+2*np.random.random()])
        ax.plot( domt,ys,'r-'  )

    ax.set_ylabel("y(t)")
    ax.set_xlabel("t")

    plt.savefig('sol1.png')
    plt.close()
