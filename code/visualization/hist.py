import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_csv('10000attempts.csv')
# log_plot = sns.histplot(df, log_scale=True, bins = 20, legend=False)

# log_plot.set(xlabel ='Move count (log scale)')
# log_plot.set(ylabel = 'Frequency')
# log_plot.set(title = "The move counts for 10,000 random algorithm attempts")
# log_plot.set()
# plt.show()

# df2 = pd.read_csv('1000attempts.csv')
# log_plot2 = sns.histplot(df2, log_scale=True, bins=20, legend=False)
# log_plot2.set(xlabel ='Move count (log scale)')
# log_plot2.set(ylabel = 'Frequency')
# log_plot2.set(title = "The move counts for 1000 random algorithm attempts")
# log_plot2.set()
# plt.show()

# df3 = pd.read_csv('1000attempts_9x9.csv')
# log_plot3 = sns.histplot(df2, log_scale=True, bins=20, legend=False)
# log_plot3.set(xlabel ='Move count (log scale)')
# log_plot3.set(ylabel = 'Frequency')
# log_plot3.set(title = "The move counts for 1000 random algorithm attempts for a 9x9 board")
# log_plot3.set()
# plt.show()

# df4 = pd.read_csv('1000_trials_randomise_6x6.csv')
# plot4 = sns.histplot(df4, bins=20, legend=False)
# plot4.set(xlabel ='Move count')
# plot4.set(ylabel = 'Frequency')
# plot4.set(title = "The move counts for 100 random algorithm trials for a 6x6 board")
# plot4.set()
# plt.show()

# df5 = pd.read_csv('1000_trials_randomise_heuristic_6x6.csv')
# plot5 = sns.histplot(df5, bins=20, legend=False)
# plot5.set(xlabel ='Move count')
# plot5.set(ylabel = 'Frequency')
# plot5.set(title = "The move counts for 100 random heuristic algorithm trials for a 6x6 board")
# plot5.set()
# plt.show()

# HILLCLIMBER VISUALISATIONS
df6 = pd.read_csv("hillclimber_comparison_6x6.csv")

# ABSOLUTE IMPROVEMENT OVER RANDOM
df6["Improvement"] = df6["random_moves"] - df6["hillclimber_moves"]
plt.bar(df6.index, df6["Improvement"], color="lightblue")

# Labels
plt.xlabel("Trial Number")
plt.ylabel("Move Reduction (Random - HillClimber)")
plt.title("HillClimber Move Reduction Over Random Algorithm")

# print number of reduced moves 
for i, val in enumerate(df6["Improvement"]):
    plt.text(i, val + 15, str(val), ha="center", fontsize=10)
plt.show()

# PERCENTAGE IMPROVEMENT
df6["Percent Improvement"] = ((df6["random_moves"] - df6["hillclimber_moves"]) / df6["random_moves"]) * 100
plt.figure(figsize=(10, 6))
plt.plot(df6.index, df6["Percent Improvement"], marker="o", linestyle="-", color="lightblue")

# Labels
plt.xlabel("Trial Number")
plt.ylabel("Percentage Improvement (%)")
plt.title("HillClimber Percentage Improvement Over Random Algorithm")
plt.ylim(0, max(df6["Percent Improvement"]) + 2)

# print values
for i, val in enumerate(df6["Percent Improvement"]):
    plt.text(i, val + 0.5, f"{val:.1f}%", ha="center", fontsize=10)
plt.show()