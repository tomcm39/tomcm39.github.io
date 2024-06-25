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

    x = np.random.normal(0,1,100)
    y = 1.6*x + 0.2 + np.random.normal(0,1.2,100)
    fig,ax = plt.subplots()

    ax.plot(x,y,'ko',alpha=0.40)

    b1,b0 = np.polyfit(x,y,1)
    minx,maxx = np.min(x),np.max(x)
    ax.plot([minx,maxx],[b0+minx*b1,b0+maxx*b1],'r-')

    ax.tick_params(direction='in')
    
    w = mm2inch(189.*0.90)
    fig.set_size_inches(w,w/1.6)
    fig.set_tight_layout(True)
    plt.savefig('featured.png')
    plt.close()
