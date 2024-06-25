#mcandrew

import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def mm2inch(x):
    return x/25.4

if __name__ == "__main__":

    x = np.random.normal(0,3,150)
    y = np.sin(x) + np.random.normal(0,0.5,150)

    fig,axs = plt.subplots(1,2)

    ax = axs[0]
    ax.plot(x,y,'ko',alpha=0.50)
    ax.set(xlabel=r'$X$',ylabel=r'$Y$')
    ax.tick_params(size=2.,direction='in')
    
    ax = axs[1]
    ax.plot(np.sin(x),y,'ko',alpha=0.50)
    ax.set(xlabel=r'$\sin(X)$',ylabel=r'$Y$')
    ax.tick_params(size=2.,direction='in')
    
    fig.set_tight_layout(True)
    fig.set_size_inches(1.3*mm2inch(183),mm2inch(183)/1.6)
    plt.savefig('featured.png')
    plt.close()
