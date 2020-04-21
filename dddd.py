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
import numpy as np
df = pd.read_csv('IrisDataset.csv')
iris = df
#------------------------------------------------------------------------------
# Petal Length Vs Petal Width


class Scatter():
    df = pd.read_csv('IrisDataset.csv')
    a = df["petal_length"] 
    b = df["petal_width"]
    c = df["sepal_length"] 
    d = df["sepal_width"]
    f = iris
     
    def __init__(self, a, b, c, d, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.f = iris
    
    def hue(self):
        return sns.scatterplot(hue = "species")

    def graph(self):
        return sns.scatterplot(df[self.a,], df[self.b], df=iris)

PL_scat = graph(df["petal_length"], df["petal_width"], hue = "species", df = iris)



# df1 = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=iris)
# df2 = sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=iris)
# df3 = sns.scatterplot(x="sepal_width", y="petal_length", hue="species", data=iris)
# df4 = sns.scatterplot(x="sepal_length", y="petal_width", hue="species", data=iris)
# df5 = sns.scatterplot(x="sepal_width", y="petal_width", hue="species", data=iris)
# df6 = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
# sns.set_style("darkgrid")
# plt.title("Iris Flowers: Petal Length Vs Petal Width")
# plt.title("Iris Flowers: Sepal Length Vs Petal Length")
# plt.title("Iris Flowers: Sepal Width Vs Petal Length")
# plt.title("Iris Flowers: Sepal Length Vs Petal Width")
# plt.title("Iris Flowers: Sepal Width Vs Petal Width")
# plt.title("Iris Flowers: Sepal Length Vs Sepal Width")
# plt.show()