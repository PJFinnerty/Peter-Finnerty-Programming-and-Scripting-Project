## Research: Notes 1-12 below from  'Appliedaicourse.com - Plotting for exploratory data analysis (EDA)' - https://www.appliedaicourse.com/course/11/Applied-Machine-learning-course

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
- Through analysis of Setosa PL and PW in scattergram PairPlots it has already been demonstrated that Setosa has a low value in both of these variables. Specifically looking at histogram of PL of Setosa, it is noted that there are no Setosas with a value greater than 2.
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
- Therefore,where s = setosa and x' is equal to an observation and n = number of observations,
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

### 7. ** Quantiles, Percentiles, MAD and IQR.**
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

- **7(d):Median Absolute Deviation.**
- We have looked at Std-dev and that it is the average distance of each of the vectors from the mean value of the dataset. Or more specifically, Std-dev tells us what is the typical deviation of each point from the mean. 

- Median Absolute Deviation is undetstood by taking the median point, and imagining one point either side, X2 on the left, and X1 on right. If you want to know the distance between X1 and the median you would calculate Xi - Median. This calculation will tell you the deviation. Since the calculated deviation is required to be positive, you will calculate from X1 as this will give you a positive, or absolute result. 
- The term Median in MAD, tells us that you are looking for the median of the absolute deviations of all the points being investigated against the median. Takke the median, for each point measure its distance from the median and compute absolute values so that both positive and negative values are resulted.
- We care about the distance, not the sign. 
- MAD does the same thing as Std-dev - measuring how far away a point is from the 'central tendency' - however it is calculated from the Median, not the Mean - therefore, it is less likely to be corrupted by an outlier. 

- **7(e):**
- Scripting for the MAD of PL of the 3 species; import robust module first:
- **from statsmodels import robust** 

- **print("\nMedian Absolute Deviation")**
- **print(robust.mad(df_setosa["petal_length"]))**
- **print(robust.mad(df_virginica["petal_length"]))**
- **print(robust.mad(df_versicolor["petal_length"]))**

- To conclude: Median is the equivalent of Mean, except Median does not face corruption with 'outliers',
whilst Median Absolute Deviation is one idea which is equivalent to Standard Deviation.

- **7(f): Inter-Quartile Range (IQR).**
- IQR is found by taking the 75th percentile value and subtracting the 25th percentile value.
- E.g. 75th Percentile of Setosa PL = 1.575, 25th Percentile of PL = 1.4, therefore IQR = 0.175.
- Understanding IQR is useful because within this range, lies 50% of your data. 

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

### 9. **Cumulative Distribution Function (CDF)**
- **9(a):Diffrence between Probability Density Function and CDF:**
- As graphed on line graph of Petal Length (Setosa) against probabilities.
- Reference graph of CDF uses versus PDF uses found in supporting material document.
- Probability plots always start at 0 at the bottom of Y axis and end with 1.0 at the toop of Y axis.
- Both CDF and PDF can both be plotted on porbability plots.
- With CDF plot, find a point on the CDF line and draw a horizontal line cutting to the Y axis, and a verticle line cutting to the X axis (in this example the X axis is Petal Length).
- A reading of 1.6 on the X axis and of 0.82 on the Y axis tells you that 82% of Setosa flowers have a petal length of 1.6 or lower.

- **9(b): How are CDFs Built?**
- A PDF is basically a 'smoothed' out histogram.
- The Y axis probability tells us the percentage of vectors in the set that have X length of Petal or less.
- Looking again at a plot of Setosa Petal length probability, taking an X value of 1.6, say you have 41 Setosa flowers with PL of 1.6 or less, dividing 41 by the total number of vectors gives you the corresponding Y value, 0.82 (82%), this can then be marked on the Y axis. You repeat this for every X value or measurement of PL in Setosa and the range of PL and corresponding probability for each individual point gives you the CDF line.

