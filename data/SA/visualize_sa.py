import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import re

# Zoek alle CSV-bestanden in de map met SA resultaten
csv_files = glob.glob("100trials_15iterations_sa_board*.csv")

# Dataframe maken voor alle bestanden
df_list = []

for file in csv_files:
    try:
        df = pd.read_csv(file)
        
        # Extract board position using regex
        match = re.search(r"board(\d+)", file)
        if match:
            board_position = int(match.group(1))
        else:
            continue
        
        # Voeg metadata toe
        df["board"] = f"Board {board_position}"
        df["improvement"] = df["random_moves"] - df["sa_moves"]
        df_list.append(df)
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Combineer alle data
full_df = pd.concat(df_list, ignore_index=True)

# Boxplot random vs sa
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
sns.barplot(data=full_df, x="board", y="improvement", palette="Set3")
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

# Scatterplot vergelijking
plt.figure(figsize=(10, 6))
sns.scatterplot(data=full_df, x="random_moves", y="sa_moves", hue="board", palette="Set1")
plt.plot([full_df["random_moves"].min(), full_df["random_moves"].max()],
         [full_df["random_moves"].min(), full_df["random_moves"].max()], 'k--')  # Referentielijn
plt.title("Vergelijking Random Moves vs. SA Moves")
plt.xlabel("Random Moves")
plt.ylabel("SA Moves")
plt.show()

# Boxplot runtime
plt.figure(figsize=(10, 6))
sns.boxplot(data=full_df, x="board", y="runtime", palette="Set2")
plt.title("Runtime van SA per Board (100 trials, 15 iterations)")
plt.xlabel("Board")
plt.ylabel("Runtime (seconden)")
plt.show()

# Opslaan naar Csv
full_df.to_csv("sa_algorithm_results.csv", index=False)
print("Data opgeslagen als sa_algorithm_results.csv")
