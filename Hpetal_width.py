# Peter Finnerty - Project Part 3(iii)
# Draft code for histogram of PETAL WIDTH (all 3 species) 

# Q. Have the script save a histogram of each variable to png files.
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('IrisDataset.csv')

# Create hist with bin measures set to bins list.
bins = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75]
plt.hist(df["petal_width"], bins = bins, edgecolor='black')

# Format histogram style.
plt.style.use('fivethirtyeight')
plt.title("Petal Width of Iris Flowers")
plt.xlabel('Petal Width (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
# Marking out a median line.
# median_PW = 1.3
# color = '#fc4f30' 
# plt.axvline(median_PW, color=color, label='Median Petal Width', linewidth=4)
plt.savefig("Hpetal_width.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------

# Creating box plot.
import seaborn as sns
sns.set_style("whitegrid")
sns.boxplot(x = 'species', y = 'petal_width', hue='species', sym='c+', data = df)
plt.title("Iris flowers: Box Plot of Petal Width")
plt.show()

# Creating a violin plot.
sns.set_style("whitegrid")
sns.violinplot(x = "species", y = "petal_width", hue='species', size = 8, data = df)
plt.title("Iris flowers: Violin Plot of Petal Width")
plt.show()

# Compute and plot PDF of petal_length:
# Reference: https://www.appliedaicourse.com/course/11/Applied-Machine-learning-course
counts, bin_edges = np.histogram(df['petal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
# Plotting the CDF using the cumulative sum function of Numpy.
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.xlabel("Sepal Length")
plt.ylabel("Probability")
plt.plot(bin_edges[1:], cdf)
plt.title("Petal Width PDF and CDF")
plt.show()

# Calculate the Median Absolute Deviation
from statsmodels import robust
print(robust.mad(df["petal_width"]) )

#-----------------------------------------------------------------------------
# To do: 
# 1. Create separate histogram for each variable OF EACH SPECIES?
# 2. Format the hists in respect of the 'bars' (no spaces, correct bar allignment etc).
# 3. Set pd.read function to read from file in local machine.
# 4. Add extra functionality and double check requirements.