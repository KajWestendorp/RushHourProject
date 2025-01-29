import os
import pandas as pd
import time
import copy
from code.algorithms.random_algorithm import Random_Algorithm
from code.algorithms.random_heuristic import Random_Heuristic
from code.algorithms.hillclimber import HillClimber
from code.algorithms.sa import SimulatedAnnealing
from code.algorithms.BreadthFirst import RushHourBFS
from code.algorithms.hillclimber2 import HillClimber2
from code.classes.grid import Grid
from code.visualization.initBoard import visualize_board

# https://stackoverflow.com/questions/12229064/mapping-over-values-in-a-python-dictionary
# Load board files in dictionary to be more dynamic
script_dir = os.path.dirname(os.path.abspath(__file__))
board_files = {
    '1': os.path.normpath(os.path.join(script_dir, "code", "gameboards", "Rushhour6x6_1.csv")),
    '2': os.path.normpath(os.path.join(script_dir, "code", "gameboards", "Rushhour6x6_2.csv")),
    '3': os.path.normpath(os.path.join(script_dir, "code", "gameboards", "Rushhour6x6_3.csv")),
    '4': os.path.normpath(os.path.join(script_dir, "code", "gameboards", "Rushhour9x9_4.csv")),
    '5': os.path.normpath(os.path.join(script_dir, "code", "gameboards", "Rushhour9x9_5.csv")),
    '6': os.path.normpath(os.path.join(script_dir, "code", "gameboards", "Rushhour9x9_6.csv")),
    '7': os.path.normpath(os.path.join(script_dir, "code", "gameboards", "Rushhour12x12_7.csv"))
}

# Map for board size and position
board_sizes = {'1': 6, '2': 6, '3': 6, '4': 9, '5': 9, '6': 9, '7': 12}

# Algorithm choices map
algorithms = {
    "1": ("Random Algorithm", Random_Algorithm),
    "2": ("Random + Heuristic", Random_Heuristic),
    "3": ("Hill Climber", HillClimber),
    "4": ("Simulated Annealing", SimulatedAnnealing),
    "5": ("Breadth First Search", RushHourBFS),
    "6": ("Depth First Search", RushHourBFS),
    "7": ("Hill Climber Optimized", HillClimber2)
}

# Print algorithm options
print("\nAvailable algorithms:")
for key, (name, _) in algorithms.items():
    print(f"  {key}. {name}")

# Retrieve input
algorithm = input("Select an algorithm (1-7): ").strip()
num_trials = int(input("Enter number of trials: ").strip())
iterations = int(input("Enter number of iterations: ").strip())

# Print board options
print("\nAvailable board positions:")
for key, value in board_files.items():
    print(f"  {key}. {value.split('/')[-1]}")  

# Retrieve input
board_choice = input("Select a board (1-7): ").strip()
if board_choice not in board_files:
    print("Invalid board choice!")
    exit()

# Load selected board file and size
board_df = pd.read_csv(board_files[board_choice], sep=',', encoding='utf-8')
board_size = board_sizes[board_choice]

# Algorithm choice for HillClimber and SA
if algorithm in ["3", "4", "7"]:
    print("Do you want to use the (1) random or (2) random + heuristic algorithm: ")
    random_start_algorithm = int(input())  
    
# Initialize results list
results = []

print(f"\nRunning {num_trials} trials for {algorithms[algorithm][0]} on board {board_choice}")

# Run selected algorithm for the specified number of trials
for trial in range(num_trials):
    print(f"Trial {trial + 1}/{num_trials}")

    # Initialize Grid
    grid = Grid(board_size)
    grid.create_grid()
    grid.add_borders()
    grid.add_cars_to_board(board_df)

    # Start timing
    start_time = time.time()

    # BFS or DFS
    if algorithm in ["5", "6"]:  
        solver = RushHourBFS(grid)

        # Needed for the run method in algorithm
        algorithm_type = 0 if algorithm == "5" else 1
        solution_df = solver.run(algorithm_type)

        end_time = time.time()
        runtime = end_time - start_time

        # Check if solution exists and is valid
        if solution_df is not None and not solution_df.empty:
            moves_made = len(solution_df)

            # Save the solution of move sequences dataFrame 
            solution_filename = f"solution_BFS_{board_choice}.csv" if algorithm == "5" else f"solution_DFS_{board_choice}.csv"
            solution_df.to_csv(solution_filename, index=False)
        else:
            moves_made = "Not solved"

        # Save move count and runtime
        results.append([moves_made, runtime])
        visualize_board(grid, solution_filename)

        

    # Random or Random Heuristic
    elif algorithm in ["1", "2"]:  
        solver = algorithms[algorithm][1](grid)
        moves_made = solver.run(iterations=iterations, verbose=False)
        end_time = time.time()
        runtime = end_time - start_time

        # Save move count and runtime
        results.append([len(moves_made), runtime])

   # HillClimber or SA or Optimized HillClimber
    elif algorithm in ["3", "4", "7"]:

        # Solve grid using Random Algorithm first
        random_solver = Random_Algorithm(grid) if random_start_algorithm == 1 else Random_Heuristic(grid)
        random_moves = random_solver.run(iterations=100000, verbose=False)

        # Ensure grid is solved before passing to HillClimber/SA
        if not random_solver.is_solution():
            print(f"Random Algorithm failed to solve the board in Trial {trial + 1}. Skipping.")
            results.append(["Not solved", "Not solved", "N/A"])
            continue

        # Deepcopy solved grid
        solved_grid = copy.deepcopy(random_solver.grid)

        # Run Hill Climber or SA on solved grid
        solver_class = algorithms[algorithm][1]
        solver = solver_class(solved_grid, temperature=5) if algorithm == "4" else solver_class(solved_grid)
        best_moves = solver.run(iterations=iterations, verbose=False)

        end_time = time.time()
        runtime = end_time - start_time

        # Ensure best_moves contains a valid solution
        final_moves = len(best_moves) if best_moves else "Not solved"
        
        # Store move count, improved move count and runtime
        results.append([len(random_moves), final_moves, runtime])


# Save results dynamically 
columns_mapping = {
    "1": ["moves", "runtime"],
    "2": ["moves", "runtime"],
    "3": ["random_moves", "hillclimber_moves", "runtime"],
    "4": ["random_moves", "sa_moves", "runtime"],
    "5": ["moves", "runtime"],
    "6": ["moves", "runtime"],
    "7": ["random_moves", "optimized_hillclimber_moves", "runtime"]
}

df_results = pd.DataFrame(results, columns=columns_mapping[algorithm])
# Replace spaces in map with lowercase
output_filename = f"{num_trials}trials_{iterations}iterations_{algorithms[algorithm][0].replace(' ', '_')}_board{board_choice}.csv"
df_results.to_csv(output_filename, index=False)

print(f"\nAlgorithm finished! Results saved to {output_filename}.")
