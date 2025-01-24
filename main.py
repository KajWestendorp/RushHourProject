#Implement script that takes a board starting position and can keep updating it
import pandas as pd
import random
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from code.movement.updatedf import update_positions
from code.visualization.initBoard import visualize_board

import os
import copy

from code.algorithms.random_algorithm import Random_Algorithm
from code.algorithms.random_heuristic import Random_Heuristic
from code.algorithms.hillclimber import HillClimber
from code.classes.grid import *
from code.classes.car import *
from code.movement.updatedf import *
from code.algorithms.random_grid import *
from code.algorithms.BreadthFirst import breadth_first

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
   
    relative_path = os.path.join("code", "gameboards", "Rushhour6x6_1.csv")
    relative_path2 = os.path.join("code", "gameboards", "Rushhour9x9_4.csv")
    relative_path3 = os.path.join("code", "gameboards", "Rushhour6x6_test.csv")
    relative_path4 = os.path.join("code", "gameboards", "Rushhour6x6_2.csv")
    relative_path5 = os.path.join("code", "gameboards", "Rushhour6x6_3.csv")
    relative_path6 = os.path.join("code", "gameboards", "Rushhour12x12_7.csv")

    # Construct the path to the gameboard file
    board_file = os.path.normpath(os.path.join(script_dir, relative_path))
    board_file2 = os.path.normpath(os.path.join(script_dir, relative_path2))
    board_file3 = os.path.normpath(os.path.join(script_dir, relative_path3))
    board_file4 = os.path.normpath(os.path.join(script_dir, relative_path4))
    board_file5 = os.path.normpath(os.path.join(script_dir, relative_path5))
    board_file6 = os.path.normpath(os.path.join(script_dir, relative_path6))

    # visualize_board(boardposition1, 6)
    boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')
    boardposition2 = pd.read_csv(board_file2, sep=',', encoding='utf-8')
    boardposition3 = pd.read_csv(board_file3, sep=',', encoding='utf-8')
    boardposition4 = pd.read_csv(board_file4, sep=',', encoding='utf-8')
    boardposition5 = pd.read_csv(board_file5, sep=',', encoding='utf-8')
    boardposition6 = pd.read_csv(board_file6, sep=',', encoding='utf-8')

    """----- Random Algorithm -----"""
    # Number of trials
    # num_trials = 10
    # iterations = 10000

    # # Results storage
    # random_results = []
    # heuristic_results = []

    """
    # Run trials for Random_Algorithm
    print(f"\nRunning {num_trials} trials for Random Algorithm")
    for trial in range(num_trials):
        print(f"Trial {trial + 1}/{num_trials}")

        # Initialize and reset grid
        grid = Grid(6)
        grid.create_grid()
        grid.add_borders()
        grid.add_cars_to_board(boardposition1)

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
    df_random.to_csv("1000_trials_randomise_6x6.csv", index=False)
    print("\nRandom Algorithm trials completed")
    """

    """
    # Run trials for Random_Heuristic
    print(f"\nRunning {num_trials} trials for Random Heuristic Algorithm")
    for trial in range(num_trials):
        print(f"Trial {trial + 1}/{num_trials}")

        # Initialize and reset grid
        grid = Grid(6)
        grid.create_grid()
        grid.add_borders()
        grid.add_cars_to_board(boardposition1)

        # Run random_heuristic algorithm
        solver = Random_Heuristic(grid)
        moves_made = solver.run(iterations=iterations, verbose=False)

        # Store result
        if solver.is_solution():
            heuristic_results.append(len(moves_made))
        else:
            heuristic_results.append("Not solved")

    # Save heuristic results to CSV
    df_heuristic = pd.DataFrame(heuristic_results, columns=['moves'])
    df_heuristic.to_csv("10_trials_randomise_heuristic_6x6.csv", index=False)
    print("\nRandom Heuristic Algorithm trials completed")
    """

    """----- HillClimber Algorithm -----"""
    # num_trials = 10
    # iterations = 1000  

    # hillclimber_results = []

    # print(f"\nRunning {num_trials} trials for Hill Climber Algorithm")
    # for trial in range(num_trials):
    #     print(f"Trial {trial + 1}/{num_trials}")

    #     # Generate grid
    #     grid = Grid(6)
    #     grid.create_grid()
    #     grid.add_borders()
    #     grid.add_cars_to_board(boardposition1)

    #     # Solve the puzzle with Random Algorithm
    #     solver = Random_Algorithm(grid)
    #     random_moves = solver.run(iterations=100000, verbose=False)

    #     # Ensure we pass a solved grid to HillClimber
    #     if solver.is_solution():
    #         print("\nPassing solved grid to HillClimber...")

    #         # Deepcopy the grid AFTER solving to capture the solved state
    #         solved_grid = copy.deepcopy(solver.grid)

    #         # Debugging check
    #         print("\nFinal Solved Grid Before Passing to HillClimber:")
    #         solved_grid.print_grid()  # Ensure red car is in the correct position

    #         hillclimber = HillClimber(solved_grid)
    #         best_moves = hillclimber.run(iterations=iterations, verbose=False)

    #         # Store results
    #         hillclimber_results.append({
    #             "random_moves": len(random_moves),
    #             "hillclimber_moves": len(best_moves) if best_moves else "Not solved"
    #         })
    #     else:
    #         print("Random Algorithm failed to find a solution, skipping trial.")
    #         hillclimber_results.append({
    #             "random_moves": "Not solved",
    #             "hillclimber_moves": "Not solved"
    #         })

    # # Save results to CSV
    # df_hillclimber = pd.DataFrame(hillclimber_results)
    # df_hillclimber.to_csv("hillclimber_comparison_6x6.csv", index=False)
    # print("\nHill Climber Algorithm trials completed and saved.")

