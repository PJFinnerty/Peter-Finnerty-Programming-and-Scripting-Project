import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import seaborn as sns

# IMmport data
data = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv", names=['f1', 'f2', 'f3', 'f4', 'f5'] )
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

data=data.iloc[np.random.permutation(len(data) )]
print(data)

x_input=data.ix[0:105,['f1', 'f2', 'f3', 'f4']]
temp=data['f5']
y_input=temp[0:106]
# Test data
x_test=data.ix[106:149, ['f1', 'f2', 'f3', 'f4']]
y_test=temp[106:150]

# Placeholders and variables, input has 4 features and output has 3 classes.
x=tf.placeholder(tf.float32, shape=[None, 4] )
y_=tf.placeholder(tf.float32, shape=[None, 4] )

#weight and bias.
W=tf.Variable(tf.zeros( [4, 3] ))
b=tf.Variable(tf.zeros( [3] ) )

#Model 
y = tf.nn.softmax(tf.matmul(x, W) + b)

#loss function
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ *tf.log(y), reduction_indices=[1]) )
