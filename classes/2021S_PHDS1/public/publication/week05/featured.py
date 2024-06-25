#mcandrew

import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    x = np.random.normal(0,1,1000)

    plt.style.use("fivethirtyeight")

    fig, ax = plt.subplots()
    ax.plot(x,lw=2.)
    ax.set(xlabel="Observations",ylabel="Outcomes")
    ax.text(0.99,0.99,r"$X \sim N(0,1)$",ha="right",va="top",transform=ax.transAxes)

    ax.tick_params(direction="in",size=2.)

    fig.set_tight_layout(True)
    plt.savefig("featured.png")
    plt.close()
