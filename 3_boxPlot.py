#BoxPlot [Tips]
import seaborn as sns
import matplotlib.pyplot as plt
BoxPlot = sns.load_dataset("tips")
sns.boxplot(x="day", y="tip", data=BoxPlot)
plt.show()


#Only show x data
import seaborn as sns
import matplotlib.pyplot as plt
BoxPlot = sns.load_dataset("tips")
sns.boxplot(x='tip', data=BoxPlot)
plt.show()


#Flip x and y
import seaborn as sns
import matplotlib.pyplot as plt
BoxPlot = sns.load_dataset("tips")
sns.boxplot(x="tip", y="day", data=BoxPlot)
plt.show()


#Add hue, palette, dodge
import seaborn as sns
import matplotlib.pyplot as plt
BoxPlot = sns.load_dataset("tips")
sns.boxplot(x="tip", y="day", hue="smoker", palette="pastel", dodge=True, data=BoxPlot)
plt.show()


#Add orient v/h
import seaborn as sns
import matplotlib.pyplot as plt
BoxPlot = sns.load_dataset("tips")
sns.boxplot(x="tip", y="day", hue="smoker", palette="pastel", dodge=True, orient='v', data=BoxPlot)
plt.show()


#Add color
import seaborn as sns
import matplotlib.pyplot as plt
BoxPlot = sns.load_dataset("tips")
sns.boxplot(x="tip", y="day", hue="smoker", color="red", data=BoxPlot)
# sns.boxplot(x="tip", y="day", hue="smoker", palette='dark:red', data=BoxPlot)
plt.show()


#how to manage individual colors for each hue color

# ............................................................................
#BoxPlot [Titanic]
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
BoxPlot1 = sns.load_dataset("titanic")
sns.boxplot(x="survived", y="age", data=BoxPlot1)
plt.show()


#show mean
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
BoxPlot1 = sns.load_dataset("titanic")
sns.boxplot(x="survived", y="age", showmeans=True, data=BoxPlot1)
plt.show()


#Add mean props
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
BoxPlot1 = sns.load_dataset("titanic")
sns.boxplot(x="survived", y="age", showmeans=True, meanprops={"marker":"*", "markersize":"12", "markeredgecolor":"red"}, data=BoxPlot1)
plt.show()


#show labels, title and their size,weight
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
BoxPlot1 = sns.load_dataset("titanic")
sns.boxplot(x="survived", y="age", showmeans=True, meanprops={"marker":"*", "markersize":"12", "markeredgecolor":"red"}, data=BoxPlot1)
plt.xlabel("How many survived", size=14),
plt.ylabel("Age (years)", size=14),
plt.title("Box Plot for Titanic", size=14, weight="bold")
plt.show()


# what is facet wrap and facet grid in boxplot?