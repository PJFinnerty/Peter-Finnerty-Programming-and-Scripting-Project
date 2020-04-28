No. of rows/no. of columns:  (150, 5) 

Names of species/no. of vectors:
setosa        50
versicolor    50
virginica     50
Name: species, dtype: int64 

Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
       'species'],
      dtype='object') 


        sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000 
mad        1.037822     0.370651      1.853253     1.037822

### **Univariate Analyis: Histograms and PDF/CDF Functions **

.
#### **Petal Length(PL)**
     ** Iris Setosa: ** From observations     immediately made under univariate analysis of 'Petal Length', Iris Setosa can be     distinguised from the other classes
. Setosa is seen to have no measure of PL longer than 2cm.     This is backed up by investigation of the CDF function of Setosa Petal Length in 'setosaCDF.png',     whereby Setosa PL reaches 100% probability at 1.9cm.

    ** Iris Virginica and Iris Versicolor: ** The histogram of Petal Length displays some minor overlap     in ths Virginica and Versicolor species. Measurements for Versicolour begin roughly at 3.2cm and end at 5.3cm.     Whilst Versicolour shows a histogram curve rangin from 4.2cm to 7cm. The overlap occurs between 4cm     and 5.1cm. Looking at the CDF function of Virginica (which begins at roughly 4.4cm, it is noticed     that less than 25 percent of Virginica PL vectors are less than 5.1cm. Whilst this is a small overlap     it is clear that a histogram univariate analysis of Petal Length does not adequately distinguish     between Versicolor and Virginica.
#### Petal Width (PW)

 ** Setosa: ** Similarly to PL, the histogram of PW, shows Setosa     to be easily distinguished.
A high peak is noted with just a few PW vectors just over 0.5cm.     Turning once again to the CDF
function of Setosa, it is seen that 100 percent of Setosa values     have a PW of 0.6cm or less. 
From the histogram and CDF function alone, it is clear that there     is no overalap between Setosa
and the other species. It is noted that roughly 55 percent of     Setosa PW vectors are between
0.2cm and 0.4cm, as noted by the sharp peak in the CDF.     

 ** Versicolor and Virginica: ** Once again there is a slight overlap in Petal Width of the
    remaining 2 species - this is roughly in the range of 1.2cm to 1.8cm. The distribution of both
    species is very spread out, in comparison to the high peak noted in the Setosa histogram.
    Looking again to the feature of Virginica as the noticably larger species in terms of PW, it is
    seen that roughly 40 percent of Virginica's PW vectors are 1.8cm or less, resulting in a higher
    probability of overlap with Versicolour than occurred with PL. This illustrates the benefit of
    the CDF function in distinguishing these species. It is clear that because the CDF curves of both
    species is more flat for PW than PL, that the overlap appeared to be less significant than it is.
    This highlight the utility of a CDF curve being used in tandem with a histogram.
