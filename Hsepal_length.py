# Peter Finnerty - Project Part 3(iii)
# Draft code for histogram of SEPAL LENGTH (all 3 species) 

# Q. Have the script save a histogram of each variable to png files.
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('IrisDataset.csv')

# Create hist with bin measures set to bins list.
bins = [4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5, 7.75, 8]
plt.hist(df["sepal_length"], bins = bins, color='green', edgecolor='black')

# Format histogram.
plt.style.use('fivethirtyeight')
plt.title("Sepal Length of Iris Flowers")
plt.xlabel('Sepal Length (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.legend()
# Mark out a median value line.
# median_SL = 5.8
# color = '#fc4f30' 
# plt.axvline(median_SL, color=color, label='Median Sepal Length', linewidth=4)
plt.savefig("Hsepal_length.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------
# Creating box plot.
import seaborn as sns
sns.set_style("whitegrid")
sns.boxplot(x = 'species', y = 'sepal_length', hue='species', sym='c+', data = df)
plt.title("Iris flowers: Box Plot of Sepal length")
plt.show()

# Creating a violin plot.
sns.set_style("whitegrid")
sns.violinplot(x = "species", y = "sepal_length", hue='species', size = 8, data = df)
plt.title("Iris flowers: Violin Plot of Sepal length")
plt.show()

# Compute and plot PDF of petal_length:
# Reference: https://www.appliedaicourse.com/course/11/Applied-Machine-learning-course
counts, bin_edges = np.histogram(df['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
# Plotting the CDF using the cumulative sum function of Numpy.
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)
plt.title("Sepal Length PDF and CDF")
plt.show()

# Calculate the Median Absolute Deviation
from statsmodels import robust
print(robust.mad(df["sepal_length"]) )

#-----------------------------------------------------------------------------
# To do: 
# 1. Create separate histogram for each variable OF EACH SPECIES?
# 2. Format the hists in respect of the 'bars' (no spaces, correct bar allignment etc).
# 3. Set pd.read function to read from file in local machine.
# 4. Add extra functionality and double check requirements.
