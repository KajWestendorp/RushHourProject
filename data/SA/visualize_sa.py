# Re-import necessary libraries after execution reset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import re

# Re-uploaded CSV files paths
csv_files = [
    "100trials_15iterations_Simulated_Annealing_board1.csv",
    "100trials_15iterations_Simulated_Annealing_board2.csv",
    "100trials_15iterations_Simulated_Annealing_board3.csv",
    "100trials_15iterations_Simulated_Annealing_board4.csv",
    "100trials_15iterations_Simulated_Annealing_board5.csv",
    "100trials_15iterations_Simulated_Annealing_board6.csv"
]

# Dataframe list to store all data
df_list = []

# Elke file 
for file in csv_files:
    try:
        df = pd.read_csv(file)
        
        # Regex voor bestandsnaam
        match = re.search(r"board(\d+)", file)
        if match:
            board_position = int(match.group(1))
        else:
            continue
        
        # Omzetten naar numerieke waardes
        df["random_moves"] = pd.to_numeric(df["random_moves"], errors="coerce")
        df["sa_moves"] = pd.to_numeric(df["sa_moves"], errors="coerce")
        df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce")

        # Info toevoegen
        df["board"] = f"Board {board_position}"
        df["improvement"] = df["random_moves"] - df["sa_moves"]
        df_list.append(df)
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Combineer data
full_df = pd.concat(df_list, ignore_index=True)

# Boxplot random vs SA
plt.figure(figsize=(12, 6))
sns.boxplot(data=full_df.melt(id_vars=["board"], value_vars=["random_moves", "sa_moves"]),
            x="board", y="value", hue="variable", palette="Set2")
plt.title("Boxplot: Random vs. SA (100 trials, 15 iterations)")
plt.xlabel("Board")
plt.ylabel("Aantal Moves")
plt.legend(title='Algorithm', labels=['Random', 'Simulated Annealing'])
plt.show()

# Barplot gemiddelde verbetering
plt.figure(figsize=(10, 6))
sns.barplot(data=full_df, x="board", y="improvement", palette="Set2")
plt.title("Gemiddelde verbetering door SA (100 trials, 15 iterations)")
plt.xlabel("Board")
plt.ylabel("Verminderde Moves")
plt.show()

# Histogram aantal moves
plt.figure(figsize=(12, 6))
sns.histplot(data=full_df, x="random_moves", bins=30, kde=True, color="blue", label="Random")
sns.histplot(data=full_df, x="sa_moves", bins=30, kde=True, color="red", label="SA", alpha=0.6)
plt.title("Histogram van Moves: Random vs. SA (100 trials, 15 iterations)")
plt.xlabel("Aantal Moves")
plt.ylabel("Frequentie")
plt.legend()
plt.show()


# Save naar CSV
output_file = "sa_algorithm_results.csv"
full_df.to_csv(output_file, index=False)

