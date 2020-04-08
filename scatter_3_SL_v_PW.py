# Peter Finnerty - Project - Scattergrams.

# Output a scattergram of each variable to png files.
#  This program will create a scattergram of (a)Iris setosa, (b)Iris virginica 
# and (c)Iris versicolor.

# Sepal Length versus Petal Width

# 3. 
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

sL = df["sepal_length"]
sW = df["petal_width"]

plt.scatter(df['sepal_length'], df['petal_width'] )
# or plt.scatter(sL, sW)
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')
plt.title("Sepal Length Versus Petal Width (ALL SPECIES)")
#plt.legend()
plt.show()

#plt.savefig("scatter3-SLvPW.png")
#plt.clf