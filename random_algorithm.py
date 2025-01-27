# Imports
import pandas as pd
import random
import os
import copy
from code.algorithms.random_algorithm import Random_Algorithm
from code.classes.grid import *
from code.classes.car import *

# Path file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Board path files
relative_path6x6_1 = os.path.join("code", "gameboards", "Rushhour6x6_1.csv")
relative_path6x6_2 = os.path.join("code", "gameboards", "Rushhour6x6_2.csv")
relative_path6x6_3 = os.path.join("code", "gameboards", "Rushhour6x6_3.csv")
relative_path9x9_1 = os.path.join("code", "gameboards", "Rushhour9x9_4.csv")
relative_path9x9_2 = os.path.join("code", "gameboards", "Rushhour9x9_5.csv")
relative_path9x9_3 = os.path.join("code", "gameboards", "Rushhour9x9_6.csv")
relative_path12x12_1 = os.path.join("code", "gameboards", "Rushhour12x12_7.csv")

# Board files
board_file6x6_1 = os.path.normpath(os.path.join(script_dir, relative_path6x6_1))
board_file6x6_2 = os.path.normpath(os.path.join(script_dir, relative_path6x6_2))
board_file6x6_3 = os.path.normpath(os.path.join(script_dir, relative_path6x6_3))
board_file9x9_1 = os.path.normpath(os.path.join(script_dir, relative_path9x9_1))
board_file9x9_2 = os.path.normpath(os.path.join(script_dir, relative_path9x9_2))
board_file9x9_3 = os.path.normpath(os.path.join(script_dir, relative_path9x9_3))
board_file12x12_1 = os.path.normpath(os.path.join(script_dir, relative_path12x12_1))

# Final Board positions
boardposition6x6_1 = pd.read_csv(board_file6x6_1, sep=',', encoding='utf-8')
boardposition6x6_2 = pd.read_csv(board_file6x6_2, sep=',', encoding='utf-8')
boardposition6x6_3 = pd.read_csv(board_file6x6_3, sep=',', encoding='utf-8')
boardposition9x9_1 = pd.read_csv(board_file9x9_1, sep=',', encoding='utf-8')
boardposition9x9_2 = pd.read_csv(board_file9x9_2, sep=',', encoding='utf-8')
boardposition9x9_3 = pd.read_csv(board_file9x9_3, sep=',', encoding='utf-8')
boardposition12x12_1 = pd.read_csv(board_file12x12_1, sep=',', encoding='utf-8')

# Lookup table
# https://stackoverflow.com/questions/69334309/choose-variable-via-input-python
lookup = {'1': boardposition6x6_1, '2': boardposition6x6_2, '3': boardposition6x6_3, '4': boardposition9x9_1,
          '5': boardposition9x9_2, '6': boardposition9x9_3, '7': boardposition12x12_1}

"""----- Random Algorithm -----"""
# Number of trials
print("How many trials do you want to let the Random Algorithm run: ")
num_trials = int(input())

print("What boardposition do you want to experiment on: ")
boardposition = input()
board = lookup.get(boardposition)
if board is None:
    print(f"Board {board} not found")

print("How many iterations do you want to set: ")
iterations = int(input())

# Determine board size based on boardposition
board_sizes = {'1': 6, '2': 6, '3': 6, 
               '4': 9, '5': 9, '6': 9, 
               '7': 12}

board_size = board_sizes.get(boardposition)

# Results storage
random_results = []

# Run trials for Random_Algorithm
print(f"\nRunning {num_trials} trials for Random Algorithm")
for trial in range(num_trials):
    print(f"Trial {trial + 1}/{num_trials}")

    # Initialize and reset grid
    grid = Grid(board_size)
    grid.create_grid()
    grid.add_borders()
    grid.add_cars_to_board(board)

    # Run random algorithm
    solver = Random_Algorithm(grid)
    moves_made = solver.run(iterations=iterations, verbose=False)

    # Store result
    if solver.is_solution():
        random_results.append(len(moves_made))
    else:
        random_results.append("Not solved")

# Save results
df_random = pd.DataFrame(random_results, columns=['moves'])
df_random.to_csv((f"{num_trials}trials_{iterations}iterations_randomalgorithm_boardposition{boardposition}.csv"), index=False)
print("\nRandom Algorithm finished")
    