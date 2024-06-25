#mcandrew

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import norm

if __name__ == "__main__":
 

    plt.style.use("fivethirtyeight")
    
    fig,ax = plt.subplots()

    domain    = np.linspace(-3,3,1000)
    normalpdf = norm(0,1).pdf(domain)
    normalpdfHalf = norm(0,1).pdf(domain[:500])
    

    ax.plot( domain, normalpdf, 'k-', alpha=0.80, lw=2. )
    ax.fill_between( domain[:500], 0,normalpdfHalf, color="k", alpha=0.40 )

    ax.set_ylabel("Probability density function", fontsize=10)
    ax.set_xlabel("Values",fontsize=10)

    ax.tick_params(which='both',labelsize=6,direction='in')

    fig.set_tight_layout(True)
    plt.savefig("featured.png")
    plt.close()



    
