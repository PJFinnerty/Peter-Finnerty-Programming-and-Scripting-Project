import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import robust
from sklearn import preprocessing


df = pd.read_csv('IrisDataset.csv')

setosa = df[0:50]
versicolor = df[50:100]
virginica = df[100:150]

# Output a scatterplot of each pair of variables to png files.

# Scatterplot of Petal Length Vs Petal Width
sns.set_style("darkgrid")
iris = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=df)
x = [4.2, 5.65]
y = [2.0, 1.0]
plt.plot(x, y)
plt.title("Scatter Plot: Petal Length Vs Petal Width")
plt.savefig("scatter1.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Scatterplot of Petal Length Vs Sepal Length
sns.set_style("darkgrid")
iris = sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length Vs Petal Length")
plt.savefig("scatter2.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------
# Scatterplot of Petal Length Vs Sepal Width 
sns.set_style("darkgrid")
iris = sns.scatterplot(x="sepal_width", y="petal_length", hue="species", data=df)
plt.title("Scatter Plot: Sepal Width Vs Petal Length")
plt.savefig("scatter3.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Scatterplot of Petal Width Vs Sepal Length
sns.set_style("darkgrid")
iris = sns.scatterplot(x="sepal_length", y="petal_width", hue="species", data=df)
x = [4.0, 8.0]
y = [1.68, 1.68]
plt.plot(x, y)
plt.title("Note: Regression line distinguishes Versicolor from Viriginica", fontsize = 10)
plt.suptitle("Scatter Plot: Sepal Length Vs Petal Width")
plt.savefig("scatter4.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Scatterplot of Petal Width Vs Sepal Width
sns.set_style("darkgrid")
iris = sns.scatterplot(x="sepal_width", y="petal_width", hue="species", data=df)
plt.title("Scatter Plot: Sepal Width Vs Petal Width")
plt.savefig("scatter5.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------
# Scatterplot of Sepal Length Vs Sepal Width
sns.set_style("darkgrid")
iris = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length Vs Sepal Width")
plt.savefig("scatter6.png")
plt.clf
plt.show()

# VIRGINICA V Versicolor : PL and PW

plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Virginica and Versicolor: Univarariate Analysis of CDF and PDF (1/2)")
sns.set_style("darkgrid")

plt.subplot(221) 
counts, bin_edges = np.histogram(virginica['petal_length'], bins = 10, density = True) # Reference: appliedaicourse.com
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF') # Reference: appliedaicourse.com
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Virginica Petal Length")
plt.legend()

plt.subplot(222)
counts, bin_edges = np.histogram(versicolor['petal_length'], bins = 10, density = True) # Reference: appliedaicourse.com
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF') 
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Versicolor Petal Length")
plt.legend()
##

plt.subplot(223)
counts, bin_edges = np.histogram(virginica['petal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Virginica Petal Width")
plt.legend()

plt.subplot(224)
counts, bin_edges = np.histogram(versicolor['petal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Versicolor Petal Width")
plt.legend()
##

plt.savefig("d_Virg_V_Vers1.png")
plt.clf
plt.show()
#==============================================================================

# VIRGINICA V Versicolor : SL and SW

plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Virginica and Versicolor: Univariate Analysis of CDF and PDF (2/2)")
sns.set_style("darkgrid")

plt.subplot(221)
counts, bin_edges = np.histogram(virginica['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Virginica Sepal Length")
plt.legend()


plt.subplot(222)
counts, bin_edges = np.histogram(versicolor['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Versicolor Sepal Length")
plt.legend()


plt.subplot(223)
counts, bin_edges = np.histogram(virginica['sepal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Virginica Sepal Width")
plt.legend()

plt.subplot(224)
counts, bin_edges = np.histogram(versicolor['sepal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Versicolor Sepal Width")
plt.legend()

plt.savefig("d_Virg_V_Vers2.png")
plt.clf
plt.show()
