import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import seaborn as sns

df = pd.read_csv('IrisDataset.csv')

class Histogram():
    a = [ ]
    b = 0
    c = [ ]
    d = sns.set
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def graph(self):
        return plt.hist(self.a, self.b, self.c, self.d)

bins = list(range(0, 3) )
PL_hist = Histogram(df["petal_length"], 20, plt.style.use('fivethirtyeight'), sns.set() )
# Format histogram style.

plt.xlabel('Petal Length (BLAHH)') 
plt.show(PL_hist.graph() )
#-----------------------------------------------------------
PW_hist = Histogram(df["petal_width"], [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75], [plt.style.use('fivethirtyeight')], 
[("Petal Widh of Iris Flowerssss")]) 
# Format histogram style.
plt.title("Petal Width of Iris Flowers")
plt.xlabel('Petal Width (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.show(PW_hist.graph() )
