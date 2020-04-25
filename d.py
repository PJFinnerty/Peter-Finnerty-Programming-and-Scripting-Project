import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import robust
import math
dataset = pd.read_csv('IrisDataset.csv')
#-----------------------------------------------------------------------
df = pd.read_csv('IrisDataset.csv')
PL = np.array( df['petal_length'])
PW = np.array( df['petal_width'])
SL = np.array( df['sepal_length'])
SW = np.array( df['sepal_width'])




ax1.histogram(PL, bins='auto')
ax1.set_title('PL Histogram')
ax1.set_xlabel('$PL$')
ax1.set_ylabel('$PW$')
plt.show()

ax1.scatter(x=PL, y=PW, marker='o', c='r', edgecolor='b')
ax1.set_title('Scatter: Petal Length Vs Petal Width')

# Creating box plot.
import seaborn as sns
sns.set_style("whitegrid")
sns.boxplot(x = 'species', y = 'petal_length', hue='species', sym='c+', data = df)
plt.title("Iris flowers: Box Plot of Petal Length")
plt.show()

# Creating a violin plot.
sns.set_style("whitegrid")
sns.violinplot(x = "species", y = "petal_length", hue='species', size = 8, data = df)
plt.title("Iris flowers: Violin Plot of Petal Length")
plt.show()

# Compute and plot PDF of petal_length:
# Reference: https://www.appliedaicourse.com/course/11/Applied-Machine-learning-course
counts, bin_edges = np.histogram(df['petal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
# Plotting the CDF using the cumulative sum function of Numpy.
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)
plt.title("Petal Length PDF and CDF")
plt.show()


#-----------------------------------------------------------------------------
# To do: 
# 1. Create separate histogram for each variable OF EACH SPECIES?
# 2. Format the hists in respect of the 'bars' (no spaces, correct bar allignment etc).
# 3. Set pd.read function to read from file in local machine.
# 4. Add extra functionality and double check requirements.
 
