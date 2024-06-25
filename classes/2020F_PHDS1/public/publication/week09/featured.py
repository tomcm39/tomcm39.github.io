#mcandrew

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    a = np.random.gamma(1,2,500)
    b = np.random.gamma(2,1,250)


    plt.style.use("fivethirtyeight")
    fig,ax = plt.subplots()

    sns.distplot(a)
    sns.distplot(b)

    ax.set_xlim(0,10)

    plt.savefig("featured.png")

    plt.close()
    

    
