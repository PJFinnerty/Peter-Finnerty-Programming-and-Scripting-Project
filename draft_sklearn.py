# Peter Finnerty - Project practice file.
# This file investigates the use of SKlearn on the IRIS dataset.
#----------------------------------------------------------------------

# Part 1 of sklearn research
# The Following research material from: 
# https://github.com/justmarkham/scikit-learn-videos/blob/master/03_getting_started_with_iris.ipynb

import numpy as np

#import load_iris function from datasets module
from sklearn.datasets import load_iris

# Create object 'df' and assign it the load_iris()
# function from sns.
df = load_iris()
type(df)

#print entire dataset
#print(df.data)

# Print 'feature names' attributes
# these are the column headers
print("\n", df.feature_names)  #['sepal length (cm)', 'sepal width (cm)', 
#                                   'petal length (cm)', 'petal width (cm)']

# Print target names
print("\n", df.target_names)  #['setosa' 'versicolor' 'virginica']

# Print targets
print("\n", df.target) #[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#                        0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#                        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
#                        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#                        2 2]

# Check the type of features and response.
print("\n", type(df.data) )     #<class 'numpy.ndarray'>
print("\n", type(df.target) )   #<class 'numpy.ndarray'>

# Check the shape of the features (1st dimension = no. of observations
#                                   2nd dimension = no. of features)
print("\n", df.data.shape)    #(150, 4)

# Check the shape of the response (single dimension matching the no. of obvs.)
print("\n", df.target.shape)  #(150,)

# Store feature matrix in X (capitalised to rep. matrix)
X = df.data

# Store response vector in y
y = df.target

# LOOKUP:
# Sklearn Dataset Loading utilities,
# Jake VanderPlas: Fast Numerical Computing
# Scott SHell: Intro to NumPy
#-------------------------------------------------------------------------

# Part 2 of sklearn research
# Material from: https://github.com/justmarkham/scikit-learn-videos/blob/master/04_model_training.ipynb

# import load_iris function from datasets module
from sklearn.datasets import load_iris

# Save "bunch" object containing iris dataset and its attributes.
df = load_iris()

# Store feature matrix in "X".
X = df.data

# Store response vector in "y".
y = df.target

# Print the shapes of X and y
print(X.shape)   #(150, 4)
print(y.shape)   #(150,)

# Sklearn 4-step modelling patter:

# STEP 1: Import the class you plan to use.
from sklearn.neighbors import KNeighborsClassifier

# STEP 2: "Insantiate" the "estimator".
# "Estimator" is sklearn's term for model and Instantiate means 'make an instance of'.
knn = KNeighborsClassifier(n_neighbors=1)  #Where n_neighbours is a tuning parameter. 

# Checking the default values for unspecified parameters.
print(knn) #KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#           metric_params=None, n_jobs=None, n_neighbors=1, p=2,
#           weights='uniform')

# STEP 3: Fit the model with data (aka "model training")
# Here the model learns the relationship between the features and the response (X and y).
# Occurs in-place.

# Use fit-method on knn object and pass X and y objects.
knn.fit(X, y) #KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#              metric_params=None, n_jobs=None, n_neighbors=1, p=2,
#              weights='uniform')

# STEP 4: Predict the response for a new observation.
# We input a measurement for an unknown iris and asking the fitted model to predict species 
# based on what has been learned in previous steps. Predict method used on knn object and pass features of
# unknown iris as a list. Numpy will convert this list to an array.

import numpy as np

print(knn.predict( [[3, 5, 4, 2]] ) )  #[2]

# Given that sklearn will not keep track of the fact that 2 is the encoding for Virginica and therefore,
# Virginica is the predicted species for the unknown Iris.

# Returns a NumPy array
# Can predict for multiple observations at once

X_new = [[3, 5, 4, 2], [5, 4, 3, 2]]
knn.predict(X_new) 

print(knn.predict(X_new) )  #array([2, 1])

### Using a different value for K:
# instantiate the model (using the value K=5)
knn = KNeighborsClassifier(n_neighbors=5)
  
# fit the model with data
knn.fit(X, y)

# predict the response for new observations
knn.predict(X_new)    #array([1, 1])
  
###  Using a different classification model:
# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

#  fit the model with data
logreg.fit(X, y)
  
# predict the response for new observations
logreg.predict(X_new)   #array([2, 0])








