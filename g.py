# Create large figure to fit 4 subplots, set title and style.
plt.figure(figsize = (15, 6.5) ) 
plt.suptitle("Setosa: Probability Density Function (PDF) and Cumulative Distribution Function (CDF)")
sns.set_style("darkgrid")

# Create subplot 1: create counts and bin_edges variables and assign it to the histogram for 'petal_length', set bins to 10.

# SETOSA

plt.subplot(221) #(221) - the first two digits refer to the subplot formation (2 by 2) and the final digit assigns it as the first subplot.
counts, bin_edges = np.histogram(setosa['petal_length'], bins = 10, density = True) # Reference: appliedaicourse.com
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
counts, bin_edges = np.histogram(setosa['petal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Petal Width")
plt.legend()

plt.subplot(223)
counts, bin_edges = np.histogram(setosa['sepal_length'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Sepal Length")
plt.legend()

plt.subplot(224)
counts, bin_edges = np.histogram(setosa['sepal_width'], bins = 10, density = True)
pdf = counts / (sum(counts) )
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, label = 'PDF')
plt.plot(bin_edges[1:], cdf, label = 'CDF')
plt.title("Sepal Width")
plt.legend()

plt.savefig("d_setosaCDF.png")
plt.clf
plt.show()
#=================================================================================================

