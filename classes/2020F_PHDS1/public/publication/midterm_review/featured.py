#mcandrew

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats

if __name__ == "__main__":

    ln = scipy.stats.lognorm(0.3,1).pdf

    domain = np.linspace(1,4,300)
    dens   = ln(domain)

    plt.style.use("fivethirtyeight")
    fig,ax = plt.subplots()

    ax.plot(domain,dens)
    ax.fill_between(domain,[0]*len(dens),dens,alpha=0.15)


    ax.fill_between([1.50,1.65],[0,0],[ln(1.50),ln(1.50)],alpha=0.55,color="red")
    ax.fill_between([1.65,1.75],[0,0],[ln(1.65),ln(1.65)],alpha=0.55,color="red")
    ax.fill_between([1.75,1.85],[0,0],[ln(1.75),ln(1.75)],alpha=0.55,color="red")
    ax.fill_between([1.85,2.00],[0,0],[ln(1.85),ln(1.85)],alpha=0.55,color="red")
    
    ax.set_xlabel(r"$Y$",fontsize=12)
    ax.set_ylabel(r"Density values for Y $f(Y=y)$",fontsize=12)

    ax.set_xticks([1,1.5,1.65,1.75,1.85,2.0,2.5,3,3.5,4])
    ax.set_xticklabels([1,1.5,1.65,1.75,1.85,2.0,2.5,3,3.5,4],rotation=90)

    yticks = [0] + [ ln(x) for x in [1.5,1.65,1.75,1.85] ]
    ax.set_yticks( yticks  )
    ax.set_yticklabels( ["{:.1f}".format(y) for y in yticks] )
    
    ax.tick_params(labelsize=8)

    fig.set_size_inches(7,3.5)
    fig.set_tight_layout(True)
    plt.savefig("featured.png")
    plt.close()
