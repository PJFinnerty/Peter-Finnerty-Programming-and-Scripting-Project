import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


df = pd.read_csv('IrisDataset.csv')
# def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

class histogram:
    df = 0
    SW = 0
    bins = []

    def graph(self, df, SW, bins):
        return plt.hist(SW, bins = [ ])

p1 = histogram()
SW = df["sepal_width"]
bins = [0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 
4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5]


bins = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75]
plt.hist(df["petal_width"], bins = bins, edgecolor='black')


#--------------------------------------------------------
# Peter Finnerty - Project 2020
# Write a program called analysis.py that:
# • outputs a summary of each variable to a single text file,
# • saves a histogram of each variable to png files, and
# • outputs a scatter plot of each pair of variables.
#-----------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

iris = pd.read_csv('IrisDataset.csv')

bins = [0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 
4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5]
plt.hist(iris["petal_length"], bins = bins, edgecolor='black')

class hist:
    df = iris
    bins = []
    feature = []

    def histograms(self, df, bins, feature):
        return plt.hist(df[feature], bins=bins, edgecolor='black')
Hist1 = hist(df, [0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 
4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5], ["petal_length"])
    

class Point3D():
    x = 0
    y = 0
    z = 0
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)             
p1 = Point3D(5.1, 3.4, 2.0)
print(p1.distance() )



# Create hist with bin measures set to bins list.
bins = [0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 
4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5]
plt.hist(df["petal_length"], bins = bins, edgecolor='black')
# Set the histrogram style.
plt.style.use('fivethirtyeight')

# Format the histogram as appropriate.
plt.title("Petal Length of Iris Flowers")
plt.xlabel('Petal Length (cm)')
plt.ylabel('No. of observations')
plt.tight_layout()
plt.legend()
# Mark out a median value line.
# median_PL = 4.35
# color = '#fc4f30'
# plt.axvline(median_PL, color=color, label='Median Petal Length', linewidth=2.5)
plt.savefig("Hpetal_length.png")
plt. clf
plt.show()
