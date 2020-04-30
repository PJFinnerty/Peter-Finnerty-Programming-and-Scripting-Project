# Programming-and-Scripting-Project
## Summary
This project features an in-depth look at Ronald Fisher's Iris data set. This famous data set investigates three species of Iris flower: Iris Setosa, Iris Versicolor and Iris Virginica. The dataset is split into 5 columns: 'sepal_length', 'sepal_width', 'petal_length', 'petal_width' and 'species', where the first four columns represent the 4 features of the Iris flower that have been recorded and the fifth column containing the specific species. There are 150 rows, detailing 150 different 'observations' of the 4 features. For each of the 3 types of species, 50 observations are recorded. A study of the 'responses' (or targets) of the dataset, reveals that the values contained are in a finite and unordered set. Therefore, the dataset represents a classification problem.
The Iris dataset is often called a 'toy' dataset, as it is relatively simple, involves the examination of just 1 csv file and it has a relatively small amount of 'vectors'. Nevertheless, basic data science knowledge is still required to carry out the core purpose of the dataset: distinguishing of one Iris species from another based upon the observations made of the 4 features.

## Research Plan and Methodology

### Identifying the Scope of the Analysis
- 1. Prior to beginning work on this project I researched the technicalities of plotting with Matplotlib. This research was intended as a way to familiarise myself with the module and get a sense of how the core tasks of this project would be undertaken, as well as an understanding of how to further examine the dataset and effectively distinguish between the 3 Iris species. Utilising a free resource from 'appliedaicourse.com' entitled 'Exploratory Data Analysis (EDA)', I researched the Iris Dataset firstly in terms of how to represent the data in histograms and scattergrams, as well as more advanced plotting tools such as contour plots and CDF/PDF graphs. I recorded this study in a text file entitled eda.txt. This consisted of over 4000 words and was a strong foundation from which to base my own study of the Iris Dataset. Further research was carried out on the utilisation of python modules that work in conjunction with 'Matplotlib', such as 'Seaborn', 'Pandas' and 'SciKitLearn'. However, it was decided that this project would deal with the univariate and bivariate analysis of the Iris Dataset using the Seaborn module. The graphs would be plotted in the 'stateful' form as it was decided that there would not need to be a high degree of complexity to the graphs that were created. 

- 2. I then set about downloading the dataset from a reliable source ("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv") as a csv. Following this, I created separate draft files for the respective questions. The project required 4 histograms to be created, one for each feature. I initially created these histograms in 4 separate files. The project also required the production of 6 scattergrams, one of each possible pair of features, which were created in 6 separate files initially. After I was satisfied with the histograms and scatterplots, I amalgamated the various files into one under the title 'Analysis.py'. 

- 3. For each variable of the dataset, I outputed a summary of the variable to a single 'Mark Down' file. This action was done from within 'Analysis.py'. In order to do this I used the 'sys.stdout' to redirect print statements sent to the command line to the file 'Summary.md'. I ordered the print statements in the specified Mark Down format, prefixing titles with hashtags to ensure they stand out and encapsulating specific text in asterixes in order to print it in bold.  

