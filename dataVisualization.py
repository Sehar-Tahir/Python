# pip install seaborn
# Steps for Data Visualization

# step 1- import libraries
# step 2- set a theme
# step 3- import data set / import your own data
# step 4- plot basic graph
# step 5- add title to plot


# a- BarPlots
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic = sns.load_dataset("titanic")

# print(titanic)
sns.catplot(x="who", y="survived", hue="class", kind="bar", data=titanic)
plt.show()



# b- CountPlots
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic = sns.load_dataset("titanic")

p1=sns.countplot(x='sex', data=titanic, hue='class')
p1.set_title("Plot for Couting")
plt.show()



# c- ScatterPlots
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic = sns.load_dataset("titanic")

g = sns.FacetGrid(titanic, row="sex", hue="alone")
g = (g.map(plt.scatter, "age", "fare").add_legend())
plt.show()

