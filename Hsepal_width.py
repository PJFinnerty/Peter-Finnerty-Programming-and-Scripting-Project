# Peter Finnerty - Project Part 3(iii)
# Draft code for histogram of SEPAL WIDTH (all 3 species) 

# Q. Have the script save a histogram of each variable to png files.
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('IrisDataset.csv')

bins = [2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5]
plt.hist(df["sepal_width"], bins = bins, color='purple', edgecolor='black')

plt.style.use('fivethirtyeight')
plt.title("Sepal Width of Iris Flowers")
plt.xlabel('Sepal Width (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.legend()

median_SW = 3
color = '#fc4f30' 
plt.axvline(median_SW, color=color, label='Median Sepal Width', linewidth=4)

plt.show()
# plt.savefig("sepal_width.png")
# plt.clf
#-----------------------------------------------------------------------------
# To do: 
# 1. Create separate histogram for each variable OF EACH SPECIES?
# 2. Format the hists in respect of the 'bars' (no spaces, correct bar allignment etc).
# 3. Set pd.read function to read from file in local machine.
# 4. Add extra functionality and double check requirements.