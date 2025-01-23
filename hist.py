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

df2 = pd.read_csv('1000attempts.csv')
log_plot2 = sns.histplot(df2, log_scale=True, bins=20, legend=False)
log_plot2.set(xlabel ='Move count (log scale)')
log_plot2.set(ylabel = 'Frequency')
log_plot2.set(title = "The move counts for 1000 random algorithm attempts")
log_plot2.set()
plt.show()

df3 = pd.read_csv('1000attempts_9x9.csv')
log_plot3 = sns.histplot(df2, log_scale=True, bins=20, legend=False)
log_plot3.set(xlabel ='Move count (log scale)')
log_plot3.set(ylabel = 'Frequency')
log_plot3.set(title = "The move counts for 1000 random algorithm attempts for a 9x9 board")
log_plot3.set()
plt.show()

df4 = pd.read_csv('1000_trials_randomise_6x6.csv')
plot4 = sns.histplot(df4, bins=20, legend=False)
plot4.set(xlabel ='Move count')
plot4.set(ylabel = 'Frequency')
plot4.set(title = "The move counts for 100 random algorithm trials for a 6x6 board")
plot4.set()
plt.show()

df5 = pd.read_csv('1000_trials_randomise_heuristic_6x6.csv')
plot5 = sns.histplot(df5, bins=20, legend=False)
plot5.set(xlabel ='Move count')
plot5.set(ylabel = 'Frequency')
plot5.set(title = "The move counts for 100 random heuristic algorithm trials for a 6x6 board")
plot5.set()
plt.show()