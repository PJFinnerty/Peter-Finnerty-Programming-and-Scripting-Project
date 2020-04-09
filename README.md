# Programming-and-Scripting-Project
This project features an in-depth look at Ronald Fisher's Iris data set. This famous data set investigates three species of Iris flower and contains data on 50 samples of each species. A summary of this data set will be carried out, following this, a qualitative study of each variable complete with specific variable summaries, histograms and scattergrams (contained in .png files) will be completed. 

## Content
- **.gitignore** - a list of words for 'git' to ignore.

- **IrisDatase.csv** - The csv file of Fisher's Iris Dataset used in this project. This version was found @ https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

- **LICENCE** - The Licence of the project (MIT).

- **practiceseaborn.py** - A practice file used to test certain scripts to be added to the project.

- **READEME.md** - This MarkDown file summarising the project.

**DRAFT MATERIAL**

## Facts on Iris Dataset
This is a balanced dataset because there is an equal quantity of datapoints or vectors for each variable.

## References: 

### Notes 1-3 below focus on the use of SCATTERGRAMS with Seaborn.
**The draft copy for scattergrams in this repository is 'draft_scattergram.py'.** 

**1. Notes on linear separation of SL and SW of 3 species.**

**1(a):**
- The results of the scatter of SL and SW show that Setosa can
 be distinguised - by drawing a line to separate them from Versicolour and Virginica. Setosa show a trend towards greater sepal width and slightly shorter sepal width than the other species.
 Setosa are therefore linearly separable. 
**1(b):**
 To imporve on this ovservation, using a 3-d model and adding in a measure of PL, setosa can be separated from the other species more accurately by drawing a 3-d 'plane'.

**2. 3-d models.**

**2(a):**
- Another benefit of a 3-d model, of SL, SW and PL, is that virginica and versicolour can also be distinguished with a plane, with Virginica showing a trend of PL that is slightly higher. It must be noted that there is some crossover of Virginica vectors across this plane, i.e. there are some data points of Virginica mixed with the Versicolour. 
- A drawback of 3-d is that it is not possible to represent them clearly. Making 3-d more valuable than 3-d.

**3. Models.**

**3(a):**
- The use of pairplots can be used to represent 4-d datasets.
- We take the variables in pairs of 2 - this gives us 4-C{2} - in this data set there are 6 such plots. 

**3(b):**
- The following script is found in 'practiceseaborn.py', it creates a pairplot of the Iris variables:
* sns.set_style("whitegrid")
* sns.pairplot(df, hue = "species", height = 3)
* plt.show() 

**3(c):**
- It is seen from the graph that Setosa flowers are most explicitely distinguised from the others, by plotting PL and PW. This leaves them grouped closely as both PL and PW are smaller in Setosa. 

**3(d):** 
- When looking at the PL by PW scatter plot, we can use an if statement to separate the Setosa group - this is preferred to using a line as it more accurately reflects the relative small Petal sizes in Setosa plowers.
Script from 'draft_scattergram.py' (line 44):
* if PL <= 2:
 *   & PW <= 1

**3(e):** 
- Below script from 'draft_scattergram.py', line 48:
- if PW <= 2:
-    & PW >= 1 
- if PL < 5:
-    & PL > 2.5

- We must do a Boolean 'And' of these 4 statements in order to distinguish Versicolour. 
It must be noted that there will be some Virginica vectors included in this calculation.

**3(f):**
- It is evident from the pairplot of the Iris Dataset that PL and PW are the most useful at distinguishing the species from one another. Setosa can be distinguised by it's short PL and PW using linear separation. Virginica and Versicolour have some overlap, but using simple 'if, else' statements they can be dinstinguised with reasonable accuracy.

### Notes 4-() below focus on the use of HISTOGRAMS.
**The draft copy for histogram in this repository is 'draft_histogram.py.**

### **4. Determining which of the variables is useful in distinguishing the 3 species.**
**4(a):**
- Distinguishing the species can be done using 'univariate analysis' and 'probability density function' or 'histograms'.
- Taking a histogram of each of the 4 variables, and on each histogram having all 3 species represented together, we can figure out the most 'useful' variable.

**4(b): Petal Length Histogram:**
- Through analysis of Setosa PL and PW in scattergram PairPlots it has already been demonstrated that Setosa has a low value in both of these variables. Specifically looking at hte hostogram of PL of Setosa, it is noted that there are no Setosas with a value greater than 2.
- In this case a high peak, representing the whole distribution is seen for Setosa PL. There is some separation between Versicolour and Virginica.

