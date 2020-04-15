# Peter Finnerty - Project Part 3(iii)
# Draft code for histogram of SEPAL WIDTH (all 3 species) 

# Q. Have the script save a histogram of each variable to png files.
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('IrisDataset.csv')

# Create hist with bin measures set to bins list.
bins = [2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5]
plt.hist(df["sepal_width"], bins = bins, color='purple', edgecolor='black')

# Format histogram style.
plt.style.use('fivethirtyeight')
plt.title("Sepal Width of Iris Flowers")
plt.xlabel('Sepal Width (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.legend()
# Marking out a median value line.
median_SW = 3
color = '#fc4f30' 
plt.axvline(median_SW, color=color, label='Median Sepal Width', linewidth=4)
plt.show()
#-------------------------------------------------------------------------------

# Creating box plot of Sepal Width.
import seaborn as sns
sns.set_style("whitegrid")
sns.boxplot(x = 'species', y = 'sepal_width', hue='species', sym='c+', data = df)
plt.title("Iris flowers: Box Plot of Sepal Width")
plt.show()

# Creating a violin plot.
sns.set_style("whitegrid")
sns.violinplot(x = "species", y = "sepal_width", hue='species', size = 8, data = df)
plt.title("Iris flowers: Violin Plot of Sepal Width")
plt.show()

# Compute and plot PDF of petal_length:
# Reference: https://www.appliedaicourse.com/course/11/Applied-Machine-learning-course
counts, bin_edges = np.histogram(df['sepal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
# Plotting the CDF using the cumulative sum function of Numpy.
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)
plt.title("Sepal Width PDF and CDF")
plt.show()

# Calculate the Median Absolute Deviation
from statsmodels import robust
print(robust.mad(df["sepal_width"]) )

# plt.savefig("sepal_width.png")
# plt.clf
#-----------------------------------------------------------------------------
# To do: 
# 1. Create separate histogram for each variable OF EACH SPECIES?
# 2. Format the hists in respect of the 'bars' (no spaces, correct bar allignment etc).
# 3. Set pd.read function to read from file in local machine.
# 4. Add extra functionality and double check requirements.