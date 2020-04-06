# Peter Finnerty - Project

# This project features an in-depth look at Ronald Fisher's Iris data set. 
# This famous data set investigates three species of Iris flower and contains 
# data on 50 samples of each species. A summary of this data set will be 
# carried out, following this, a qualitative study of each variable complete 
# with specific variable summaries, histograms and scattergrams 
# (contained in .png files) will be completed. 

# Q. Have the script save a histogram of each variable to png files.

# This program will create a histogram of (a)Iris setosa, (b)Iris virginica and (c)Iris versicolor

# I must create a separate histogram for each specias, this will feature 4 variables.

# This is a rough attempt.

# Example code below of McLou for different data - edit for draft...
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("IrisDataset.csv")
#print(df)

df2 = df["eruption"]
print(df2)

# plt.hist(df['sepal_length'], df['sepal_width'])
# plt.title("Sepal Length Vs Sepal Width")
# plt.xlabel("Sepal Length")
# plt.ylabel("Sepal Width")
# plt.show()