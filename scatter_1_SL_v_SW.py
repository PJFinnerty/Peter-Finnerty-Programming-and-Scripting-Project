# Peter Finnerty - Project - Scattergrams.

# Output a scattergram of each variable to png files.
#  This program will create a scattergram of (a)Iris setosa, (b)Iris virginica 
# and (c)Iris versicolor.

# I must create a separate scattergram for each specias, this will feature 4 variables.
# Sepal Length versus Sepal Width

# 1.
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = pd.read_csv('IrisDataset.csv')
sns.set_style("whitegrid")
df = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Length Vs Sepal Width")
#plt.savefig("scatter1.png")
#plt.clf
#plt.show()


# Looking at the scatter plot it's noted that setosa can be distinguised from the other species
# by using linear separation.

