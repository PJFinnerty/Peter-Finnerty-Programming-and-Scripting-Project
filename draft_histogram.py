# Peter Finnerty - Project

# This project features an in-depth look at Ronald Fisher's Iris data set. 
# This famous data set investigates three species of Iris flower and contains 
# data on 50 samples of each species.
# Q. Have the script save a histogram of each variable to png files.

# This program will create a histogram of (a)Iris setosa, (b)Iris virginica and (c)Iris versicolor

# I must create a separate histogram for each specias, this will feature 4 variables.

# This is a rough attempt.

# Example code below of McLou for different data - edit for draft...
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

print(df.shape) # (150, 5)

print(df.columns) # Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
# 'species'], dtype='object')

print(df["species"].value_counts() ) # virginica     50, setosa        50, versicolor    50
# Name: species, dtype: int64
#-------------------------------------------------------------------------------------
