import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import robust
import math
df = pd.read_csv('IrisDataset.csv')
#-----------------------------------------------------------------------
PL = np.array( df['petal_length'])
PW = np.array( df['petal_width'])
SL = np.array( df['sepal_length'])
SW = np.array( df['sepal_width'])

setosa = df[0:50]
versicolor = df[50:100]
virginica = df[100:150]

#VIRGINICA
# 2d Density Plot: PL v PW
sns.jointplot(x="petal_length", y="petal_width", data = virginica, kind = "kde", colour='r')
plt.suptitle("Virginica: Petal Length Vs Petal Width")
plt.savefig("virginica_C1.png")
plt.clf
plt.show()


# 2D Density Plot: PL v SL
sns.jointplot(x="sepal_length", y="petal_length", data = virginica, kind = "kde")
plt.suptitle("Virginica: Petal Length Vs Sepal Length")
plt.savefig("virginica_C2.png")
plt.clf
plt.show()

# 2d density plot: PL v SW
sns.jointplot(x="sepal_width", y="petal_length", data = virginica, kind = "kde")
plt.suptitle("Virginica: Petal Length Vs Sepal Width")
plt.savefig("virginica_C3.png")
plt.clf
plt.show()

# 2d density plot: PW v SL
sns.jointplot(x="petal_width", y="sepal_length", data = virginica, kind = "kde")
plt.suptitle("Virginica: Petal Width Vs Sepal Length")
plt.savefig("virginica_C4.png")
plt.clf
plt.show()

# 2d density plot: PW v SW 
sns.jointplot(x="petal_width", y="sepal_width", data = virginica, kind = "kde")
plt.suptitle("Virginica: Petal Width Vs Sepal Width")
plt.savefig("virginica_C5.png")
plt.clf
plt.show()

# 2d density plot: SL v SW
sns.jointplot(x="sepal_length", y="sepal_width", data = virginica, kind = "kde")
plt.suptitle("Virginica: Sepal Length Vs Sepal Width")
plt.savefig("virginica_C6.png")
plt.clf
plt.show()
#=================================================================

#VERGINICA
# 2d Density Plot: PL v PW
sns.jointplot(x="petal_length", y="petal_width", data = versicolor, kind = "kde")
plt.suptitle("Versicolor: Petal Length Vs Petal Width")
plt.savefig("versicolor_C1.png")
plt.clf
plt.show()


# 2D Density Plot: PL v SL
sns.jointplot(x="petal_length", y="sepal_length", data = versicolor, kind = "kde")
plt.suptitle("Versicolor: Petal Length Vs Sepal Length")
plt.savefig("versicolor_C2.png")
plt.clf
plt.show()

# 2d density plot: PL v SW
sns.jointplot(x="petal_length", y="sepal_width", data = versicolor, kind = "kde")
plt.suptitle("Versicolor: Petal Length Vs Sepal Width")
plt.savefig("versicolor_C3.png")
plt.clf
plt.show()

# 2d density plot: PW v SL
sns.jointplot(x="petal_width", y="sepal_length", data = virginica, kind = "kde")
plt.suptitle("versicolor: Petal Width Vs Sepal Length")
plt.savefig("veriscolor_C4.png")
plt.clf
plt.show()

# 2d density plot: PW v SW 
sns.jointplot(x="petal_width", y="sepal_width", data = versicolor, kind = "kde")
plt.suptitle("Versicolor: Petal Width Vs Sepal Width")
plt.savefig("versicolor_C5.png")
plt.clf
plt.show()

# 2d density plot: SL v SW
sns.jointplot(x="sepal_length", y="sepal_width", data = versicolor, kind = "kde")
plt.suptitle("Versicolor: Sepal Length Vs Sepal Width")
plt.savefig("versicolor_C6.png")
plt.clf
plt.show()