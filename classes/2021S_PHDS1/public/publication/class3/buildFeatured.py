#mcandrew

import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import image

def mm2inch(x):
    return x/25.4

if __name__ == "__main__":

    x = np.random.normal(0,1,150)
    y = 3.0*x + 1.0*x**2 + -1.5*x**3 + 0.2 + np.random.normal(0,3.0,150)
    fig,ax = plt.subplots()

    ax.plot(x,y,'ko',alpha=0.40)

    b3,b2,b1,b0 = np.polyfit(x,y,3)
    minx,maxx = np.min(x),np.max(x)

    domX = np.linspace(minx,maxx,100)
    ax.plot(domX,b0 + b1*domX + b2*domX**2 + b3*domX**3,'r-')

    ax.tick_params(direction='in')
    
    w = mm2inch(189.*0.90)
    fig.set_size_inches(w,w/1.6)
    fig.set_tight_layout(True)
    plt.savefig('featured.png')
    plt.close()
