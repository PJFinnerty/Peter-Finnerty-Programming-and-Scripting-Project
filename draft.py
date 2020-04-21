import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv('IrisDataset.csv')

# Histogram of Setosa Petal Length


# Histogram of Petal Length (all species)
# Create hist with bin measures se t to bins list.
PL = np.array( df['petal_length'])
sns.set()
plt.hist(PL, bins = 20, edgecolor='black', hue= "species")
# Set the histrogram style.
plt.style.use('fivethirtyeight')
# Format the histogram as appropriate.
plt.title("Petal Length of Iris Flowers")
plt.xlabel('Petal Length (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.show()
#------------------------------------------------------------------------------

# Histogram of Petal Width (all species)
# Create hist with bin measures set to bins list.
bins = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75]
plt.hist(df["petal_width"], bins = bins, edgecolor='black')
# Format histogram style.
plt.style.use('fivethirtyeight')
plt.title("Petal Width of Iris Flowers")
plt.xlabel('Petal Width (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.show()
#-------------------------------------------------------------------------------

# Histogram of Petal Length (all species)
# Create hist with bin measures set to bins list.
bins = [4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5, 7.75, 8]
plt.hist(df["sepal_length"], bins = bins, color='green', edgecolor='black')
# Format histogram.
plt.style.use('fivethirtyeight')
plt.title("Sepal Length of Iris Flowers")
plt.xlabel('Sepal Length (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.show()
#--------------------------------------------------------------------------------

# Histogram of Sepal Width (all species)
# Create hist with bin measures set to bins list.
bins = [2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5]
plt.hist(df["sepal_width"], bins = bins, color='purple', edgecolor='black')
# Format histogram style.
plt.style.use('fivethirtyeight')
plt.title("Sepal Width of Iris Flowers")
plt.xlabel('Sepal Width (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.show()
#---------------------------------------------------------------------------------