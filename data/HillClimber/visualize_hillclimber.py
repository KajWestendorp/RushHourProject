import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import re

# Zoek alle Hill Climber CSV-bestanden in de map
csv_files = glob.glob("100trials_500iterations_hillclimber_1_boardposition*.csv")

# Dataframe lijst om alle data op te slaan
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

        # "Not solved" omzetten naar NaN en onopgeloste runs verwijderen
        df.replace("Not solved", pd.NA, inplace=True)
        df.dropna(inplace=True)

        # Kolommen naar numeriek omzetten
        df["random_moves"] = pd.to_numeric(df["random_moves"], errors="coerce")
        df["hillclimber_moves"] = pd.to_numeric(df["hillclimber_moves"], errors="coerce")

        # Bereken verbetering
        df["improvement"] = df["random_moves"] - df["hillclimber_moves"]

        # Metadata toevoegen
        df["board"] = f"Board {board_position}"
        df["size"] = board_size 

        df_list.append(df)

    except Exception as e:
        print(f"Fout bij lezen van {file}: {e}")

# Debug voor t geval er geen data is
if not df_list:
    print("Geen geldige data ingelezen. Controleer de CSV-bestanden.")
    exit()

# Combineer data
hillclimber_df = pd.concat(df_list, ignore_index=True)

# Zorg ervoor dat borden correct worden geordend
order = ["6x6", "9x9", "12x12"]

# Boxplot per boardgrootte
plt.figure(figsize=(12, 6))
sns.boxplot(data=hillclimber_df.melt(id_vars=["size"], value_vars=["random_moves", "hillclimber_moves"]),
            x="size", y="value", hue="variable", palette="Set1", order=order)
plt.title("Boxplot: Random vs. HillClimber (100 trials - 500 iteraties)")
plt.xlabel("Boardgrootte")
plt.ylabel("Aantal Moves")
plt.legend(title='Algorithm', labels=['Random', 'Hill Climber'])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# Histogram van het aantal moves per boardgrootte
plt.figure(figsize=(12, 6))
sns.histplot(data=hillclimber_df, x="improvement", hue="size", bins=30, kde=True, palette="Set1", hue_order=order)
plt.title("Hill Climber Verbetering Over Random Algorithm (100 trials - 500 iteraties)")
plt.xlabel("Verbetering in Moves", fontsize=15)
plt.ylabel("Frequentie", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# Voor ordenen van bord posities
hillclimber_df["board"] = pd.Categorical(hillclimber_df["board"], 
                                         categories=["Board 1", "Board 2", "Board 3", "Board 4", "Board 5", "Board 6", "Board 7"], 
                                         ordered=True)

# Gemiddeld aantal moves per boardgrootte
plt.figure(figsize=(10, 6))
sns.lineplot(data=hillclimber_df, x="board", y="improvement", marker="o", hue="size", palette="Set1", hue_order=order)
plt.title("Gemiddelde verbetering per Bord (Random vs. Hill Climber) (100 trials - 500 iteraties)")
plt.xlabel("Bord Positie")
plt.ylabel("Moves verminderd door Hill Climber", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# Heatmap met alleen basisstatistieken
summary_stats = hillclimber_df.groupby("size")[["random_moves", "hillclimber_moves", "improvement"]].describe()
selected_stats = summary_stats.loc[:, (slice(None), ["mean", "std", "min", "max"])]  

plt.figure(figsize=(10, 5))
sns.heatmap(selected_stats.T, annot=True, fmt=".0f", cmap="Blues")
plt.title("Overzicht van Moves per Boardgrootte (100 trials - 500 iteraties)")
plt.show()

# Data opslaan
hillclimber_df.to_csv("hillclimber_algorithm_results.csv", index=False)
print("Data opgeslagen als hillclimber_algorithm_results.csv")
