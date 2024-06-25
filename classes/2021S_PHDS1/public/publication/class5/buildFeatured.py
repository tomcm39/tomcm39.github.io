#mcandrew

import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    x = np.random.normal(0,1,100)
    b0 = 1.
    b1 = 2.
    b2 = -1.
    y = b0 + b1*x + b2*x**2 + np.random.normal(0,2,100)

    y = y.reshape(-1,1)
    X = np.hstack((np.ones((100,1)),x.reshape(-1,1),(x**2).reshape(-1,1)))
    
    def SSE(y,X,beta):
        return sum((y - X.dot(beta))**2)
    
    betaPredict = np.array([1,2,-1]).reshape(-1,1)
    SSEs = []
    for ep in np.random.normal(0,0.5,100):
        SSEval = SSE(y,X,betaPredict+ep)
        SSEs.append((ep,SSEval))

    eps,sses = zip(*sorted(SSEs))
    fig,ax = plt.subplots()
    ax.plot(eps,sses,'ro',alpha=0.60)
    ax.plot(eps,sses,'k-',alpha=0.75)

    ax.tick_params(direction='in',size=2.)
    ax.set_xlabel(r'True $\beta$ + $\epsilon$')
    ax.set_ylabel(r'SSE')

    plt.savefig('featured.png')
    plt.close()
