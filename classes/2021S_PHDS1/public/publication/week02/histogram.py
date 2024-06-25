#mcandrew

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
 

    d0 = np.random.normal(0,1,1000)
    d1 = np.random.normal(0.5,0.5,1000)

    plt.style.use('fivethirtyeight')
    
    fig,ax = plt.subplots()
    hist = ax.hist(list(d0)+list(d1), 50)

    bins,counts = hist[1], hist[0]

    ax.set_xlabel("Data values",fontsize=10)
    ax.set_ylabel("Count",fontsize=10)

    idx = 20
    ax.text(bins[idx]*0.99,counts[idx]
            ,"Awesomeness",ha='right',va='bottom',weight='bold')

    fig.set_tight_layout(True)
    plt.savefig('featured.png')
    plt.close()
