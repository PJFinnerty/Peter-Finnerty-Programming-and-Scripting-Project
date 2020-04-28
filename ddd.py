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

# VIRGINICA V Versicolor : PL and PW

plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Virginica and Versicolor: CDF and PDF of Sepal Length / Sepal Width")
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
plt.suptitle("Virginica and Versicolor: CDF and PDF of Sepal Length / Sepal Width")
sns.set_style("darkgrid")

plt.subplot(221)
counts, bin_edges = np.histogram(virginica['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Virginica Sepal Length")
plt.legend()


plt.subplot(221)
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
