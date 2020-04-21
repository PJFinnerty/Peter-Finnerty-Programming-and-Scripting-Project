# Programming-and-Scripting-Project
## Summary
This project features an in-depth look at Ronald Fisher's Iris data set. This famous data set investigates three species of Iris flower: Iris Setosa, Iris Versicolor and Iris Virginica. The dataset is split into 5 columns: 'sepal_length', 'sepal_width', 'petal_length', 'petal_width' and 'species', where the first four columns represent the 4 features of the Iris flower that have been recorded and the fifth column containing the specific species. There are 150 rows, detailing 150 different 'observations' of the 4 features. For each of the 3 types of species, 50 observations are recorded. A study of the 'responses' (or targets) of the dataset, reveals that the values contained are in a finite and unordered set. Therefore, the dataset represents a classification problem.
The Iris dataset is often called a 'toy' dataset, as it is relatively simple, involves the examination of just 1 csv file and it has a relatively small amount of 'vectors'. Nevertheless, basic data science knowledge is still required to carry out the core purpose of the dataset: distinguishing of one Iris species from another based upon the observations made of the 4 features.

## Research Plan
- 1. Prior to beginning work on this project I researched the technicalities of plotting with Matplotlib. This research was intended as a way to familiarise myself with the module and get a sense of how the core tasks of this project would be undertaken, as well as an understanding of how to further examine the dataset and effectively distinguish between the 3 Iris species. Utilising a free resource from appliedaicourse.com entitles 'Exploratory Data Analysis (EDA), I researched the Iris Dataset firstly in terms of how to represent the data in histograms and scattergrams, as well as more advanced plotting tools such as violin plots and CDF/PDF graphs. I recorded this study in a text file entitled eda.txt. This consisted of over 4000 words and was a strong foundation from which to base my own study of the Iris Dataset. Further research was carried out on the utilisation of python modules that work in conjunction with 'Matplotlib', such as 'Seaborn', 'Pandas' and 'SciKitLearn'.

- 2. I then set about downloading the dataset from a reliable source ("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv") as a csv. Following this, I created separate draft files for the respective questions. The project required 4 histograms to be created, one for each feature. I initially created these histograms in 4 separate files. The project also required the production of 6 scattergrams, one of each possible pair of features, which were created in 6 separate files initially. After I was satisfied with the histograms and scatterplots, I amalgamated the various files into one under the title 'Analysis.py'. 

- 3. For each variable of the dataset, I outputed a summary of the variable to a single text file. This action was done from within 'Analysis.py'.

### Work Yet to be carried out.
- 4. It is intended to create graphs that outline trends not visible in the histograms and scatter plots. Using the research so far, I will utilse linear separation, violin plots and pair plots to further distinguish the 3 species of Iris flower. 'Seaborn' will be used in creating these graphs. Following this, I intend to employ basic machine learning knowledge in doing so. 'Sklean' will be a core utility in accomplishing this. By indexing each observation according to what species it represents, I will be able to more accurately create separation. 

## Content

-**Analysis.py** - The core python file, containing the scripts for creating the plots of this project.

- **.gitignore** - a list of words for 'git' to ignore.

- **IrisDatase.csv** - The csv file of Fisher's Iris Dataset used in this project. This version was found @ https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

- **LICENCE** - The Licence of the project (MIT).

- **practiceseaborn.py** - A practice file used to test certain scripts to be added to the project.

- **READEME.md** - This MarkDown file summarising the project.


