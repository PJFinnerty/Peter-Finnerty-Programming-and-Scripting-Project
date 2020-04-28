import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import robust
df = pd.read_csv('IrisDataset.csv')
#------------------------------------------------------------------------------

# Q3(i): Output a summary of each variable to a single text file.

# Use 'sys.stdout' to print statements to output a summary to the command line and then redirect to a text file.
import sys # ref: https://stackoverflow.com/questions/17394846/print-the-output-in-txt-from-command-line-using-python
orig_sys = sys.stdout  # ref: https://stackoverflow.com/questions/17394846/print-the-output-in-txt-from-command-line-using-python
with open('summary.txt','w') as out: # ref: https://stackoverflow.com/questions/17394846/print-the-output-in-txt-from-command-line-using-python
    sys.stdout = out
    # Print 
    print("No. of rows/no. of columns: ", df.shape, "\n\nNames of species/no. of vectors:") # (150, 5)
    print(df["species"].value_counts(), "\n") 
    # virginica     50, setosa        50, versicolor    50
    # Name: species, dtype: int64
    print(df.columns, "\n") # Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
    # 'species'], dtype='object')
    MAD1 = round(robust.mad(df["sepal_length"]), 6)
    MAD2 = round(robust.mad(df["sepal_width"]), 6)
    MAD3 = round(robust.mad(df["petal_length"]), 6)
    MAD4 = round(robust.mad(df["petal_width"]), 6)
    print("\n", df.describe(), "\nmad       ",MAD1,"   ",MAD2,"    ",MAD3,"   ",MAD4)

    print("\nDistinguishing Setosa Species Through Univariate Analysis\n\
    Setosa and Petal Length:\n\
    From observations made under univariate analysis of 'Petal Length' (PL)\
    it is noted that Iris Setosa can be immediately distinguised from the other classes.\n\
    This is identified in the histogram where there are no Setosa shown to have a petal length greater than 2cm,\
    and no Virginca or Versicolor shown to have a petal length less than 2cm.\n\n\
    This is reflected in the violin plot of petal length, whereby Setosa has a 75 percentile of 1.8cm.\
    The violin plot shows Setosa being greatly separated from Virginica, that diaplays a 25th percentile of 4cm and\
    Versicolor, with a 25th percentile of 5cm.")
