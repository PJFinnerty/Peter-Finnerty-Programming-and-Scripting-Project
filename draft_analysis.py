# Peter Finnerty - Project 2020
# Write a program called analysis.py that:
# • outputs a summary of each variable to a single text file,
# • saves a histogram of each variable to png files, and
# • outputs a scatter plot of each pair of variables.
#-----------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv('IrisDataset.csv')
#------------------------------------------------------------------------------

# Histogram of Petal Length (all species)
# Create hist with bin measures set to bins list.
sns.FacetGrid(df,hue="species",height=5.5).map(sns.distplot,"petal_length").add_legend()
plt.xlabel("Petal Length (cm)")
plt.ylabel("Occurrance")
# Format histogram style.
sns.set_style("darkgrid")
plt.style.use('fivethirtyeight')
plt.title("Petal Length of Iris Flowers")
plt.tight_layout()
plt.savefig("Hpetal_length.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------

# Histogram of Petal Width (all species)
sns.FacetGrid(df,hue="species",height=5.5).map(sns.distplot,"petal_width").add_legend()
plt.xlabel("Petal Width (cm)")
plt.ylabel("Occurrance")
# Format histogram.
sns.set_style("darkgrid")
plt.style.use('fivethirtyeight')
plt.title("Petal Width of Iris Flowers")
plt.tight_layout()
plt.savefig("Hpetal_width.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------

# Histogram of Sepal Length (all species)
# Create hist with bin measures set to bins list.
sns.FacetGrid(df,hue="species",height=5.5).map(sns.distplot,"sepal_length").add_legend()
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Occurrance")
# Format histogram style.
sns.set_style("darkgrid")
plt.style.use('fivethirtyeight')
plt.title("Sepal Length of Iris Flowers")
plt.tight_layout()
plt.savefig("Hsepal_length.png")
plt.clf
plt.show()
#---------------------------------------------------------------------------------
# Histogram of Sepal Width (all species)
# Create hist with bin measures set to bins list.
sns.FacetGrid(df,hue="species",height=5.5).map(sns.distplot,"sepal_width").add_legend()
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Occurrance")
# Format histogram style.
sns.set_style("darkgrid")
plt.style.use('fivethirtyeight')
plt.title("Sepal Width of Iris Flowers")
plt.tight_layout()
plt.savefig("Hsepal_width.png")
plt.clf
plt.show()
#---------------------------------------------------------------------------------
#  This program will create a scattergram of (a)Iris setosa, (b)Iris virginica 
# and (c)Iris versicolor.
iris = pd.read_csv('IrisDataset.csv')
# Petal Length Vs Petal Width
sns.set_style("darkgrid")
df = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=iris)
plt.title("Iris Flowers: Petal Length Vs Petal Width")
plt.savefig("scatter1.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Petal Length Vs Sepal Length
sns.set_style("darkgrid")
df = sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Length Vs Petal Length")
plt.savefig("scatter2.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------
# Petal Length Vs Sepal Width 
sns.set_style("darkgrid")
df = sns.scatterplot(x="sepal_width", y="petal_length", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Width Vs Petal Length")
plt.savefig("scatter3.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Petal Width Vs Sepal Length
sns.set_style("darkgrid")
df = sns.scatterplot(x="sepal_length", y="petal_width", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Length Vs Petal Width")
plt.savefig("scatter4.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Petal Width Vs Sepal Width
sns.set_style("darkgrid")
df = sns.scatterplot(x="sepal_width", y="petal_width", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Width Vs Petal Width")
plt.savefig("scatter5.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------
# Sepal Length Vs Sepal Width
sns.set_style("darkgrid")
df = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Length Vs Sepal Width")
plt.savefig("scatter6.png")
plt.clf
plt.show()
# Looking at the scatter plot it's noted that setosa can be distinguised from the other species
# by using linear separation.
# #------------------------------------------------------------------------------