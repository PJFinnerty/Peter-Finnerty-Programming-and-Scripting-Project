import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import robust
import math
df = pd.read_csv('IrisDataset.csv')

# Compute and plot PDF of petal_length:

# Create large figure to fit 4 subplots, set title and style.
plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Probability Density Function (PDF) and Cumulative Distribution Function (CDF) of 4 Features")
sns.set_style("darkgrid")

# Plotting the CDF using the cumulative sum function of Numpy.

# Create subplot 1: create counts and bin_edges variables and assign it to the histogram for 'petal_length', set bins to 10.
plt.subplot(221)
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
# Creating a violin plot.
plt.figure (figsize = (15, 6.5) ) 
plt.suptitle("Iris Flowers: Violin Plots of Features")
sns.set_style("darkgrid")

plt.subplot(221)
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