#mcandrew

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats

if __name__ == "__main__":
 
    
    binomPmf = scipy.stats.binom(100,0.06).pmf

    domain = np.arange(0,100,1)


    plt.style.use("fivethirtyeight")
    fig,ax = plt.subplots()

    ax.scatter(domain, binomPmf(domain), 10, alpha=0.70 ) 
    ax.plot(domain, binomPmf(domain), lw=2 )

    ax.set_xlim(0,25)

    ax.set_ylabel("Probability mass function",fontsize=10)
    ax.set_xlabel("Number of successes (out of 100 trials)",fontsize=10)

    ax.tick_params(size=2,direction="in")

    fig.set_tight_layout(True)
    plt.savefig("featured.png")
    plt.close()
    

    
