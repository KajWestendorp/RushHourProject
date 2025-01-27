# Imports
import pandas as pd
import random
import os
import copy
from code.algorithms.hillclimber import HillClimber
from code.algorithms.random_algorithm import Random_Algorithm
from code.algorithms.random_heuristic import Random_Heuristic
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

"""----- HillClimber Algorithm -----"""
# Number of trials
print("How many trials do you want to let the HillClimber Algorithm run: ")
num_trials = int(input())

print("What boardposition do you want to experiment on: ")
boardposition = input()
board = lookup.get(boardposition)
if board is None:
    print(f"Board {board} not found")

print("How many iterations do you want to set: ")
iterations = int(input())

print("Do you want to use the (1) random or (2) random + heuristic algorithm: ")
algorithm = int(input())

# Determine board size based on boardposition
board_sizes = {'1': 6, '2': 6, '3': 6, 
               '4': 9, '5': 9, '6': 9, 
               '7': 12}

board_size = board_sizes.get(boardposition)

hillclimber_results = []

if algorithm == 1:
    print(f"\nRunning {num_trials} trials for Hill Climber + Random Algorithm")
else:
    print(f"\nRunning {num_trials} trials for Hill Climber + Random Heuristic Algorithm")

for trial in range(num_trials):
    print(f"Trial {trial + 1}/{num_trials}")

    # Initialize and reset grid
    grid = Grid(board_size)
    grid.create_grid()
    grid.add_borders()
    grid.add_cars_to_board(board)

    # Run algorithm
    solver = Random_Algorithm(grid) if algorithm == 1 else Random_Heuristic(grid)
    random_moves = solver.run(iterations=100000, verbose=False)

    if solver.is_solution():
        # Start by copying the solved grid, and locating the red car
        
        print("\nFinal Solved Grid Before Passing to HillClimber:")
        solver.print_grid()
        solved_grid = copy.deepcopy(solver.grid)

        hillclimber = HillClimber(solved_grid)
        best_moves = hillclimber.run(iterations=iterations, verbose=False)

        # Store results
        hillclimber_results.append((len(random_moves), len(best_moves) if best_moves else "Not solved"))
    else:
        print(f"Trial {trial + 1}: Algorithm failed to find a solution, skipping trial.")
        hillclimber_results.append(("Not solved", "Not solved"))

# Save results
df_hillclimber = pd.DataFrame(hillclimber_results, columns=['random_moves', 'hillclimber_moves'])
df_hillclimber.to_csv(f"{num_trials}trials_{iterations}iterations_hillclimber_{algorithm}_boardposition{boardposition}.csv", index=False)
print("\nHill Climber trials completed")