**4(c): Petal Width Histogram:**
- Looking at PW, we see that Setose has a very tiny overlap with Versicolour (at 0.5). It is noted that the more separated the histogram bars (peaks) are, is wanted. Therefore, PW is preferred as a distinguishing variable compared to PW.

**4(d): Sepal Length Histogram:**
- With SL, we see a massive overlap between each of the variables. Ther is a very close distribution in both the Setosa/Versicolour pair and the Versicolour/Virginica pair. This makes both PL and PW much better than Sepal Length at the above task.

**4(e): Sepal Width Histogram:**
- It is immediately clear looking at the histogram of SW, that this is the least useful variable in distinguishing species.

**4(f): Order of Preference in Histograms:**
- Petal Length > Petal Width (slightly better)
- Petal > Sepal Length (a good deal better)
- Sepal Length >> Sepal Width (far better - Sepal width shows distribution of species practically ontop of one another).
- PL > PW > SL >> SW

### **5. Mean, Variance and Standard Deviation (Std-dev) - Related to file 'draft_mean.py'.**

**5(a): The Mean of the Petal Length Observations**
- Looking at Setosa PL, there are 50 obserrvations. The symbol for mean is 'μ'.
- Therefore,where s = setosa and x' is equal to an observation and n = nubber of observations,
we can calculate the mean with the following equation:
**μsPL = x1 + x2 + x3 ... xn / n**

- The mean of each species can be calculated with the follow script:
- print(np.mean(df_setosa ["petal_length"] ) )
- print(np.mean(df_virginica ["petal_length"] ) )
- print(np.mean(df_versicolor ["petal_length"] ) ) 

- It is clearly noticed that setosa has the smallest petal length. We can now see the exact figure to be 1.464.
- The use of mean is known as 'central tendency'. Just 1 'outlier' can lead to the mean misrepresenting the data.

**5(b): The Variance:**
- Looking at the histogram of Setosa flowers it is seen that the 'spread' (or range), is relatively small, we can calculate the spread of Setosa vectors, which is a more reliable number. This 'spread' is more accurately described ad VARIANCE.
- Variance = σ ** 2 = ∑**n [i=1](xi - μ) **2 / n
- **Therefore the variance is the average squared distance of each point (vector) from the mean value.**

**5(c): Standard Deviation**
- The square root of variance is the Standard Deviation (Std-dev).
- **Std-dev tells us the average deviation of points from the mean value.**
- If the Std-dev is small, the 'spread' is small.

