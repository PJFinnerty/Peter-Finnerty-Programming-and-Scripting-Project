# IPython log file

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
df

df["sepal_length"]
df["sepal_width"]
df["petal_length"]
df["petal_width"]
#Next two lines incorrect
#df["species"]
#slVsw = (df["sepal_length] , df["sepal_width"])

#next line produces blank histogram
#plt.hist(df)

plt.hist(df["sepal_length"])
plt.show()

plt.hist(df["sepal_width"])
plt.show()

plt.hist(df["petal_length"])
plt.show()

plt.hist(df["petal_width"])
plt.show()

#next line not correct
#dfsetosa1 = df["sepal_length"] , df["species"]


#----------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
df

df["sepal_length"]
df["sepal_width"]
df["petal_length"]
df["petal_width"]

plt.hist(df["sepal_length"])
plt.show()

plt.hist(df["sepal_length"])
plt.title("Sepal Length All Sprecies")
plt.savefig("sepal_length.png")
plt.clf
()
plt.hist(df["Waiting"])
plt.savefig("Waiting.png")
exit()