### Univariate Analysis 
For the univariate analysis (the plotting of 1 feature at a time), I decided to use a comparison of histograms and Cumulative Density Functions (CDF's) and attempt to distinguish the species as best I could. Univariate analysis was carried out by first investigating the profile of the histograms of the features, specifying the distribution of the species and then referencing this to the CDF of each feature. These figures were saved to the repository, along with the other supplementary plots, however, I ensured that the supplementary plots appeared in the botton of the repository, whilst the histogram and scatter plot 'png' files were placed at the top, to allow for a clear layout of the repository. In this part of the analyis, Iris Setosa was successfully distinguished in terms of Petal Length and Petal Width from the other two species.  The histograms displayed a high degree of separation and the CDF plots confirmed this with a high probability of separation for each feature. Iris Setosa was not successfully distinguished in terms of the 2 Sepal features. Iris Versicolor and Virginica were compared with specific focus on the CDF plots of each species, in subplots that placed them side by side within the same figure. It was noted that for Petal Length and Petal Width, Versicolor and Virginica had moderate overlap, whilst for Sepal Length and Sepal Width, there was a large degree of overlap of vectors. As such Versicolor and Virinica were not successfully distinguished relevant to any of the 4 features under univariate analysis. Bivariate analysis would therefore be required to distinguish Setosa in terms of Sepal Length and Sepal width and for all 4 features of Versicolor and Virginica.

### Bivariate Analysis
Bivariate analysis was carried out by utilising scatter plots and contour plots. Each combination of variable pair was plotted in 6 scatter plots. For Iris Setosa, investigation of the scatter plots that featured Sepal Length and Sepal Width were sufficient to distinguish the species. As Versicolor and Virginica displayed a higher degree of overlap, each scatter plot was compared with a contour plot, plotting 2 features and a single species at a time. By investigating the contour plots, areas of dense population of measurements were identified separately for Versicolor and Virginica. Linear separation was then carried out on each scatter plot, taking into consideration both the position of the most dense regions for each species and where drawing the line would result in the least amount of outlier vectors. For each scatter plot a line of regression was drawn and the probability of incorrect classification on either side of the line was calculated. This calculation aided in a result that indicated whether the species had been distinguished to a high degree, a moderate degree or were not distinguished successfully. For 5 of the 6 scatter plots, linear separation was achieved to some degree. However, for the plot of Sepal Length V. Sepal Width, linear regression was not successful. As such it is in this category alone that Versicolor and Virginica have not been distinguished.

## Conclusion
Through the use of 'stateful' plotting in the Seaborn module, I have successfully plotted a histogram of each Iris feature and a scatter plot of each possible feature pair. I have also saved each feature to png. files available in the projet repository. Following this I utilised a framework of analysis provided by my EDA research, to distinguish the Iris species from one another to varying degrees of success, first under univariate analysis and then under bivariate analysis. In this project, the 'stateful' method of plotting in Matplotlib was successfully employed in favour of less complicated by highly stylised plots. Furthermore, a basic understanding of statistical analysis was displayed in the information outputted to 'Summary.md'. 

## Content

- **_Hist_petal_length.png** - Histogram png. file of Petal Length of all species, as output from 'Analysis.py'.

- **_Hist_petal_width.png** - Histogram png. file of Petal Length of all species, as output from 'Analysis.py'.

- **_Hist_sepal_length.png** - Histogram png. file of Petal Length of all species, as output from 'Analysis.py'.

- **_Hist_sepal_width.png** - Histogram png. file of Petal Length of all species, as output from 'Analysis.py'.

- **_Scatter1.png** - Scatterplot png. file of Petal Length and Petal Width, as output from 'Analysis.py'.

- **_Scatter2.png** - Scatterplot png. file of Petal Length and Sepal Length, as output from 'Analysis.py'.

- **_Scatter3.png** - Scatterplot png. file of Petal Length and Sepal Width, as output from 'Analysis.py'.

- **_Scatter4.png** - Scatterplot png. file of Petal Width and Sepal Length, as output from 'Analysis.py'.

- **_Scatter5.png** - Scatterplot png. file of Petal Width and Sepal Width, as output from 'Analysis.py'.

- **_Scatter6.png** - Scatterplot png. file of Sepal Length and Sepal Width, as output from 'Analysis.py'.

- **.gitignore** - a list of words for 'git' to ignore.

- **Analysis.py** - The core python file, containing the scripts for creating the plots of this project.

- **CDF_Setosa.png** -  CDF and PCF png. file of Petal Length of all Setosa, containing a figure with 4 subplots, 1 for each Iris feature.

- **CDF_Virg_V_Vers1.png** - CDF and PCF png. file of Petal Length of all species, containing a figure with 4 subplots of the Petal features, 2 for Versicolor and 2 for Virginica.	

- **CDF_Virg_V_Vers2.png** - CDF and PCF png. file of Petal Length of all species, containing a figure with 4 subplots of the Sepal features, 2 for Versicolor and 2 for Virginica.

- **EDA.md** - Research notes I rescored from undertaking 'EDA' course @ https://www.appliedaicourse.com/course/11/Applied-Machine-learning-course

- **IrisDatase.csv** - The csv file of Fisher's Iris Dataset used in this project. This version was found @ https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

- **LICENCE** - The Licence of the project (MIT).

- **READEME.md** - This MarkDown file outlining the project contents and methodology.

- **Summary.md** - The results of univariate and bivariate analysis of the Iris Dataset. The contents of this file are outputted from 'Analysis.py'.

- **Vers_Contour1.png** - Versicolor contour png. file of Petal Length and Petal Width, as output from 'Analysis.py'.

- **Vers_Contour2.png** - Versicolor contour png. file of Petal Length and Sepal Length, as output from 'Analysis.py'.	

- **Vers_Contour3.png** - Versicolor contour png. file of Petal Length and Sepal Width, as output from 'Analysis.py'.	

- **Vers_Contour4.png** - Versicolor contour png. file of Petal Width and Sepal Length, as output from 'Analysis.py'.	

- **Vers_Contour5.png** - Versicolor contour png. file of Petal Width and Sepal Width, as output from 'Analysis.py'.	

- **Vers_Contour6.png** - Versicolor contour png. file of Sepal Length and Sepal Width, as output from 'Analysis.py'.	

- **Virg_Contour_1.png** - Virginica contour png. file of Petal Length and Petal Width, as output from 'Analysis.py'.

- **Virg_Contour_2.png** - Virginica contour png. file of Petal Length and Sepal Length, as output from 'Analysis.py'.

- **Virg_Contour_3.png** - Virginica contour png. file of Petal Length and Sepal Width, as output from 'Analysis.py'.	

- **Virg_Contour_4.png** - Virginica contour png. file of Petal Width and Sepal Length, as output from 'Analysis.py'.

- **Virg_Contour_5.png** - Virginica contour png. file of Petal Width and Sepal Width, as output from 'Analysis.py'. 	

- **Virg_Contour_6.png** - Virginica contour png. file of Sepal Length and Sepal Width, as output from 'Analysis.py'. 	

README.md	Summary 



ddd.py	Completed bivg
summary.md	Completedg
 README.md


Type	Name	Latest commit message	Commit time
.gitignore	Initial commit	25 days ago
Analysis.py	Completed bivariate analysis, and outputed to 'Summary.md'. Deleted d…	16 hours ago
