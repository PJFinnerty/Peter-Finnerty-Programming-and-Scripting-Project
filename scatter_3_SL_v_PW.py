# Peter Finnerty - Project - Scattergrams.

# Output a scattergram of each variable to png files.
#  This program will create a scattergram of (a)Iris setosa, (b)Iris virginica 
# and (c)Iris versicolor.

# Sepal Length versus Petal Width

# 3. 
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = pd.read_csv('IrisDataset.csv')
sns.set_style("whitegrid")
df = sns.scatterplot(x="sepal_length", y="petal_width", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Length Vs Petal Width")
plt.show()

#plt.savefig("scatter3-SLvPW.png")
#plt.clf