#mcandrew

import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def polyFit(X,y,degree,color):
    poly_reg = PolynomialFeatures(degree=degree)
    X_poly = poly_reg.fit_transform(X)
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, y)

    ax.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color=color,alpha=0.01)

def generateDataSet():
    x = np.random.uniform(-6,6,100)
    y = np.sin(x) + np.random.normal(0,1.75,100)
    
    dta = pd.DataFrame({'x':x,'y':y})
    dta = dta.sort_values('x')

    X = dta.iloc[:,0].values.reshape(-1,1)
    y = dta.y.values.reshape(-1,1)
    return X,y

if __name__ == "__main__":

    fig,ax = plt.subplots()

    xs = np.linspace(-6,6,500)
    ax.plot(xs,np.sin(xs),'k-')
    
    trainingSets = 500
    degree2color = {1:'r',6:'b',16:'c',21:'g'}
    for t in range(trainingSets):
        X,y = generateDataSet()
        for degree in np.arange(1,21,5):
            if degree==11:
                continue
            polyFit(X,y,degree,degree2color[degree])
    ax.tick_params(direction='in',size=2.)
    ax.set_xticks([])
    ax.set_yticks([])
    sns.despine(bottom=True,top=True,left=True,right=True)
    
    I = 8.5
    fig.set_size_inches(I,I/1.6)
    plt.savefig('./featured.png')
    plt.close()
 

    
