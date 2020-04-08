# Peter Finnerty - Project - Scattergrams.

# Output a scattergram of each variable to png files.
#  This program will create a scattergram of (a)Iris setosa, (b)Iris virginica 
# and (c)Iris versicolor.

# I must create a separate scattergram for each specias, this will feature 4 variables.

#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

sL = df["sepal_length"]
sW = df["sepal_width"]

plt.scatter(df['sepal_length'], df['sepal_width'] )
# or plt.scatter(sL, sW)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title("Sepal Length Versus Sepal Width (ALL SPECIES)")
#plt.legend()
plt.show()

#plt.savefig("scatterSLvSW.png")
#plt.clf