import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import re

# Zoek alle CSV-bestanden in de map
csv_files = [
    # "100trials_5000iterations_Random_+_Heuristic_board1.csv",
    # "100trials_5000iterations_Random_+_Heuristic_board2.csv",
    # "100trials_5000iterations_Random_+_Heuristic_board3.csv",
    # "100trials_10000iterations_Random_+_Heuristic_board1.csv",
    # "100trials_10000iterations_Random_+_Heuristic_board2.csv",
    # "100trials_10000iterations_Random_+_Heuristic_board3.csv",
    "100trials_10000iterations_Random_+_Heuristic_board4.csv",
    "100trials_10000iterations_Random_+_Heuristic_board5.csv",
    "100trials_10000iterations_Random_+_Heuristic_board6.csv"
]

df_list = []

for file in csv_files:
    try:
        df = pd.read_csv(file)

        # Regex voor board positie en iteraties
        match = re.search(r"(\d+)trials_(\d+)iterations_Random_\+_Heuristic_board(\d+)", file)
        if match:
            num_trials, iterations, board_position = match.groups()
            iterations = int(iterations)
            board_position = int(board_position)
        else:
            continue

        # Boardgrootte bepalen
        # if board_position in [1, 2, 3]:
        #     board_size = "6x6"
        if board_position in [4, 5, 6]:
            board_size = "9x9"
        else:
            continue

        # Info toevoegen
        df["board"] = f"Board {board_position}"
        df["size"] = board_size
        df["iterations"] = iterations
        
        # Edge cases behandelen
        df = df[pd.to_numeric(df["moves"], errors='coerce').notna()]
        df["moves"] = df["moves"].astype(int)
        
        df_list.append(df)
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Combineer data
if df_list:
    full_df = pd.concat(df_list, ignore_index=True)

# Order aangeven
order = ["9x9"]

# Basisstatistieken per boardgrootte
stats = full_df.groupby("size")["moves"].describe()
print("\nStatistieken per boardgrootte:\n", stats)

# Boxplot
plt.figure(figsize=(12, 6))
sns.boxplot(x="board", y="moves", hue="iterations", data=full_df, palette="Set2")
plt.title("Boxplot: Moves per bordpositie & iteraties (100 trials)")
plt.xlabel("Bordpositie", fontsize=16)
plt.ylabel("Aantal Moves", fontsize=16)
plt.legend(title="Iteraties")
plt.show()

# Barplot voor gemiddelde moves
plt.figure(figsize=(10, 6))
sns.barplot(x="board", y="moves", hue="iterations", data=full_df, estimator=lambda x: sum(x)/len(x), palette="Set3")
plt.title("Gemiddeld aantal moves per bordpositie en iteraties")
plt.xlabel("Bordpositie", fontsize=16)
plt.ylabel("Gemiddeld aantal Moves", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(title="Iteraties")
plt.show()

# Violin om distributie te verduidelijken
plt.figure(figsize=(12, 6))
sns.violinplot(x="board", y="moves", hue="iterations", data=full_df, split=True, inner="quartile", palette="Set1")
plt.title("Violin plot van het aantal moves per bordpositie en iteraties")
plt.xlabel("Bordpositie", fontsize=16)
plt.ylabel("Aantal Moves", fontsize=16)
plt.legend(title="Iteraties")
plt.show()

# Heatmap 
summary_stats = full_df.groupby(["board", "iterations"])["moves"].describe()[["mean", "std", "min", "max"]]
plt.figure(figsize=(12, 5))
sns.heatmap(summary_stats.unstack(), annot=True, fmt=".0f", cmap="Blues")
plt.title("Overzicht van Moves per Bordpositie en Iteraties (100 trials)")
plt.show()

# Opslaan naar csv.
full_df.to_csv("random_heuristic_algorithm_results.csv", index=False)
print("Data opgeslagen als random_heuristic_algorithm_results.csv")
