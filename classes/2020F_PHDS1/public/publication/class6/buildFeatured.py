#mcandrew

import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def polyFit(X,y,degree):
    poly_reg = PolynomialFeatures(degree=degree)
    X_poly = poly_reg.fit_transform(X)
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, y)

    ax.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='red',alpha=0.80)



if __name__ == "__main__":

    b0=-1
    b1=1.5
    b2=-1.25
    b3=0.70
    b4=1.
    b5=2.

    x = np.random.normal(0,3,100)
    y = b0 + b1*x + b2*x**2 + b3*x**3 + b5*np.sin(x)+np.random.normal(0,40,100)

    dta = pd.DataFrame({'x':x,'y':y})
    dta = dta.sort_values('x')

    fig,ax = plt.subplots()
    ax.plot(dta.x,dta.y,'ko',alpha=0.50)

    X = dta.iloc[:,0].values.reshape(-1,1)
    y = dta.y.values.reshape(-1,1)

    for degree in np.arange(1,20,5):
        polyFit(X,y,degree)
    
    ax.tick_params(direction='in',size=2.)
    ax.set_xticks([])
    ax.set_yticks([])
        
    plt.savefig('./featured.png')
    plt.close()
    
    
