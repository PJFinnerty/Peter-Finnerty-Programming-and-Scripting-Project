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
from statsmodels import robust
df = pd.read_csv('IrisDataset.csv')
#------------------------------------------------------------------------------

# Q3(i): Output a summary of each variable to a single text file.

# Use 'sys.stdout' to print statements to output a summary to the command line and then redirect to a text file.
import sys # ref: https://stackoverflow.com/questions/17394846/print-the-output-in-txt-from-command-line-using-python
orig_sys = sys.stdout  # ref: https://stackoverflow.com/questions/17394846/print-the-output-in-txt-from-command-line-using-python
with open('summary.txt','w') as out: # ref: https://stackoverflow.com/questions/17394846/print-the-output-in-txt-from-command-line-using-python
    sys.stdout = out
    # Print 
    print("No. of rows/no. of columns: ", df.shape, "\n\nNames of species/no. of vectors:") # (150, 5)
    print(df["species"].value_counts(), "\n") 
    # virginica     50, setosa        50, versicolor    50
    # Name: species, dtype: int64
    print(df.columns, "\n") # Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
    # 'species'], dtype='object')
    MAD1 = round(robust.mad(df["sepal_length"]), 6)
    MAD2 = round(robust.mad(df["sepal_width"]), 6)
    MAD3 = round(robust.mad(df["petal_length"]), 6)
    MAD4 = round(robust.mad(df["petal_width"]), 6)
    print("\n", df.describe(), "\nmad       ",MAD1,"   ",MAD2,"    ",MAD3,"   ",MAD4)

#---------------------------------------------------------------------------------------------------

# Q3(ii): Save a histogram of each variable to png files.

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
#---------------------------------------------------------------------------------
# Output a scatterplot of each pair of variables to png files.
iris = pd.read_csv('IrisDataset.csv')

# Scatterplot of Petal Length Vs Petal Width
sns.set_style("darkgrid")
df = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=iris)
plt.title("Iris Flowers: Petal Length Vs Petal Width")
plt.savefig("scatter1.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Scatterplot of Petal Length Vs Sepal Length
sns.set_style("darkgrid")
df = sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Length Vs Petal Length")
plt.savefig("scatter2.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------
# Scatterplot of Petal Length Vs Sepal Width 
sns.set_style("darkgrid")
df = sns.scatterplot(x="sepal_width", y="petal_length", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Width Vs Petal Length")
plt.savefig("scatter3.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Scatterplot of Petal Width Vs Sepal Length
sns.set_style("darkgrid")
df = sns.scatterplot(x="sepal_length", y="petal_width", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Length Vs Petal Width")
plt.savefig("scatter4.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Scatterplot of Petal Width Vs Sepal Width
sns.set_style("darkgrid")
df = sns.scatterplot(x="sepal_width", y="petal_width", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Width Vs Petal Width")
plt.savefig("scatter5.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------
# Scatterplot of Sepal Length Vs Sepal Width
sns.set_style("darkgrid")
df = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
plt.title("Iris Flowers: Sepal Length Vs Sepal Width")
plt.savefig("scatter6.png")
plt.clf
plt.show()
# Looking at the scatter plot it's noted that setosa can be distinguised from the other species
# by using linear separation.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Compute and plot PDF of petal_length:

# Create large figure to fit 4 subplots, set title and style.
plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Probability Density Function (PDF) and Cumulative Distribution Function (CDF) of 4 Features")
sns.set_style("darkgrid")

# Create subplot 1: create counts and bin_edges variables and assign it to the histogram for 'petal_length', set bins to 10.

plt.subplot(221) #(221) - the first two digits refer to the subplot formation (2 by 2) and the final digit assigns it as the first subplot.
counts, bin_edges = np.histogram(df['petal_length'], bins = 10, density = True) # Reference: appliedaicourse.com
# Create pdf variable and assign it the value of each x point on petal length histogram divided by the sum of the points.
pdf = counts / (sum(counts) )
# Use Numpys's cumulative sum function on 'pdf' variable and assign it to variable 'cdf'.
cdf = np.cumsum(pdf)
# Plot both CDF and PDF lines and label.
plt.plot(bin_edges[1:], pdf, label = 'PDF') # Reference: appliedaicourse.com
plt.plot(bin_edges[1:], cdf, label = 'CDF')
# Assign titel and legend.
plt.title("Petal Length")
plt.legend()

plt.subplot(222)
counts, bin_edges = np.histogram(df['petal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Petal Width")
plt.legend()

plt.subplot(223)
counts, bin_edges = np.histogram(df['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Sepal Length")
plt.legend()

plt.subplot(224)
counts, bin_edges = np.histogram(df['sepal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Sepal Width")
plt.legend()

plt.show()

#============================================================================================

# Creating violin plots of the features.

# Create large figure to fit 4 subplots, set title and style.
plt.figure (figsize = (15, 6.5) ) 
plt.suptitle("Iris Flowers: Violin Plots of Features")
sns.set_style("darkgrid")

# Create violin plot 1, add hue for species and format as necessary.
plt.subplot(221)  #(221) - the first two digits refer to the subplot formation (2 by 2) and the final digit assigns it as the first subplot.
sns.violinplot(x = "species", y = "petal_length", hue='species', size = 8, data = df)
plt.title("Petal Length", ha = 'right')

plt.subplot(222)
sns.violinplot(x = "species", y = "petal_width", hue='species', size = 8, data = df)
plt.title("Petal Width", ha = 'right' )

plt.subplot(223)
sns.violinplot(x = "species", y = "sepal_length", hue='species', size = 8, data = df)
plt.title("Petal Width", ha = 'right')

plt.subplot(224)
sns.violinplot(x = "species", y = "sepal_width", hue='species', size = 8, data = df)
plt.title("Petal Width", ha = 'right')

plt.show()