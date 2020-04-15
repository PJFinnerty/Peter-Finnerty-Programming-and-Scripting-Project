# Peter Finnerty - Project Part 3(iii)
# Draft code for histogram of PETAL LENGTH (all 3 species) 

# Q. Have the script save a histogram of each variable to png files.
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('IrisDataset.csv')

# Create hist with bin measures set to bins list.
bins = [0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 
4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5]
plt.hist(df["petal_length"], bins = bins, edgecolor='black')
# Set the histrogram style.
plt.style.use('fivethirtyeight')

# Format the histogram as appropriate.
plt.title("Petal Length of Iris Flowers")
plt.xlabel('Petal Length (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.legend()
# Mark out a median value line.
median_PL = 4.35
color = '#fc4f30'
plt.axvline(median_PL, color=color, label='Median Petal Length', linewidth=2.5)

plt.show()
#-------------------------------------------------------------------------------

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

# Calculate the Median Absolute Deviation
from statsmodels import robust
print(robust.mad(df["petal_length"]) )

# plt.savefig("petal_length.png")
# plt.clf
#-----------------------------------------------------------------------------
# To do: 
# 1. Create separate histogram for each variable OF EACH SPECIES?
# 2. Format the hists in respect of the 'bars' (no spaces, correct bar allignment etc).
# 3. Set pd.read function to read from file in local machine.
# 4. Add extra functionality and double check requirements.