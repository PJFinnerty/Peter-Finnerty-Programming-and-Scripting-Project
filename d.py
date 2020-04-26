import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import robust
import math
dataset = pd.read_csv('IrisDataset.csv')
#-----------------------------------------------------------------------
df = pd.read_csv('IrisDataset.csv')
PL = np.array( df['petal_length'])
PW = np.array( df['petal_width'])
SL = np.array( df['sepal_length'])
SW = np.array( df['sepal_width'])


