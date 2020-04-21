import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# df = pd.read_csv('IrisDataset.csv')
# # Create hist with bin measures set to bins list.
# bins = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75]
# plt.hist(df["petal_width"], bins = bins, edgecolor='black')
# a = df["petal_width"]
# b = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75] 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
df = pd.read_csv('IrisDataset.csv')

class Histogram():
    a = (df['petal_length'], df['petal_width'], df['sepal_length'], df['sepal_width']
    b = 0
    c = []
    d = [plt.title]
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def graph(self):
        return plt.hist(self.a, self.b, self.c, self.d)


PL_hist = Histogram(df["petal_length"], [0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 
4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5], [plt.style.use('fivethirtyeight')], 
[("Petal Length of Iris Flowerssss")])

# Format histogram style.
plt.xlabel('Petal Length (BLAHH)')
plt.ylabel('No. of observations')
[plt.tight_layout()] 
plt.show(PL_hist.graph() )
#-----------------------------------------------------------
PW_hist = Histogram(df["petal_width"], [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75] )
# Format histogram style.
plt.style.use('fivethirtyeight')
plt.title("Petal Width of Iris Flowers")
plt.xlabel('Petal Width (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
PW_hist(color='red')
plt.show(PW_hist.graph() )
#-----------------------------------------------------------
SL_hist = Histogram(df["sepal_length"], [4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5, 7.75, 8] )
# Format histogram style.
plt.style.use('fivethirtyeight')
plt.title("Sepal Length of Iris Flowers")
plt.xlabel('Sepal Length (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.legend()
plt.show(SL_hist.graph() )
#--------------------------------------------------------------
SW_hist = Histogram(df["sepal_width"], [2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5] )
# Format histogram style.
plt.style.use('fivethirtyeight')
plt.title("Sepal Width of Iris Flowers")
plt.xlabel('Sepal Width (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.show(SW_hist.graph() )
#-----------------------------------------------------------------