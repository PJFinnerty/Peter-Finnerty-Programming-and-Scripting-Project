# Peter Finnerty - Project - Scattergrams.

# Output a scattergram of each variable to png files.
#  This program will create a scattergram of (a)Iris setosa, (b)Iris virginica 
# and (c)Iris versicolor.

# Sepal Length versus Petal Length

# 2. 
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = pd.read_csv('IrisDataset.csv')
sns.set_style("whitegrid")
df = sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Length Vs Petal Length")
#plt.savefig("scatter2.png")
#plt.clf
#plt.show()