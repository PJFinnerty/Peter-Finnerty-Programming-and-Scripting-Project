# Peter Finnerty - Project

# The following scripts relate to information contained in Section 5 of Notes in README,
# it has been collected in research for the Iris Project.

# This relates to exploring Mean, Variance and Std-dev in the Irish Dataset.
#------------------------------------------------------------------------
import matplotlib.pyplot  as plt
import pandas as pd
import seaborn as sns
import numpy as np
import plotly.graph_objects as go

#------------------------------------------------------------------------
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

# Calculating the mean PL of (a)Setosa, (B)Virginica and (C)Versicolour, with an 'Outlier':
print(np.mean(df_setosa ["petal_length"] ) )
print(np.mean(df_virginica ["petal_length"] ) )
print(np.mean(df_versicolor ["petal_length"] ) )

#print( "\nStd-dev: ")
#print(np.std(df_setosa ["petal_length"] ) )
#print(np.std(df_virginica ["petal_length"] ) )
#print(np.std(df_versicolor ["petal_length"] ) )

