import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import re

# Zoek alle CSV-bestanden in de map
csv_files = glob.glob("100trials_*iterations_randomalgorithm_boardposition*.csv")

# Dataframe maken voor alle bestanden
df_list = []

for file in csv_files:
    try:
        df = pd.read_csv(file)

        # Regex om de boardpositie uit de bestandsnaam te halen
        match = re.search(r"boardposition(\d+)", file)
        if match:
            board_position = int(match.group(1))
        else:
            board_position = "Unknown"

        # Bepaal de boardgrootte
        if board_position in [1, 2, 3]:
            board_size = "6x6"
        elif board_position in [4, 5, 6]:
            board_size = "9x9"
        elif board_position == 7:
            board_size = "12x12"
        else:
            board_size = "Unknown"

        df["board"] = f"Board {board_position}"
        df["size"] = board_size 
        
        # Zorg ervoor dat moves numeriek is en verwijder de niet-opgeloste waarden
        df = df[pd.to_numeric(df["moves"], errors='coerce').notna()]
        df["moves"] = df["moves"].astype(int)
        
        df_list.append(df)
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Combineer alle data
full_df = pd.concat(df_list, ignore_index=True)

# Basisstatistieken per boardgrootte
stats = full_df.groupby("size")["moves"].describe()
print("\nStatistieken per boardgrootte:\n", stats)

# Boxplot per boardgrootte
plt.figure(figsize=(10, 6))
sns.boxplot(x="size", y="moves", data=full_df, palette="Set2")
plt.title("Boxplot: Moves per boardgrootte (100 trials - 200.000 iteraties)")
plt.xlabel("Boardgrootte")
plt.ylabel("Aantal Moves")
plt.show()

# Histogram van het aantal moves per boardgrootte
plt.figure(figsize=(12, 6))
sns.histplot(data=full_df, x="moves", hue="size", bins=30, kde=True, palette="Set1")
plt.title("Histogram van het aantal moves per boardgrootte (100 trials - 200.000 iteraties)")
plt.xlabel("Aantal Moves")
plt.ylabel("Frequentie")
plt.show()

# Gemiddeld aantal moves per boardgrootte
plt.figure(figsize=(10, 6))
sns.barplot(x="size", y="moves", data=full_df, estimator=lambda x: sum(x)/len(x), palette="Set3")
plt.title("Gemiddeld aantal moves per boardgrootte (100 trials - 200.000 iteraties)")
plt.xlabel("Boardgrootte")
plt.ylabel("Gemiddeld aantal moves")
plt.show()

plt.figure(figsize=(10, 4))
sns.heatmap(full_df.groupby("size")["moves"].describe(), annot=True, fmt=".0f", cmap="Blues")
plt.title("Overzicht van Moves per Boardgrootte (100 trials - 200.000 iteraties)")
plt.show()


full_df.to_csv("random_algorithm_results.csv", index=False)
print("Data opgeslagen als random_algorithm_results.csv")
