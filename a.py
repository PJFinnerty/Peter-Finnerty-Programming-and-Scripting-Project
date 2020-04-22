import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import robust
df = pd.read_csv('IrisDataset.csv')

#------------------------------------------------------------------------------
# Outputting summaries of variables to 'summary.txt'.

import sys # ref: https://stackoverflow.com/questions/17394846/print-the-output-in-txt-from-command-line-using-python
orig_sys = sys.stdout  # ref: https://stackoverflow.com/questions/17394846/print-the-output-in-txt-from-command-line-using-python
with open('summary.txt','w') as out: # ref: https://stackoverflow.com/questions/17394846/print-the-output-in-txt-from-command-line-using-python
    sys.stdout = out
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

    








#-----------------------------------------------------------------------------------------------


