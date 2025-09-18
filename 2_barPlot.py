#BarPlot [Titanics]
import seaborn as sns
import matplotlib.pyplot as plt
BarPlot = sns.load_dataset("titanic")
sns.barplot(x="sex", y="alone", hue="who", data=BarPlot)
plt.show()


#Add Order
import seaborn as sns
import matplotlib.pyplot as plt
BarPlot = sns.load_dataset("titanic")
sns.barplot(x="sex", y="alone", hue="who", data=BarPlot, order=["female", "male"])
plt.show()


#Add Color
import seaborn as sns
import matplotlib.pyplot as plt
BarPlot = sns.load_dataset("titanic")
sns.barplot(x="sex", y="alone", hue="who", data=BarPlot, color= "blue", order=["female", "male"])
# sns.barplot(x="sex", y="alone", hue="who", data=BarPlot, palette='dark:blue, order=["female", "male"])........
plt.show()


#Remove Plot lines
import seaborn as sns
import matplotlib.pyplot as plt
BarPlot = sns.load_dataset("titanic")
sns.barplot(x="sex", y="alone", hue="who", data=BarPlot, order=["female", "male"], color= "blue", ci=None)
plt.show()


#Add Pallete Color
import seaborn as sns
import matplotlib.pyplot as plt
BarPlot = sns.load_dataset("titanic")
sns.barplot(x="sex", y="alone", hue="who", data=BarPlot, order=["female", "male"], palette="pastel")
plt.show()


#Add Estimator (also add another library numpy )
import seaborn as sns
# from numpy import median
from numpy import mean
import matplotlib.pyplot as plt
BarPlot = sns.load_dataset("titanic")
sns.barplot(x="sex", y="alone", hue="who", data=BarPlot, order=["female", "male"], estimator=mean,)
plt.show()


#Add Saturation of colour
import seaborn as sns
import matplotlib.pyplot as plt
BarPlot = sns.load_dataset("titanic")
sns.barplot(x="sex", y="alone", hue="who", data=BarPlot, order=["female", "male"], saturation= 0.5)
plt.show()


#Horizontal Plot
import seaborn as sns
import matplotlib.pyplot as plt
BarPlot = sns.load_dataset("titanic")
sns.barplot(x="alone", y="sex", hue="who", data=BarPlot, order=["female", "male"], saturation= 0.5)
plt.show()


#Bar plot as a stroke/outline not filled
import seaborn as sns
import matplotlib.pyplot as plt
BarPlot = sns.load_dataset("titanic")
sns.barplot(x="sex", y="alone", data=BarPlot, linewidth=3, facecolor=(1,1,1,0), errcolor=".2", edgecolor=".2")
plt.show()