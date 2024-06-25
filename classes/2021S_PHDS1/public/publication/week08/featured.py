#mcandrew

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats

if __name__ == "__main__":
 
    ms = [-1,1]
    ss = [ 1,2]

    d = {"group":[],"value":[]}
    for j in range(5*10**3):
        
        sample0 = np.random.normal(ms[0],ss[0])
        d["group"].append(0)
        d["value"].append(sample0)
        
        sample1 = np.random.normal(ms[1],ss[1])
        d["group"].append(1)
        d["value"].append(sample1)
 
        dif = sample0 - sample1
        d["group"].append(2)
        d["value"].append(dif)

    d = pd.DataFrame(d)

    plt.style.use("fivethirtyeight")
    
    fig,ax = plt.subplots()
    sns.stripplot( x="group",y="value", data=d, alpha=0.50,size=2 )
    
    ax.set_xlabel("")
    ax.set_ylabel("")

    ax.set_xticklabels(["G0","G1","Diff."],fontsize=12)

    ax.tick_params(labelsize=10)
    
    plt.savefig("featured.png")
    plt.close()
       
            
            
    







    
