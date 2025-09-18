# relPlot with multifacets [Dots]
import seaborn as sns
import matplotlib.pyplot as plt
relPlot = sns.load_dataset("dots")
pelette = sns.color_palette("rocket_r")
sns.relplot(x="time", y="firing_rate", data=relPlot, size="choice", col="align", kind="line", 
            palette=pelette, height=5, aspect=0.80, facet_kws=dict(sharex=False))
plt.show()


# BoxPlot (nested) [Tips]
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
BoxPlot = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", hue="smoker", data=BoxPlot, palette=["m", "g"])
sns.despine(offset=10, trim=True)
plt.show()


# ViolinPlot (nested) [Tips]
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
ViolinPlot = sns.load_dataset("tips")
# sns.violinplot(x="day", y="total_bill", hue="smoker", split=True, inner="quart", linewidth=1, data=ViolinPlot, palette={"Yes":"b", "No":".85"})
sns.violinplot(x="day", y="total_bill", hue="smoker", inner="quart", linewidth=1, data=ViolinPlot, palette={"Yes":"b", "No":".85"})
sns.despine(left=True)
plt.show()


# ScatterPlot (nested) [Tips]
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
ScatterPlot = sns.load_dataset("tips")
# sns.scatterplot(x="day", y="total_bill", hue="smoker", split="True", inner="quart", linewidth=1, data=ScatterPlot, palette={"Yes":"b", "No":".85"})
sns.scatterplot(x="day", y="total_bill", hue="smoker", linewidth=1, data=ScatterPlot, palette={"Yes":"b", "No":".85"})
sns.despine(left=True)
plt.show()


# For more plots go to seaborn website -> Example Gallery for more Plots