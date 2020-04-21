# IPython log file

get_ipython().run_line_magic('logstart', '')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import seaborn as sns
# IMmport data
data = pd.read_csv('IrisDataset.csv', names=['f1', 'f2', 'f3', 'f4', 'f5'] )
data
data["f5"].value_counts()
sns.FacetGrid(data, hue="f5", height=5)\
    .map(plt.scatter, "f1", "f2" )\
        .add_legend()
# Map data into arrays
s = np.asarray([1,0,0])
ve = np.asarray([0,1,0])
vi = np.asarray([0,0,1])
data['f5'] = data['f5'].map( {'Iris-setosa': s, 'Iris-versicolor' : ve, 'Iris-virginica' : vi})
data
exit()
