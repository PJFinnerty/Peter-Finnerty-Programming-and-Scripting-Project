import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

iris = pd.read_csv('IrisDataset.csv')


class Histogram:
    def __init__(self, bins, feature):
        self.bins = bins
        self.feature = feature

    def graph_hist(self):
        plt.hist(df[feature], self.bins, edgecolor='black')

H1 = Histogram()
H1.bins = [0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 
4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5]
h1.feature = "petal_length"
H1.edge = 'black'


class hist:
    df = iris
    bins = []
    feature = []

    def histograms(self, df, bins, feature):
        

Hist1 = hist(df, [0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 
4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7, 7.25, 7.5], ["petal_length"]
plt.show(Hist1)