import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import robust
df = pd.read_csv('IrisDataset.csv')


setosa = df[0:50]
versicolor = df[50:100]
virginica = df[100:150]

PL = df['petal_length']
PW = df['petal_width']
SL = df['sepal_length']
SW = df['sepal_width']

# 1. Virginica Contour Plot: Petal Length Vs Petal Width.
sns.jointplot(x="petal_length", y="petal_width", data = virginica, kind = "kde")
plt.suptitle("Virginica: Petal Length Vs Petal Width")
plt.savefig("Virg_Contour_1.png")
plt.clf
plt.show()


versicolorPL = versicolor[PL]

versicolorPW = versicolor[PW]

print("df", df.shape, "\n")
print("PL", PL.shape, "\n")
print("PW", PW.shape, "\n")
print("versicolor", versicolor.shape, "\n")

X = np.arange(0,5,0.01)
Y = np.arange(0,3,0.01)

X_grid, Y_grid = np.meshgrid(X,Y)
Z_grid = X_grid**2 + Y_grid**2

plt.contour(X_grid, Y_grid, Z_grid)  # Works fine


# Load the data
from sklearn.datasets import load_iris
iris = load_iris()

from matplotlib import pyplot as plt

## The indices of the features that we are plotting
#x_index = 0
#y_index = 1
#
## this formatter will label the colorbar with the correct target names
#formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])
#
#plt.figure(figsize=(5, 4))
#plt.contour(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
#plt.colorbar(ticks=[0, 1, 2], format=formatter)
#plt.xlabel(iris.feature_names[x_index])
#plt.ylabel(iris.feature_names[y_index])
#
#plt.tight_layout()
#plt.show()
#
#
#plt.figure(figsize=(5, 4))
#plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
#plt.colorbar(ticks=[0, 1, 2], format=formatter)
#plt.xlabel(iris.feature_names[x_index])
#plt.ylabel(iris.feature_names[y_index])
#
#plt.tight_layout()
#plt.show()


# z = z.reshape((len(x), len(y)))

#fig, ax1 = plt.subplots(nrows=1, ncols=1)



#ax1.contour(PL, PW, label='PLPW')
#ax1.set_xlabel('PL')
#ax1.set_ylabel('PW')

#ax2.scatter(df['sepal_length'], df['sepal_width'], label='SLSW')
#ax2.set_xlabel('SL')
#ax2.set_ylabel('SW')

#plt.tight_layout()
#plt.show


# # (ii) VERSICOLOR CONTOUR PLOTS
# # Use Seaborn's 'Jointplot' to create a 2D density contour plots of Versicolor.
# # Repeat for each pair of variables. 
# 
# # 1. Versicolor Contour Plot: Petal Length Vs Petal Width.
# sns.jointplot(x="petal_length", y="petal_width", data = versicolor, kind = "kde")
# plt.suptitle("Versicolor: Petal Length Vs Petal Width")
# plt.savefig("TEST.png")
# plt.clf
# plt.show()
# 
# 
# # 2. Versicolor Contour Plot: Sepal Length V. Petal Length.
# sns.jointplot(x="sepal_length", y="petal_length", data = versicolor, kind = "kde")
# plt.suptitle("Versicolor: Sepal Length Vs Petal Length")
# plt.savefig("TEST2.png")
# plt.clf
# plt.show()
# 
# # 3. Versicolor Contour Plot: Sepal Width V. Petal Length.
# sns.jointplot(x="sepal_width", y="petal_length", data = versicolor, kind = "kde")
# plt.suptitle("Versicolor: Sepal Width Vs Petal Length")
# plt.savefig("TEST3.png")
# plt.clf
# plt.show()
# 
# # 4. Versicolor Contour Plot: Sepal Length V. Petal Width.
# sns.jointplot(x="sepal_length", y="petal_width", data = versicolor, kind = "kde")
# plt.suptitle("versicolor: Sepal Length Vs Petal Width")
# plt.savefig("TEST4.png")
# plt.clf
# plt.show()
# 
# # 5. Versicolor Contour Plot: Sepal Width V. Petal Width.
# sns.jointplot(x="sepal_width", y="petal_width", data = versicolor, kind = "kde")
# plt.suptitle("Versicolor: Sepal Width Vs Petal Width")
# plt.savefig("TEST5.png")
# plt.clf
# plt.show()
# 
# # 6. Versicolor Contour Plot: Sepal Length V. Sepal Width.
# sns.jointplot(x="sepal_length", y="sepal_width", data = versicolor, kind = "kde")
# plt.suptitle("Versicolor: Sepal Length Vs Sepal Width")
# plt.savefig("TEST6.png")
# plt.clf
# plt.show()
# 
# #==========================================================================================
# # 1. Virginica Contour Plot: Petal Length Vs Petal Width.
# sns.jointplot(x="petal_length", y="petal_width", data = virginica, kind = "kde")
# plt.suptitle("Virginica: Petal Length Vs Petal Width")
# plt.savefig("TEST7.png")
# plt.clf
# plt.show()
# 
# 
# # 2. Virginica Contour Plot: Sepal Length V. Petal Length.
# sns.jointplot(x="sepal_length", y="petal_length", data = virginica, kind = "kde")
# plt.suptitle("Virginica: Sepal Length Vs Petal Length")
# plt.savefig("TEST8.png")
# plt.clf
# plt.show()

# # 3. Virginica Contour Plot: Sepal Width V. Petal Length.
# sns.jointplot(x="sepal_width", y="petal_length", data = virginica, kind = "kde")
# plt.suptitle("Virginica: Sepal Width Vs Petal Length")
# plt.savefig("TEST9.png")
# plt.clf
# plt.show()
# 
# # 4. Virginica Contour Plot: Sepal Length V. Petal Width.
# sns.jointplot(x="sepal_length", y="petal_width", data = virginica, kind = "kde")
# plt.suptitle("Virginica: Sepal Length Vs Petal Width")
# plt.savefig("TEST10.png")
# plt.clf
# plt.show()
# 
# # 5. Virginica Contour Plot: Sepal Width V. Petal Width.
# sns.jointplot(x="sepal_width", y="petal_width", data = virginica, kind = "kde")
# plt.suptitle("Virginica: Sepal Width Vs Petal Width")
# plt.savefig("TEST11.png")
# plt.clf
# plt.show()
# 
# # 6. Virginica Contour Plot: Sepal Length V. Sepal Width.
# sns.jointplot(x="sepal_length", y="sepal_width", data = virginica, kind = "kde")
# plt.suptitle("Virginica: Sepal Length Vs Sepal Width")
# plt.savefig("TEST12.png")
# plt.clf
# plt.show()