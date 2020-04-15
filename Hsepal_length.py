# Peter Finnerty - Project Part 3(iii)
# Draft code for histogram of SEPAL LENGTH (all 3 species) 

# Q. Have the script save a histogram of each variable to png files.
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('IrisDataset.csv')

bins = [4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5, 7.75, 8]
plt.hist(df["sepal_length"], bins = bins, color='green', edgecolor='black')

plt.style.use('fivethirtyeight')
plt.title("Sepal Length of Iris Flowers")
plt.xlabel('Sepal Length (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.legend()

median_SL = 5.8
color = '#fc4f30' 
plt.axvline(median_SL, color=color, label='Median Sepal Length', linewidth=4)

plt.show()
# plt.savefig("sepal_length.png")
# plt.clf
#-----------------------------------------------------------------------------
# To do: 
# 1. Create separate histogram for each variable OF EACH SPECIES?
# 2. Format the hists in respect of the 'bars' (no spaces, correct bar allignment etc).
# 3. Set pd.read function to read from file in local machine.
# 4. Add extra functionality and double check requirements.