- Another way to build CDF, is by looking at the PDF line (which counts how many flowers have a certain petal length) calculating this for each PL, (as histograms do) and adding the associated PDF Y values together up to a certain point on the graph. 
- Thinking back to the bars on the histogram, imagine there are 6 bars of varying heights up until the X value Petal Length of 1.6, for each bar, adding the associated Y value probabilities together will give you the CDF value up until PL 1.6. 
- In this case CDF lines are similar to percentiles in that they tell you the cumulative probability of the presence of PL up until a certain X-value point.
- Even though it is not intuitive looking at a graph with a PDF and a CDF graph, by taking points on both curves that allign with the same X-value point - from this point the CDF is not only seen on the CDF line, but also the entire area under the PDF curve - this area as a whole is equal to the CDF.
- This is more easily understood by saying that if you 'differentiate' the CDF, you get the PDF.
AND
- If you do 'integration' on the PDF you get the CDF. 

- **9(c): Code for PDF and CDF.**
- Compute and plot PDF of petal_length:
- **counts_bin_edges = np.histogram(df_setosa['petal_length'], bins = 10, density = True)**
- **pdf = counts / (sum(counts) )** - this line specifically computes PDF.
- **print(pdf)**
- **print(bin_edges)**
 
- Compute the CDF:
- **cdf = np.cumsum(pdf)** - This line features the cumulative sum function of Numpy.
- Plotting CDF:
- **plt.plot(bin_edges[1:], pdf)**
- **plt.plot(bin_edges[1:], cdf)**

- **9(d): How is CDF Useful?**
- Taking a plot featuring both PDF and CDF of each of the 3 species (6 curves on 1 graph), and imagining you had no prior knowledge of the Iris dataset, you can immediately determine what the highest vector is for each species. 
- You can therefore say  for example, that 100% of setosa flowers have a PL of < 2. 

- Analysing Virginica and Versicolor is more difficult. But still provides valuable insights.
- You can pinpoint the intersection of the PDF lines of Virginica and Versicolour at X-value 5. Drawing a verticle line, you correspond this point of intersection with the PDF of Virginica and then to it's Y-value - this gives you a Y-value of 0.95 (95%). This tells you that 95% of Virginica have a PL of 5 or less.
- Drawing a horizontal line from the CDF point for Versicolor corresponding to the intersection point, to the Y-axis, you can a figure of 0.1 (10%). This will function as the point at which you cut off your study of Virginica for Versiclor. You now know from looking at the CDF of Versicolor that you will be investigating the remaining 90% of Versicolor. 
- I.e. There will be 90% accuracy on your investigation of Versicolor as 10% of Versicolor vectors are muddled with the Virginica.

- **9(e): Creating an If for CDF of Virginica and Versicolor:**
- If rule for analysing Virginica, with an upper limit set at the X-value 5 and 95% accuracy:
- **if PL > 2:**
-   **& PL <= 5:**
    **Then Virginica**

- If rule for analysing Versicolor, with a lower limit set at X-value 5 and 90% accuracy:
- **if PL > 2:**
-   **& PL > 5:**
    **Then Versicolor**

- This such information cannot be understood with PDF, it is whem the CDF is applied, you can understand cut-off points for analysis and the rates of error that will apply to them.

### 10. **Violin Plots.**
- **10(a):**
- A violin plot is a combination of a histogram and a PDF into a simpler format. Denser regions of the dataset are the fatter areas of the 'violins', whilst sparser regions of the data are represented by the thinner parts of the violin.
- The thick black line in the middle of the violin with the white dot, has a relationship to the box-plot.
- Moving down this vertical thick line, from where the line begins higher up represents the 75th percentile, the white dot represents the 50th percentile and the end of the thick line represents the 25th percentile. 
- The two thinner lines ejecting from either vertical end of the thick line represent the 'whiskers' of the box plot. The end of the these thinner lines corresponding to the two horizontal whiskers of a box plot. 

