
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns 

df = pd.read_csv("IrisDataset.csv")

plt.scatter(df['sepal_length'], df['sepal_width'] )
plt.title("Sepal Length Vs Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.show()