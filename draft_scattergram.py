# Peter Finnerty - Project - Scattergrams.


# The following scripts relate to information contained in Sections 1-3 of Notes in README,
# it has been collected in research for the Iris Project.

# This file contains scripts that experiment with Scattergrams extrapolted from 
# the Iris dataset.
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
#-------------------------------------------------------------------------------

# Scripts relating to Sections 1 & 2 of README.

plt.scatter(df['sepal_length'], df['sepal_width'] )
# or plt.scatter(sL, sW)
# or df.plot(kind = 'scatter', x = 'sepal_length', y = 'sepal_width'])
# NB: the plot produced above is not defined at 0.0!!

# Colouring vectors to represent class (species)
sns.set_style("whitegrid")
sns.FacetGrid(df, hue = "species", size = 4.5) \
    .map(plt.scatter, "sepal_length", "sepal_width") \
    .add_legend()
plt.show()

# The results of the scatter of SL and SW show that setosa can
# be distinguised - by drawing a line to separate them from versicolour 
# and virginica.
# Setosa show a trend towards greater sepal width and slightly
# shorte sepal width than the other species.
# Setosa are therefore linearly separable.
#-------------------------------------------------------------------------

# Below script corresponds to Section 3 of README notes .
sns.set_style("whitegrid")
sns.pairplot(df, hue = "species", height = 3)
plt.show()

# Below script corresponds to Section 3(d) of README notes. This helps distinguish Setosa.
if PL <= 2:
    & PW <= 1

# Below script from Section 3(e) of README notes.
if PW <= 2:
    & PW >= 1 
if PL < 5:
    & PL > 2.5
#Must do a Boolean And of these 4 statements in order to distinguish Versicolour. 
# It must be noted that there will be some Virginica vectors included in this calculation.
#------------------------------------------------------------------------------



