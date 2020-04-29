import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import robust
from sklearn import preprocessing


df = pd.read_csv('IrisDataset.csv')

setosa = df[0:50]
versicolor = df[50:100]
virginica = df[100:150]

# Output a scatterplot of each pair of variables to png files.

# Scatterplot of Petal Length Vs Petal Width
sns.set_style("darkgrid")
iris = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=df)
x = [4.2, 5.65]
y = [2.0, 1.0]
plt.plot(x, y)
plt.title("Scatter Plot: Petal Length Vs Petal Width")
plt.savefig("scatter1.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Scatterplot of Petal Length Vs Sepal Length
sns.set_style("darkgrid")
iris = sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df)
x = [4.5, 7.5]
y = [4.6, 5.0]
plt.plot(x, y)
plt.title("Scatter Plot: Sepal Length Vs Petal Length")
plt.savefig("scatter2.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------
# Scatterplot of Petal Length Vs Sepal Width 
sns.set_style("darkgrid")
iris = sns.scatterplot(x="sepal_width", y="petal_length", hue="species", data=df)
x = [1.8, 3.6]
y = [4.1, 5.2]
plt.plot(x, y)
plt.title("Scatter Plot: Sepal Width Vs Petal Length")
plt.savefig("scatter3.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Scatterplot of Petal Width Vs Sepal Length
sns.set_style("darkgrid")
iris = sns.scatterplot(x="sepal_length", y="petal_width", hue="species", data=df)
x = [4.0, 8.0]
y = [1.60, 1.60]
plt.plot(x, y)
plt.title("Note: Regression line distinguishes Versicolor from Viriginica", fontsize = 10)
plt.suptitle("Scatter Plot: Sepal Length Vs Petal Width")
plt.savefig("scatter4.png")
plt.clf
plt.show()
#--------------------------------------------------------------------------------
# Scatterplot of Petal Width Vs Sepal Width
sns.set_style("darkgrid")
iris = sns.scatterplot(x="sepal_width", y="petal_width", hue="species", data=df)
x = [2.0, 3.80]
y = [1.55, 1.70]
plt.plot(x, y)
plt.title("Scatter Plot: Sepal Width Vs Petal Width")
plt.savefig("scatter5.png")
plt.clf
plt.show()
#-------------------------------------------------------------------------------
# Scatterplot of Sepal Length Vs Sepal Width
sns.set_style("darkgrid")
iris = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length Vs Sepal Width")
plt.savefig("scatter6.png")
plt.clf
plt.show()
#===============================================================================

print("\n### **Biivariate Analyis: Scatter Plots and Contour Plots**\n\n\
#### Further Distinguishing Setosa\n\n\
**Setosa SL:** It is noted that Iris Setosa has been shown to be distinguishable in terms\
of Petal Length and Petal Width. It is now necessary to distinguish it in terms\
of Sepal Length and Sepal Width. To do this scatter plots can be used.\
Looking at the scatter plot of Sepal Length and Petal Length, it is noted that\
the vectors of Setosa are all grouped in the bottom left corner, ranging in\
SL from 4.2cm-5.8cm. In terms of PL, Setosa ranges from 0.2cm to 1.95cm. This\
2-dimensional graph, firmly establishes the feature of Setosa Sepal Length,\
by representing it's relationship to Petal Length.\n\n\
**Setosa SW:** Whilst a univariate representation of Setosa Sepal Width did not\
provide a representation that defined the species, by plotting Sepal Width with\
Petal Length, a high degree of separation is achieved. Iris Setosa are shown to\
have Sepal width that far exceeds Petal Length, whilst for Virginica and\
Versicolor, this relationship is inverted. This contrast displays that Setpsa can\
be clearly distinguished from the other species by SW and will no longer be included\
in the analysis. This graph is an example of the effectiveness of scatter plots in\
using a 2-d image to provide an accurate idea of both sepal and petal shapes of the\
3 species.\n\n")

print("#### Distinguishing Virginica from Veriscolor by Linear Regression\n\n\
**Method for Distinguishing Versicolor from Virginica:** \
Versicolor and Virginica, species that were shown to display little\
distinguishing features under univariate analysis, will now be investigated in 2-d\
models to achieve a higher degree of separation. This will be achieved by\
examining scatter plots that display 2 features, with specific colouring highlighting\
the relevant species on the scatter plot (versicolor=yellow and viginica=green).\
The scatter plots will then be compared against the individual contour density plots of\
both Versicolor and Virginica. Contour plots provide an idea of where the most densely\
populated centres of both species occur in terms of 2 features.\
As there is a varying degree of overlap in the scatter plots of the various pairs of features,\
the contour plots will idetify where linear spearation on the scatter plot is most appropriately\
carried out. Once the most dense regions have been identified, a regression line will be drawn into\
the graph. This line will be drawn oustide of the range depicted as the most dense in\
the contour plot, but the angle and of the line will drawn based on the scatter plots, to\
provide the least amount of 'outlying' vectors on either side of the line.\n\n")

print("**Petal Length V. Petal Width:** A study of the contour plot of Versicolor\
displays that it has a densely populated central contour representing the Petal Legnth range\
of 4.2cm to 4.75cm and a Petal Width range of 1.25cm-1.55cm. On the Virginica plot, as the\
central contour is very small, the 2nd contour will also be included in the analysis: this\
dense centre ranges from 4.9cm-5.7cm in Petal Length and 1.8cm-2.3cm in Petal Width. This\
leaves a degree of seperation between the central contours of both species of 0.15cm in\
terms of PL and 0.25cm in terms of PW. Whilst this distance is not so large, there is a\
consistent trend for Virginica to have larger PL and PW vectors. This is evident in the\
scatter plot. The fact that the trend is clear for both features highlights that\
linear separation will be highly effective at distinguishing the species.\
The following coordinates have been chosen for linear separation\
on the PL/PW scatter plot:\n\
x = [4.2, 5.65]\n\
y = [2.0, 1.0]\n\n\
The above corrdinates are shown to draw a diagonal across the scatter plot that leaves only\
1 Virginica vector on the Versicolor side of the line and just 2 Versicolor vectors on the\
Virginica side of the line. Therefore, linear separation has been achieved between the two\
species with 94 percent accuracy.\
Comparing this line first to the contour plot of Versicolor, the line occurs just outside\
the central contour. In the Virginica contour plot, it is drawn well outside of the central\
contour.\n\
**Result:** Versicolor and Virginica have been distinguished to a high degree under\
bivariate analysis of Petal Length and Petal Width.\n\n")

print("**Sepal Length V. Petal Length:** A study of the individual contour plots of\
Virginica and Versicolor, show that the central contours in both plots, have a moderate\
degree of separation from one another, in terms of the measurement ranges that contain\
the most vectors. Versicolor has a central contour rougly in the SL range of 5.6cm-\
5.9cm and a PL range of 4cm-4.3cm. Virginica meanwhile, has a smaller central contour\
therefore, it is necessary to investigate the central two contours (or darkest shades).\
These 2 contours range in SL from 6.3cm-6.8cm and in PL, range from 5.2cm-5.75cm.\
This leaves a degree of separation between the central contours of both species of 0.4cm\
in SL and 0.9cm in PL. The following coordinates have been chosen for a line of\
regression on the scatter plot of PL/PW:\n\
x = [4.5, 7.5]\n\
y = [4.6, 5.0]\n\n\
The diagonal that is drawn with the above coordinates, casts a line that generally\
dintinguishes the species in terms of PL. On the Versicolor side of the line, there are\
three outlier Virginica vectors. On the Virginica side of the line, there are 4 outlier\
Versicolor vectors. Therefore, this linear separation has distinguished Versicolor from\
Virginica with 86 percent accuracy.\n\
**Result:** Versicolor and Virginica have been moderately distinguished under\
bivariate analysis of Petal Length and Sepal Length.")

print("**Sepal Width V Petal Length:** The contour plot of Versicolor in terms of SW\
and PL contains a very small central contour. As a result the 3 centre contours will\
be considered the area of greatest density. This area ranges from 2.7cm-3.3cm in SW and\
4.2cm to 4.7cm in PL. Likewise it is necessary to take into consideration the 2 centre\
contours of Virginica SW/PL. For Virginica, this dense area ranges from 2.8cm-3.2cm\
in Sepal Width and 5.1cm-5.75cm in terms of Petal Length. This leaves a moderate degree of\
separation of the dense contours of the two species in terms of Petal Length, i.e. there is\
0.4cm between the upper edge of the Versicolor central contours and the lower edge of\
Virginica. This trend is more clearly seen in the scatter plot of both features, where\
like, PL and PW, a trend towards Petal Length difference is the distinguishing feature.\
The following coordinates have been chosed for a line of regression:\n\
x = [1.8, 3.6]\n\
y = [4.1, 5.2]\n\n\
Linear separation here results in 2 Viginica outliers on the Versicolor side of the line and\
5 Versicolor outliers on the Virginica side of the line.\n\
**Result:** linear regression here has achieved 86 percent accuracy in distinguishing the\
two species in terms of Sepal Width and Petal Length.\n\n")

print("**Sepal Length V. Petal Width:** The contour plot of Versicolor SL/SW, taking the two\
central contours as the dense region for comparison with the scatter plot, ranges from\
5.5cm-6cm in SL and 1.2cm-1.35cm in PW. As such this is a relatively small, but\
dense centre. Comparing the contours of Versicolor with Virginica, it's noteed that whilst\
there is a slight trend for Virginica to have larger Sepal Length, the primary difference is\
in Petal Width. Therefore, it is again one of the two petal features that will provide data\
for linear separation. Virginica shows a centre contour ranging from 1.76cm-1.78cm in\
terms of Petal Width, however, when including the second contour, this increases to a\
dense centre ranging from 1.75cm-2.35cm. As such Virginica displays a trend towards a more\
dispersed population in terms of PW. It is worth noting that in terms of PW, the upper\
edge of the central 2 contours of Versicolor is separated from the lower edge of the\
central contours of Virginica by 0.4cm. This is a not very large difference in terms of\
clustered Petal Width vectors. The coordinates for a line of regression in the scatter plot\
are as follows:\n\
x = [4.0, 8.0]\n\
y = [1.60, 1.60]\n\n\
This line of separation results in 4 outlier Virginica vectors on the Versicolor side of the\
line and 3 Versicolor outliers on the Virginica side. As such, linear separation has been\
achieved within 86 percent accuracy. It may be noted that in an effort to result in less\
outlying Versicolor vectors on the Virginica side, the line could have been drawn at a higher\
Y-axis value (perhaps 1.68cm). However, in this case the distance of the dense populations of\
both species from one another was deemed a more important factor than the number of outlying\
vectors.\n\
**Result:** linear separation of both species has been achieved via Petal Width to 86 percent\
accuracy\n\n")

print("**Sepal Width V. Petal Width:** Once again investigating the two most inner contours\
Versicolor is seen to have very little separation from Virginica in terms of the density of\
the Sepal Width vectors. As such this investigation will look at Petal Width. The range of\
the 2 central contours of Versicolor PW is from 1.25cm to 1.48cm. Similarly to SL/PW\
Iris Viginica displays a more extended central contour in terms of PW, ranging from 1.75cm-\
2.3cm. It is clear therefore, that Virginica show a greater variation in terms of Petal Width\
than Versicolor. In terms of PW, the degree of separation between the edge of the dense centre\
of Versicolor PW and the lower edge of the Virginica central contours is 0.27cm. This is an\
even smaller degree of separation between the dense populations of both species than in\
the analysis of SL/PW. The coordinates for a line of separation between both species are:\n\
x = [2.0, 3.80]\n\
y = [1.55, 1.70]\n\n\
This line of regression results in 4 Virginica outliers on the Versicolor side of the line and\
2 Versicolor vectors on the Virginica side. According to the regression line as drawn on the\
scatter plot, it appears that the species have been distinguished accurately up to 88 percent.\
However, due to the close proximity of the dense populations of the species, it is\
clear that this figure is misleading. The species have been distinguished moderately, but the\
close dense centres as seen in the contour plots, suggest that the outlying vectors of both\
species hold more statistical weight than in previous models.\n\
**Result:** linear separation has been moderately successful in distinguishing Versicolor from\
Virginica in terms of Petal Width.")

print("**Sepal Length V. Sepal Width:** Looking at the scatter plot of SL/SW, a massive\
degree of overlap is seen, to the extent that it is difficult to identify vectors that can\
be classified as outliers. Comparing this to the contour plots of both species for these\
features, it is clear that the contour density plots will not aid us in distinguishing the\
species. In fact, it is evident that the contour plots may be deceiving. The contour plot\
of Versicolor SP/SW shows a small dense centre, whereby the two central contours extend from\
5.6cm-6.1cm in SL and from 2.7cm to 2.9cm in SW. The two inner contours on the Virginica\
plot range from 6.2cm-7cm in SL and from 2.8cm-3.3cm in SW. However, by examining the\
scatter plot, it is evident that there is not a clear dense population of either species.\
Instead, there are a few clusters of Virginica species, intermingled with numerous outlying\
Versicolor vectors. The dence centre of Versicolor as seen in the contour plot appears to\
correlate to a cluster of just 5 Versicolor vectors, indicating that the program that\
calculates the central contour of Versicolor simply located the most cloesly packed group\
of Versicolor vectors it could find and assigned this region, that is surrounded by 6 Virginica\
vectors, as the dense population centre. It is clear therefore, considering the high degree,\
of Virginica and Versicolor vectors within the same range, that linear regression will\
not successfully distinguish the species.\n\
**Result:** linear regression is not capable of separating the two species in terms of\
Sepal Length and Sepal Width. The use of contour plots in conjunction with the scatter plot\
will not provide a valuable outcome.")


#=====================================================================================
# Create large figure to fit 4 subplots, set title and style.
plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Probability Density Function (PDF) and Cumulative Distribution Function (CDF) of 4 Features")
sns.set_style("darkgrid")

# Create subplot 1: create counts and bin_edges variables and assign it to the histogram for 'petal_length', set bins to 10.

plt.subplot(221) #(221) - the first two digits refer to the subplot formation (2 by 2) and the final digit assigns it as the first subplot.
counts, bin_edges = np.histogram(df['petal_length'], bins = 10, density = True) # Reference: appliedaicourse.com
# Create pdf variable and assign it the value of each x point on petal length histogram divided by the sum of the points.
pdf = counts / (sum(counts) )
# Use Numpys's cumulative sum function on 'pdf' variable and assign it to variable 'cdf'.
cdf = np.cumsum(pdf)
# Plot both CDF and PDF lines and label.
plt.plot(bin_edges[1:], pdf, label = 'PDF') # Reference: appliedaicourse.com
plt.plot(bin_edges[1:], cdf, label = 'CDF')
# Assign titel and legend.
plt.title("Petal Length")
plt.legend()

plt.subplot(222)
counts, bin_edges = np.histogram(df['petal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Petal Width")
plt.legend()

plt.subplot(223)
counts, bin_edges = np.histogram(df['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Sepal Length")
plt.legend()

plt.subplot(224)
counts, bin_edges = np.histogram(df['sepal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Sepal Width")
plt.legend()

plt.show()







# VIRGINICA V Versicolor : PL and PW

plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Virginica and Versicolor: Univarariate Analysis of CDF and PDF (1/2)")
sns.set_style("darkgrid")

plt.subplot(221) 
counts, bin_edges = np.histogram(virginica['petal_length'], bins = 10, density = True) # Reference: appliedaicourse.com
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF') # Reference: appliedaicourse.com
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Virginica Petal Length")
plt.legend()

plt.subplot(222)
counts, bin_edges = np.histogram(versicolor['petal_length'], bins = 10, density = True) # Reference: appliedaicourse.com
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF') 
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Versicolor Petal Length")
plt.legend()
##

plt.subplot(223)
counts, bin_edges = np.histogram(virginica['petal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Virginica Petal Width")
plt.legend()

plt.subplot(224)
counts, bin_edges = np.histogram(versicolor['petal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Versicolor Petal Width")
plt.legend()
##

plt.savefig("d_Virg_V_Vers1.png")
plt.clf
plt.show()
#==============================================================================

# VIRGINICA V Versicolor : SL and SW

plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Virginica and Versicolor: Univariate Analysis of CDF and PDF (2/2)")
sns.set_style("darkgrid")

plt.subplot(221)
counts, bin_edges = np.histogram(virginica['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Virginica Sepal Length")
plt.legend()


plt.subplot(222)
counts, bin_edges = np.histogram(versicolor['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Versicolor Sepal Length")
plt.legend()


plt.subplot(223)
counts, bin_edges = np.histogram(virginica['sepal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Virginica Sepal Width")
plt.legend()

plt.subplot(224)
counts, bin_edges = np.histogram(versicolor['sepal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Versicolor Sepal Width")
plt.legend()

plt.savefig("d_Virg_V_Vers2.png")
plt.clf
plt.show()


#==============================================================================
# Creating violin plots of the features.

# Create large figure to fit 4 subplots, set title and style.
plt.figure (figsize = (15, 6.5) ) 
plt.suptitle("Iris Flowers: Violin Plots of Features")
sns.set_style("darkgrid")

# Create violin plot 1, add hue for species and format as necessary.
plt.subplot(221)  #(221) - the first two digits refer to the subplot formation (2 by 2) and the final digit assigns it as the first subplot.
sns.violinplot(x = "species", y = "petal_length", hue='species', size = 8, data = df)

plt.subplot(222)
sns.violinplot(x = "species", y = "petal_width", hue='species', size = 8, data = df)

plt.subplot(223)
sns.violinplot(x = "species", y = "sepal_length", hue='species', size = 8, data = df)

plt.subplot(224)
sns.violinplot(x = "species", y = "sepal_width", hue='species', size = 8, data = df) 

plt.show()

#========================================================

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import robust
import math
df = pd.read_csv('IrisDataset.csv')

plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Virginica: Probability Density Function (PDF) and Cumulative Distribution Function (CDF)")
sns.set_style("darkgrid")

plt.subplot(221) #(221) - the first two digits refer to the subplot formation (2 by 2) and the final digit assigns it as the first subplot.
counts, bin_edges = np.histogram(virginica['petal_length'], bins = 10, density = True) # Reference: appliedaicourse.com
# Create pdf variable and assign it the value of each x point on petal length histogram divided by the sum of the points.
pdf = counts / (sum(counts) )
# Use Numpys's cumulative sum function on 'pdf' variable and assign it to variable 'cdf'.
cdf = np.cumsum(pdf)
# Plot both CDF and PDF lines and label.
plt.plot(bin_edges[1:], pdf, label = 'PDF') # Reference: appliedaicourse.com
plt.plot(bin_edges[1:], cdf, label = 'CDF')
# Assign titel and legend.
plt.title("Petal Length")
plt.legend()

plt.subplot(222)
counts, bin_edges = np.histogram(virginica['petal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Petal Width")
plt.legend()

plt.subplot(223)
counts, bin_edges = np.histogram(virginica['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Sepal Length")
plt.legend()

plt.subplot(224)
counts, bin_edges = np.histogram(virginica['sepal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Sepal Width")
plt.legend()

plt.savefig("d_virginicaCDF.png")
plt.clf
plt.show()
#==============================================================================

# VERSICOLOR

plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Versicolor: Probability Density Function (PDF) and Cumulative Distribution Function (CDF)")
sns.set_style("darkgrid")

plt.subplot(221) #(221) - the first two digits refer to the subplot formation (2 by 2) and the final digit assigns it as the first subplot.
counts, bin_edges = np.histogram(versicolor['petal_length'], bins = 10, density = True) # Reference: appliedaicourse.com
# Create pdf variable and assign it the value of each x point on petal length histogram divided by the sum of the points.
pdf = counts / (sum(counts) )
# Use Numpys's cumulative sum function on 'pdf' variable and assign it to variable 'cdf'.
cdf = np.cumsum(pdf)
# Plot both CDF and PDF lines and label.
plt.plot(bin_edges[1:], pdf, label = 'PDF') # Reference: appliedaicourse.com
plt.plot(bin_edges[1:], cdf, label = 'CDF')
# Assign titel and legend.
plt.title("Petal Length")
plt.legend()

plt.subplot(222)
counts, bin_edges = np.histogram(versicolor['petal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Petal Width")
plt.legend()

plt.subplot(223)
counts, bin_edges = np.histogram(versicolor['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Sepal Length")
plt.legend()

plt.subplot(224)
counts, bin_edges = np.histogram(versicolor['sepal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Sepal Width")
plt.legend()

plt.savefig("d_versicolorCDF.png")
plt.clf
plt.show()

#============================================================================================
# Creating a violin plot.
plt.figure (figsize = (15, 6.5) ) 
plt.suptitle("Iris Flowers: Violin Plots of Features")
sns.set_style("darkgrid")

plt.subplot(221)
sns.violinplot(x = "species", y = "petal_length", hue='species', size = 8, data = df)
plt.title("Petal Length", ha = 'right')

plt.subplot(222)
sns.violinplot(x = "species", y = "petal_width", hue='species', size = 8, data = df)
plt.title("Petal Width", ha = 'right' )

plt.subplot(223)
sns.violinplot(x = "species", y = "sepal_length", hue='species', size = 8, data = df)
plt.title("Petal Width", ha = 'right')

plt.subplot(224)
sns.violinplot(x = "species", y = "sepal_width", hue='species', size = 8, data = df)
plt.title("Petal Width", ha = 'right')

plt.savefig("violin_plot.png")
plt.clf
plt.show()


print("\n### **Biivariate Analyis: Scatter Plots and Contour Plots**\n\n\
#### Further Distinguishing Setosa\n\n\
**Setosa SL:** It is noted that Iris Setosa has been shown to be distinguishable in terms\
of Petal Length and Petal Width. It is now necessary to distinguish it in terms\
of Sepal Length and Sepal Width. To do this scatter plots can be used.\
Looking at the scatter plot of Sepal Length and Petal Length, it is noted that\
the vectors of Setosa are all grouped in the bottom left corner, ranging in\
SL from 4.2cm-5.8cm. In terms of PL, Setosa ranges from 0.2cm to 1.95cm. This\
2-dimensional graph, firmly establishes the feature of Setosa Sepal Length,\
by representing it's relationship to Petal Length.\n\n\
**Setosa SW:** Whilst a univariate representation of Setosa Sepal Width did not\
provide a representation that defined the species, by plotting Sepal Width with\
Petal Length, a high degree of separation is achieved. Iris Setosa are shown to\
have Sepal width that far exceeds Petal Length, whilst for Virginica and\
Versicolor, this relationship is inverted. This contrast displays that Setpsa can\
be clearly distinguished from the other species by SW and will no longer be included\
in the analysis. This graph is an example of the effectiveness of scatter plots in\
using a 2-d image to provide an accurate idea of both sepal and petal shapes of the\
3 species.\n\n")

print("#### Distinguishing Virginica from Veriscolor by Linear Regression\n\n\
**Method for Distinguishing Versicolor from Virginica:** \
Versicolor and Virginica, species that were shown to display little\
distinguishing features under univariate analysis, will now be investigated in 2-d\
models to achieve a higher degree of separation. This will be achieved by\
examining scatter plots that display 2 features of both species together, with\
specific colouring added to each species (versicolor=yellow and viginica=green).\
The scatter plots will then be compared against a contour plot that displays the density\
of either Versicolor or Virginica. As there is a small degree of overlap in the scatter\
plots, the contour plot will identify where 1 of the species is most densely populated\
thereby highlighting where linear spearation on the scatter plot is most appropriately\
carried out. Whether the contour plot used as a comparison will be that of Virginica\
or Versicolor will depend on which plot provides the most densely populated contours.\
Once the most dense region has been identified, a regression line will be drawn into\
the graph. This line will be drawn oustide of the range depicted as the most dense in\
the contour plot, but the angle and of the line will drawn based on the scatter plots, to\
provide the least amount of 'outlier' vectors on either side of the line.\n\n")

print("**Petal Length V. Petal Width:** A study of the contour plot of Versicolor\
displays that it is the preferred comparison graph for the scatter plot of PL/PW.\
It has a densely populated central contour representing the range within\
which most Versicolor PL and PW vectors occur. This is in the PL range 4.2cm to 4.75cm\
and in PW, 1.25cm-1.55cm. The following coordinates have been chosen for linear separation\
on the PL/PW scatter plot:\n\
x = [4.2, 5.65]\n\
y = [2.0, 1.0]\n\n\
The above corrdinates are shown to draw a diagonal across the scatter plot that leaves only\
1 Virginica vectors on the Versicolor side of the line and just 2 Versicolor vectors on the\
Virginica side of the line. Therefore, this linear regression line distinguishes\
Versicolor with 98 percent accuracy and distinguishes Virginica with 96 percent accuracy.\
Comparing this line first to the contour plot of Versicolor, the line occurs just outside\
the central contour. In the Virginica contour plot, it is drawn well outside of the central\
contour.\n\
**Result:** Versicolor and Virginica have been accurately distinguished under bivariate\
analysis of Petal Length and Petal Width.\n\n")

print("**Sepal Length V. Petal Length:** A study of the individual contour plots of\
Virginica and Versicolor, shows that the central contours in both plots, have a relative\
degree of separation from one another in terms of the measurement ranges that contain\
the most vectors. Versicolor has a central contour rougly in the SL range of 5.6cm-\
5.9cm and a PL range of 4cm-4.3cm. Virginica meanwhile, has a smaller central contour\
therefore, it is necessary to investigate the central two contours (or darkest shades).\
These 2 contours range in SL from 6.3cm-6.8cm and in PL range from 5.2cm-5.75cm.\
This leaves a degree of separation between the central contours of both species of 0.4cm\
in SL and 1.45cm in PL. Furthermore, it is noted from the scatter plot of both species\
that the species are separated according to variation along the Y-axis, i.e., Petal Length\
is the feature that distinguishes species in this particular bivariate analysis. The\
following coordinates have been chosen for a line of regressions:\n\
x = [4.5, 7.5]\n\
y = [4.6, 5.0]\n\n\
The diagonal that is drawn with the above coordinates, casts a line that generally\
dintinguishes the species in terms of PL. On the Versicolor side of the line, there are\
three outlier Virginica vectors. On the Virginica side of the line, there are 4 outlier\
Versicolor vectors. Therefore, this linear separation has distinguished Versicolor from\
Virginica with 86 percent accuracy.\n\
**Result:** Versicolor and Virginica have been relatively accurately distinguished under\
bivariate analysis of Petal Length and Sepal Length.")

print("**Sepal Width V Petal Length:** The contour plot of Versicolor in terms of SW\
and PL contains a very small central contour. As a result the 3 centre contours will\
be considered the area of greates density. This area ranges from 2.7cm-3.3cm in SW and\
4.2cm to 4.7cm in PL. Likewise it is necessary to take into consideration the 2 centre\
contours of Iris Virginica SW/PL. For Virginica, this dense area ranges from 2.8cm-3.2cm\
in Sepal Width and 5.1cm-5.75cm in terms of Petal Length. This leaves a moderate degree of\
separation of the dense contours of the two species in terms of Petal Length, i.e. there is\
0.4cm between the upper edge of the Versicolor central contours and the lower edge of\
Virginica. This trend is more clearly seen in the scatter plot of both features, where\
like, PL and PW, a trend towards Petal Length difference is the distinguishing feature.\
The following coordinates have been chosed for a line of regression:\n\
x = [1.8, 3.6]\n\
y = [4.1, 5.2]\n\n\
Linear separation here results in 2 Viginica outliers on the Versicolor side of the line and\
5 Versicolor outliers on the Virginica side of the line.\n\
**Result:** linear regression here has achieved 86 percent accuracy in distinguishing the\
two species in terms of Sepal Width and Petal Length.\n\n")

print("**Sepal Length V. Petal Width:** The contour plot of Versicolor SL/SW, taking the two\
central contours as the dense region for comparison with the scatter plot, ranges from\
5.5cm-6cm in SL and 1.2cm-1.35cm in PW. As such this is a relatively small, but\
dense centre. Comparing the contours of Versicolor with Virginica, displays that whilst\
there is a slight trend for Virginica to have larger Sepal Length, the primary difference is\
in Petal Width. Therefore, it is again one of the two petal features that will provide data\
for linear separation. Virginica shows a centre contour ranging from 1.76cm-1.78cm in\
terms of Petal Width, however, when including the second contour, this increases to a\
dense centre ranging from 1.75cm-2.35cm. As such Virginica displays a tend towards a more\
dispersed population in terms of PW. It is worth noting that in terms of PW, the upper\
edge of the central 2 contours of Versicolor is separated from the lower edge of the\
central contours of Virginica by 0.4cm. This is a not very large difference in terms of\
clustered Petal Width vectors. The coordinates for a line of regression in the scatter plot\
are as follows:\n\
x = [4.0, 8.0]\n\
y = [1.60, 1.60]\n\n\
This line of separation results in 4 outlier Virginica vectors on the Versicolor side of the\
line and 3 Versicolor outliers on the Virginica side. As such, linear separation has been\
achieved within 86 percent accuracy. It may be noted that in an effort to result in less\
outlying Versicolor vectors on the Virginica side, the line could have been drawn at a higher\
Y-axis value (perhaps 1.68cm). However, in this case the distance of the dense populations of\
both species from one another was deemed a more important factor than the number of outlying\
vectors.\n\
**Result:** linear separation of both species has been achieved via Petal Width to 86 percent\
accuracy\n\n")

print("**Sepal Width V. Petal Width:** Once again investigating the two most inner contours\
Versicolor is seen to have very little separation from Virginica in terms of the density of\
the Sepal Width vectors. As such this investigation will look at Petal Width. The range of\
the 2 central contours of Versicolor PW is from 1.25cm to 1.48cm. Similarly to SL/PW\
Iris Viginica displays a more extended central contour in terms of PW, ranging from 1.75cm-\
2.3cm. It is clear therefore, that Virginica show a greater variation in terms of Petal Width\
than Versicolor. In terms of PW, the degree of separation between the edge of the dense centre\
of Versicolor PW and the lower edge of the Virginica central contours is 0.27cm. This is an\
even smaller degree of between the dense populations of both species than in SL/PW.\
The coordinates for a line of separation between both species are:zn\
x = [2.0, 3.80]\n\
y = [1.55, 1.70]\n\n\
This line of regression results in 4 Virginica outliers on the Versicolor side of the line and\
2 Versicolor vectors on the Virginica side. According to the regression line as drawn on the,\
scatter plot, it appears that the species have been distinguished accurately up to 88 percent.\
However, due to the close very close proximity of the dense populations of the species, it is\
clear that this figure is misleading. The species have been distinguished moderately, but the\
close dense centres as seen in the contour plots, sugges that the outlying vectors of both\
species hold more statistical weight than in previous models.\n\
**Result:** linear separation has been moderately successful in distinguishing Versicolor from\
Virginica in terms of Petal Width.end=

print("**")