import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('IrisDataset.csv')
print(df.index.values)

b = df.set_index('species')
print (b.head() )

b2 = df[ (df.sepal_length>5) & (df.petal_length<6) ] 
print(b.head() )

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('IrisDataset.csv')

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))
fig.subplots_adjust(hspace=0.8)
fig.suptitle('Distributions of Iris Features')

f or ax, feature, name in zip(axes.flatten(), df.drop('species',axis=1).values.T, df.columns.values):
    ax.hist(feature, bins=len(np.unique(df.drop('species',axis=1).values.T[0])//2))
    ax.set(title=name[:-4].upper(), xlabel='cm')

plt.show()
#-----------------------------------------------------------------------
df = pd.read_csv('IrisDataset.csv')
PL = np.array( df['petal_length'])
PW = np.array( df['petal_width'])
SL = np.array( df['sepal_length'])
SW = np.array( df['sepal_width'])
sns.set()
plt.hist(PL)
plt.show()

class Histogram():
    a = (df['petal_length'], df['petal_width'], df['sepal_length'], df['sepal_width'] )
    b = [PL]
    c = [plt.style.use('fivethirtyeight')]
    d = [plt.title]
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def graph(self):
        return plt.hist(self.a, self.b, self.c, self.d)


PL_hist = Histogram(df["petal_length"], [PL], [], 
[("Petal Length of Iris Flowerssss")])
# Format histogram style.
plt.xlabel('Petal Length (BLAHH)')
plt.ylabel('No. of observations')
[plt.tight_layout()] 
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
