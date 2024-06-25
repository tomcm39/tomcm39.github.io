#mcandrew

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":


    x = np.random.normal(size=500)
    y = 1+0.5*x + np.random.normal(0,1,500)

    d = pd.DataFrame({"x":x,"y":y})

    plt.style.use("fivethirtyeight")
    fig,ax = plt.subplots()
    sns.lmplot(x="x",y="y",data=d)

    fig.set_size_inches(7.2,7.2/1.6)
    fig.set_tight_layout(True)
    plt.savefig("featured.png")
    plt.close()
    