- Code for graphing a violin plot:
- **sns.violinplot(x = "species", y = "petal_length", data = df, size = 8)**
- **plt.show()**

- **10(b): What is the significance of the colored region of the violin?**
- We immediately notice that both sides of the violin are symmetrical. We also see that the shape of the violin looks similar to a bell curve.
- The side of the violin represents the Probability Distribution Function (PDF), essentially what is represented in a histogram - turining your head sideways illustrates this.

- Therefore, a violin plot takes the histogram (colored region) and the box plot and combines them into a single plot. In this way, the violin plot gives you the best of both worlds: you can tell what the distribution is and you can also read the percentile values. 

### 11. **Univariate, Bivariate and Multivariate Analysis.**
- PDF, CDF, box plots, violin plots - these do univariate analysis. 
- Pairplots and scatter plots do bivariate analysis as they investigate 2 variables.
- Multivariate analysis is the study of multiple is when you are investigating more than 2 variables, e.g. a 3-dimensional scatter plot. 
- Multivariate analysis has a large subject and includes the entire field of machine learning. Therefore, in creating a plotting scheme to incorporate all 4 variables in the Iris Dataset, you will be carrying out multivariate analysis.

### 12. **Multivariate Probability Density - Contour Plots.**
- **12(a): Conceptualising a Contour Plot:**
- We have looked at 1-dimensional probability functions such as histograms, box plots, violin plots etc. 
- We will now investigate how to create a probability density plot with more than 1 dimensions.

- Script for 2D density 'Contours Plots':
- **sns.jointplot(x = "petal_length", y = "petal_width", data = df_setosa, kind = "kd)**
- **plt.show()**

- Contour plots can resemble a 'wormhole' as depicted in sci-fi. 
- The above script creates a contour plot featuring PL on the x-axis and PW on the Y-axis. This plot investigates the same data as the 12th scatter plot in the pairplot for Setosa previously created, except excluding the 2 other species as subjects.
- Looking the grouping of the dots in this pervious scatter plot we see that most of the dots are densely grouped in the centre, with those on the outside being sparsely populated. 
- Taking this knowledge of how PL and PW of setosa are grouped in a scatter plot and looking at the Contours Plot, we'll notice that the densely grouped centre is represented here by the black central hole, the darest part of the plot. 
- To conceptualise what is being represented in the Contour plot it is helpful to imagine a hill extending out of the screen from the centre of the plot. With the centre darkest point being the peak of the hill and representing the densest data group and the lighter outlines being the lower level of the hill, representing the sparser data.

- **12(b): What are the contour lines representing?**
- The various shades of colour of the 'hill' are the contours themselves. 
- Prior to the advent of modern computing, when graphs of this nature were not being built by computers for datasets, Cathographers utilised the same concept of contour plots when mapping a hill of varied altitude. In the maps, and in todays maps still, each shade represented a specific altitude (or range of altitude).
- The contours in Seaborn plots similarly represent measures of probability of the two axis values (PL and PW).
- The darker contours represent higher probabilities (or higher probability density), whilst the lighter outer contours represent lower probability density. 
- In Seaborn Contour Plots are generated with 2 supplementary PDF plots, for both axis values, these are displayed along the edges of the graph. This provides both instances of the 1-d variables being represented in the contour plot.
- Therefore, 1-d density plots are achieved using PDF graphs and 2-d density plots are achieved using Contour Density Plots.

- From looking at a Contour plot, we can understand that the darker contours represent the most common PL and PW measurements (as read off the x and y axes). The black central contour therefore, corresponds to the combination of both peaks from the 2 supplementary 1-d PDF graphs. 

- 3-density plots are much more difficult to visualise as it requires an conceptualisation of 4-dimensions. However, using tools of 1-d, 2-d, and 3-d analysis is sufficient to have a mathematical understanding of 4-d and onwards.