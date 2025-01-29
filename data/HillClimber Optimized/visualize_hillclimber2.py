import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import re

# Zoek alle Hill Climber Optimized CSV-bestanden in de map
csv_files = glob.glob("100trials_*iterations_Hill_Climber_Optimized_board*.csv")

# Dataframe lijst om alle data op te slaan
df_list = []

for file in csv_files:
    try:
        df = pd.read_csv(file)

        # Regex om de boardpositie en iteraties uit de bestandsnaam te halen
        match = re.search(r"(\d+)trials_(\d+)iterations_Hill_Climber_Optimized_board(\d+)", file)
        if match:
            num_trials, iterations, board_position = match.groups()
            iterations = int(iterations)
            board_position = int(board_position)
        else:
            continue

        # Bepaal de boardgrootte
        board_size = "6x6" if board_position in [1, 2, 3] else "9x9" if board_position in [4, 5, 6] else "12x12"

        # "Not solved" omzetten naar NaN en onopgeloste runs verwijderen
        df.replace("Not solved", pd.NA, inplace=True)
        df.dropna(inplace=True)

        # Kolommen naar numeriek omzetten
        df["random_moves"] = pd.to_numeric(df["random_moves"], errors="coerce")
        df["optimized_hillclimber_moves"] = pd.to_numeric(df["optimized_hillclimber_moves"], errors="coerce")

        # Bereken verbetering
        df["improvement"] = df["random_moves"] - df["optimized_hillclimber_moves"]

        # Metadata toevoegen
        df["board"] = f"Board {board_position}"
        df["size"] = board_size
        df["iterations"] = iterations

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

# Boxplot moves per bordgrootte
plt.figure(figsize=(12, 6))
sns.boxplot(data=hillclimber_df.melt(id_vars=["size"], value_vars=["random_moves", "optimized_hillclimber_moves"]),
            x="size", y="value", hue="variable", palette="Set1", order=order)
plt.title("Boxplot: Random vs. Optimized HillClimber (100 trials)")
plt.xlabel("Bordgrootte")
plt.ylabel("Aantal Moves")
plt.legend(title='Algorithm', labels=['Random', 'Optimized Hill Climber'])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# Histogram verbetering
plt.figure(figsize=(12, 6))
sns.histplot(data=hillclimber_df, x="improvement", hue="size", bins=30, kde=True, palette="Set1", hue_order=order)
plt.title("Optimized Hill Climber Verbetering Over Random Algorithm (100 trials)")
plt.xlabel("Verbetering in Moves", fontsize=15)
plt.ylabel("Frequentie", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# Bordposities ordenen
hillclimber_df["board"] = pd.Categorical(hillclimber_df["board"], 
                                         categories=["Board 1", "Board 2", "Board 3", "Board 4", "Board 5", "Board 6", "Board 7"], 
                                         ordered=True)

# Verbetering per iteraties
plt.figure(figsize=(12, 6))
sns.lineplot(data=hillclimber_df, x="board", y="improvement", marker="o", hue="iterations", palette="Set1")
plt.title("Gemiddelde verbetering per Bord (Random vs. Optimized Hill Climber) (100 trials)")
plt.xlabel("Bord Positie")
plt.ylabel("Moves verminderd door Optimized Hill Climber", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(title="Iterations")
plt.show()

# Heatmap basisstatistieken
summary_stats = hillclimber_df.groupby(["size", "iterations"])[["random_moves", "optimized_hillclimber_moves", "improvement"]].describe()
selected_stats = summary_stats.loc[:, (slice(None), ["mean", "std", "min", "max"])]

plt.figure(figsize=(10, 5))
sns.heatmap(selected_stats.T, annot=True, fmt=".0f", cmap="Blues")
plt.title("Overzicht van Moves per Boardgrootte en Iteraties (100 trials)")
plt.show()

# Osplaan naar CSV
hillclimber_df.to_csv("optimized_hillclimber_algorithm_results.csv", index=False)
print("Data opgeslagen als optimized_hillclimber_algorithm_results.csv")
