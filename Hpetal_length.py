# Peter Finnerty - Project Part 3(iii)
# Draft code for histogram of PETAL LENGTH (all 3 species) 

# Q. Have the script save a histogram of each variable to png files.
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

plt.hist(df["petal_length"])
plt.title("Petal Length All Sprecies")

plt.show()

plt.savefig("petal_length.png")
plt.clf
#-----------------------------------------------------------------------------
# To do: 
# 1. Create separate histogram for each variable OF EACH SPECIES?
# 2. Format the hists in respect of the 'bars' (no spaces, correct bar allignment etc).
# 3. Set pd.read function to read from file in local machine.
# 4. Add extra functionality and double check requirements.