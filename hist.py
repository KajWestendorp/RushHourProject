import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('10000attempts.csv')
log_plot = sns.histplot(df, log_scale=True, bins = 20, legend=False)

log_plot.set(xlabel ='Move count (log scale)')
log_plot.set(ylabel = 'Frequency')
log_plot.set(title = "The move counts for 10,000 random algorithm attempts")
log_plot.set()
plt.show()
