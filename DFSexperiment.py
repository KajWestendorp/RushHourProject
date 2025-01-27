
#Implement script that takes a board starting position and can keep updating it
import pandas as pd

import os

from code.classes.grid import *
from code.classes.car import *
from code.algorithms.random_grid import *
from code.algorithms.BreadthFirst import RushHourBFS

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
   
    relative_path = os.path.join("code", "gameboards", "Rushhour6x6_1.csv")
    relative_path2 = os.path.join("code", "gameboards", "Rushhour9x9_4.csv")
    relative_path3 = os.path.join("code", "gameboards", "Rushhour6x6_test.csv")
    relative_path4 = os.path.join("code", "gameboards", "Rushhour6x6_2.csv")
    relative_path5 = os.path.join("code", "gameboards", "Rushhour6x6_3.csv")
    relative_path9x9_5 = os.path.join("code", "gameboards", "Rushhour9x9_5.csv")
    relative_path9x9_6 = os.path.join("code", "gameboards", "Rushhour9x9_6.csv")

    # Construct the path to the gameboard file
    board_file = os.path.normpath(os.path.join(script_dir, relative_path))
    board_file2 = os.path.normpath(os.path.join(script_dir, relative_path2))
    board_file3 = os.path.normpath(os.path.join(script_dir, relative_path3))
    board_file4 = os.path.normpath(os.path.join(script_dir, relative_path4))
    board_file5 = os.path.normpath(os.path.join(script_dir, relative_path5))
    board_file9x9_5 = os.path.normpath(os.path.join(script_dir, relative_path9x9_5))
    board_file9x9_6 = os.path.normpath(os.path.join(script_dir, relative_path9x9_6))

    # visualize_board(boardposition1, 6)
    boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')
    boardposition2 = pd.read_csv(board_file2, sep=',', encoding='utf-8')
    boardposition3 = pd.read_csv(board_file3, sep=',', encoding='utf-8')
    boardposition4 = pd.read_csv(board_file4, sep=',', encoding='utf-8')
    boardposition5 = pd.read_csv(board_file5, sep=',', encoding='utf-8')
    boardposition9x9_5 = pd.read_csv(board_file9x9_5, sep=',', encoding='utf-8')
    boardposition9x9_6 = pd.read_csv(board_file9x9_5, sep=',', encoding='utf-8')


initial_grid = Grid(9)
initial_grid.create_grid()
initial_grid.add_borders()
initial_grid.add_cars_to_board(boardposition9x9_5)

#Run algorithm
import time

# # Calculate the end time and time taken (https://stackoverflow.com/questions/70058132/how-do-i-make-a-timer-in-python)
start = time.time()

Solved_grid = RushHourBFS(initial_grid)

#1 for DFS
final_grid, outputdf = RushHourBFS.run(Solved_grid, 1)
# Calculate the end time and time taken
end = time.time()
length = end - start
# Show the results : this can be altered however you like

print("It took", length, "seconds to find the best solution!")
print()