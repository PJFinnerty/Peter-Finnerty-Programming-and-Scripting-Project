import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('IrisDataset.csv')

class Histogram():
    a = (df['petal_length'], df['petal_width'], df['sepal_length'], df['sepal_width'] )
    b = 0
    c = [plt.style.use('fivethirtyeight')]
    d = [plt.title]
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def graph(self):
        return plt.hist(self.a, self.b, self.c, self.d)


PL_hist = Histogram(df["petal_length"], [20], [], 
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


# Calculate the Median Absolute Deviation
# from statsmodels import robust
# MAD_PL = robust.mad(df["petal_length"])
# MAD_PW = robust.mad(df["petal_width"])
# MAD_SL = robust.mad(df["sepal_length"])
# MAD_SW = robust.mad(df["sepal_width"])
# print(MAD_PL)
# print(MAD_PW)
# print(MAD_SL)
# print(MAD_SW)
# 
# with open ('summary.txt', 'a') as f:
#     f.write(MAD_PL)

#print("Mean Sepal Length: ", np.mean(df["sepal_length"]), "\n", "Mean Sepal Width: ", np.mean(df["sepal_width"]) )
#
## Calculate the Median Absolute Deviation
#
#MAD_PL = 
#print(
## Calculate the median with an outlier:
#print("Median Petal Length: ", np.median(np.append(df["petal_length"], 50) ) )
# print(data.target[[10, 25, 50]] ) # [0 0 1]
# print("Summary of Petal Length: \nMean Petal Length: ", np.mean(df["petal_length"]), "\nMAD of Petal Length: ", robust.mad(df["petal_width"]))

# print("\nMean Petal Width: ", np.mean(df["petal_width"]) )


# with open ('summary.txt', 'w') as f:
#     f.write("Peter Finnerty - Iris Dataset Project\nThis text file contains a brief description of the \
# variables contained in the Iris Dataset.\n\nSummary of Iris Dataset Variables", )