- print( "\nStd-dev: ")
- print(np.std(df_setosa ["petal_length"] ) )
- print(np.std(df_virginica ["petal_length"] ) )
- print(np.std(df_versicolor ["petal_length"] ) 

- We see from looking at the outputs from the above print statements, that Setosa (0.171767) has a small Std-dev and that of Virginica (0.546347) and Versicolour (0.465188) is greater.
- With both Std-dev and Variance, an outlier can also corrupt the data.

### 6. **Median**
**6(a):**
- Unlike the Mean value, computing the 'Median', even with the presence of an outlier, gives us a value that is not as affected.
- The median of Setosa PL is 1.5 when there is NO outlier, with an outlier, it is still 1.5.
- The median value tends to look similar to the mean value or 'central tendency'.

**6(b):Calculating The Median**
- Take 7 values: x = {1, 1.2, 1.1, 2.1, 1.8, 1.6, 1.2}
- The same values in order = { 1, 1.1, 1.2, 1.2, 1.6, 1.8, 2.1}
- Pick the middle value = 1.2
When there is an odd number of vectors, you take the number of vectors, add 1 and divide by 2 - this gives you the index where the middle value is found. **The middle value IS the median.**
- **Median = n + 1 / 2**
- Median of x = 1.2

- When the number of vectors is even, there is a different method.
- x = {1, 1.1, 1.2, 1.2, 1.6, 1.8, 1.8, 2.1}.
- Here you CANNOT use 'n+1 / 2' as this gives you an intermediate index position.
- Instead you take the two middle index values and calculate the mean of them.
- Mean of 1.2 and 1.6 = 1.4

**6(c): Median and Outliers.**
- In the above sets, if there was a final vector with a value of 50, the outcome of the median would be the same, this is because the same method of calculation applies. 
- However, if more than 50% of the vectors are corrupted the Median will be corrupted.
- x = {1, 1.1, 1.2, 5, 10, 20, 30}
- In this list, 4 points are corrupted' and there are only 3 reliable figures (1, 1.1, 1.2).
- This will put 5 as the Median value due to its index.
- In conclusion, the Median is useful only when more 50% of the vectors are 'good' data points.

**6(d): Script for Median Calculation.**
- print("\nMedians: ")
- print(np.median(df_setosa ["petal_length"] ))

Below is a median with an outlier:
- print(np.median(np.append(df_setosa["petal_length"], **50** ) ) )

- print(np.median(df_virginica["petal_length"] ))
- print(np.median(df_versicolour["petal_length"] ))

### 7. ** Quantiles and Percentiles.**
**7(a): Quantiles.**
- Take a sorted dataset with 100 values, sprted = s: xS = {1, 2, 3, 4 ... 100}
- Median x = take the 2 middle values, 50 & 51, find the mean of these two numbers.

- In the above example of 100 values, the 50th is known as **the 50th percentile value**. This holds true if the values of each of the 100 vectors were different - the 50th percentile of x corresponds to the 50th rank in the list.  
- Therefore, the 50th percentile is basically the same as the median value.

- If you are looking for the 10th percentile, you look for the 10th position in a sorted list of 100 values. This figure essentially tells you that 10% of vectors are roughly less than this value, and 90% of vectors are greater.

- The Quantiles include the 25th, the 50th, the 75th and the 100th percentile.
- The 50th percentile (or second quantile) is also the median

**7(b): Calculating the Quantiles in code.**
- The below script calculates in order the Quantiles. Each output for each statement is also provided (in bold).

- print("\nQuantiles: ")
- print(np.percentil(df_setosa["petal_length"], np.arange(0, 100, 25) ) )
- **1.0   1.4   1.5    1.575**
- print(np.percentil(df_virginica["petal_length"], np.arange(0, 100, 25) ) )
- **4.5   5.1   5.55   5.875**
- print(np.percentil(df_versicolor["petal_length"], np.arange(0, 100, 25) ) )
- **3.    4.    4.35   4.6**

- **7(c): Calculating the Percentiles in code.**
- The below script calculates in order the percentiles. Each output for each statement is also provided (in bold).

- print("\n90th Percentiles: ")
- print(np.percentile(df_setosa["petal_length"], 90) )
- **1.7**
- print(np.percentile(df_virginica["petal_length"], 90) )
- **6.31**
- print(np.percentile(df_versicolor["petal_length"], 90) )
- **4.8**

- It should be noted in the above statements that the 0th to 75th Percentile inclusive are being calculating, as the first index in the numpy arange is 0. It is possible to calculate the 25th - 100th percentile (or 1st quantile to 4th quantile inclusive) by altering this array.

- When working with very large datasets, using the higher percentiles, such as 95th or 99th percentiles can be very useful, to understand waiting times for delivery to a large number of customers for example.

### **8. Box Plots - refer to file 'draft_boxplot.py'**
- **8(a): Understanding Box Plots.** 
- The tool we use to represent percentiles and quantiles in a 2-d graph is Box Plots. 

- E.g.:
- sns.boxplot(x = 'species', y = 'petal_length', data = df)
- plt.show()

- The above script will display a box plot of the petal length of the 3 species. Each box consists of a coloured box with 3 horizontal lines running parralel to the x axis. The lowest line correspoinds to the 25th percentile value of the relevant species, the second line corresponds to the 50th and the highest line, the 75th.
- Note: the width of the plots has no significance.

- The core use of box plots is to be able to scale the percentile markers off of the reading on the Y value (in the above example the petal length). Therefore, if you set a 'threshold' at 5 for example, you may be able to calculate, what percentage of the 'virginica' set had a petal length greater than 5. This introduces a level of specificity not seen in other plots. The effectiveness of the information you can extropolate from a box plot often depends on how wisely you have chosen your threshold.

- **8(b): Whiskers.**
- The extended 2 lines shooting out of the box are called 'the whiskers'. Some modules calculate these whiskers by taking 1.5 the IQR value (25th to 75th percentiles). They may also be drawn based on the max and min values of the set.
- Normally the whiskers represent the range within which most of a species vectors are located.
