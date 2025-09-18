#LinePlot [Flower]
import seaborn as sns
import matplotlib.pyplot as plt
LinePlot = sns.load_dataset("iris")
sns.lineplot(x="sepal_length", y="sepal_width", data=LinePlot)
plt.show()


#Add Title
import seaborn as sns
import matplotlib.pyplot as plt
LinePlot = sns.load_dataset("iris")
sns.lineplot(x="sepal_length", y="sepal_width", data=LinePlot)
plt.title("LinePlot of Flowers")
plt.show()


#Add Limits
import seaborn as sns
import matplotlib.pyplot as plt
LinePlot = sns.load_dataset("iris")
sns.lineplot(x="sepal_length", y="sepal_width", data=LinePlot)
plt.title("LinePlot of Flowers")
plt.xlim(7.5)
plt.ylim(3.8)
plt.show()


#Add Styles
import seaborn as sns
import matplotlib.pyplot as plt
LinePlot = sns.load_dataset("iris")
sns.lineplot(x="sepal_length", y="sepal_width", data=LinePlot)
plt.title("LinePlot of Flowers")
sns.set_style("darkgrid")
sns.set_style(style=None, rc=None)
plt.show()


#Add size of figure
import seaborn as sns
import matplotlib.pyplot as plt
LinePlot = sns.load_dataset("iris")
sns.lineplot(x="sepal_length", y="sepal_width", data=LinePlot)
plt.title("LinePlot of Flowers")
sns.set_style("darkgrid")
sns.set_style(style=None, rc=None)
plt.figure(figsize=(8,6))
plt.show()