"----- Experiment for random data -----"

# Change value when changing board size
# boardsize = 9
# grid = Grid(boardsize)
# grid.create_grid()
# grid.add_borders()

# # Change value when changing board
# grid.add_cars_to_board(boardposition2)
# for row in grid.grid:
#     #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
#     print(" ".join(str(cell) for cell in row))
# print()
# total_moves = 0
# solved = False
# trials = 1
# attempt_number = 0
# experimentdata = []
# for i in range(trials):
#     attempt_number += 1

#     # Change value when changing board size
#     boardsize = 6  
#     grid = Grid(boardsize)
#     grid.create_grid()
#     grid.add_borders()

#     # Change value when changing board 
#     grid.add_cars_to_board(boardposition3)
#     total_moves = 0
#     solved = False

#     while not solved:
#         if valid_board(grid.cars):
#             car_to_move, direction = random_move(grid)
#             if car_to_move:
#                 total_moves += 1
#                 direction_str = "forward" if direction > 0 else "backward"
#         else:
#             break

#         # Check if board is solved
#         if grid.grid_solved():
#             experimentdata.append(total_moves)
            
#             for move in grid.car_moves:
#                 print(move)

#             solved = True
# df_of_experiment = pd.DataFrame(experimentdata)
# print(df_of_experiment)

# df_of_experiment.to_csv('1000attempts_9x9.csv', header='Move Count', index=False)


# """----- BreadthFirstSearch Algorithm -----"""
initial_grid = Grid(12)
initial_grid.create_grid()
initial_grid.add_borders()
initial_grid.add_cars_to_board(boardposition2)

#Run algorithm
import time

# Calculate the start time
start = time.time()
final_grid, outputdf = breadth_first(initial_grid)
# Calculate the end time and time taken
end = time.time()
length = end - start
# Show the results : this can be altered however you like

print("It took", length, "seconds to find the best solution!")
print()

print(outputdf)
outputdf.to_csv('output.csv',index=False)

#nOTES

# 6x6 Board 1 output = checked, Movecount = 
# 6x6 Board 2 output = checked, Movecount = 
# 6x6 Board 3 output = checked, Movecount = 

# 9x9 board 4 output = checked, Movecount = 
# 9x9 board 5 output = checked, Movecount =
# 9x9 board 6 output = checked, Movecount =

# 12x12 board 7 output = 

