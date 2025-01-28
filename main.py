#Implement script that takes a board starting position and can keep updating it
import pandas as pd
import random
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import time
import os
import copy

from code.algorithms.random_algorithm import Random_Algorithm
from code.algorithms.random_heuristic import Random_Heuristic
from code.algorithms.hillclimber import HillClimber
from code.algorithms.sa import SimulatedAnnealing
from code.classes.grid import *
from code.classes.car import *
from code.algorithms.random_grid import *
from code.algorithms.BreadthFirst import RushHourBFS
from code.visualization.initBoard import visualize_board


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
   
    relative_path = os.path.join("code", "gameboards", "Rushhour6x6_1.csv")
    relative_path2 = os.path.join("code", "gameboards", "Rushhour6x6_2.csv")
    relative_path3 = os.path.join("code", "gameboards", "Rushhour6x6_3.csv")
    relative_path4 = os.path.join("code", "gameboards", "Rushhour9x9_4.csv")
    relative_path5 = os.path.join("code", "gameboards", "Rushhour9x9_5.csv")
    relative_path6 = os.path.join("code", "gameboards", "Rushhour9x9_6.csv")
    relative_path7 = os.path.join("code", "gameboards", "Rushhour12x12_7.csv")

    # Construct the path to the gameboard file
    board_file = os.path.normpath(os.path.join(script_dir, relative_path))
    board_file2 = os.path.normpath(os.path.join(script_dir, relative_path2))
    board_file3 = os.path.normpath(os.path.join(script_dir, relative_path3))
    board_file4 = os.path.normpath(os.path.join(script_dir, relative_path4))
    board_file5 = os.path.normpath(os.path.join(script_dir, relative_path5))
    board_file6 = os.path.normpath(os.path.join(script_dir, relative_path6))
    board_file7 = os.path.normpath(os.path.join(script_dir, relative_path7))

    # visualize_board(boardposition1, 6)
    boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')
    boardposition2 = pd.read_csv(board_file2, sep=',', encoding='utf-8')
    boardposition3 = pd.read_csv(board_file3, sep=',', encoding='utf-8')
    boardposition4 = pd.read_csv(board_file4, sep=',', encoding='utf-8')
    boardposition5 = pd.read_csv(board_file5, sep=',', encoding='utf-8')
    boardposition6 = pd.read_csv(board_file6, sep=',', encoding='utf-8')
    boardposition7 = pd.read_csv(board_file7, sep=',', encoding='utf-8')
    

    Board_size = int(input("Enter which board-size you would like to solve (6x6 = 6, 9x9 = 9, 12x12 = 12): "))
    if Board_size == 12:
        Algo_choice = int(input("Enter which algorithm you would like to choose:(BreadthFirst = 0, DepthFirst = 1, SA = 2, Random = 3, Random + heuristic = 4): "))
    else:
        Board_choice = int(input("Enter which difficulty (1,2 or 3): "))
        Algo_choice = int(input("Enter which algorithm you would like to choose:(BreadthFirst = 0, DepthFirst = 1, SA = 2, Random = 3, Random + heuristic = 4): "))
        
        

    initial_grid = Grid(Board_size)
    initial_grid.create_grid()
    initial_grid.add_borders()
    if Algo_choice == 0 or Algo_choice == 1:
        if Board_size  == 6 and Board_choice == 1:
            initial_grid.add_cars_to_board(boardposition1)
        if Board_size  == 6 and Board_choice == 2:
            initial_grid.add_cars_to_board(boardposition2)
        if Board_size  == 6 and Board_choice == 3:
            initial_grid.add_cars_to_board(boardposition3)
        if Board_size  == 9 and Board_choice == 1:
            initial_grid.add_cars_to_board(boardposition4)
        if Board_size  == 9 and Board_choice == 2:
            initial_grid.add_cars_to_board(boardposition5)
        if Board_size  == 9 and Board_choice == 3:
            initial_grid.add_cars_to_board(boardposition6)
        if Board_size  == 12:
            initial_grid.add_cars_to_board(boardposition7)
        start = time.time()
        Solved_grid = RushHourBFS(initial_grid)
        outputdf = RushHourBFS.run(Solved_grid, Algo_choice)
        # Calculate the end time and time taken
        end = time.time()
        length = end - start
        # Show the results : this can be altered however you like

        print("It took", length, "seconds to find the best solution!")
        print()
        output_file = f"{Board_size},{Board_choice}_output{Algo_choice}.csv"
        outputdf.to_csv(output_file, index=False)
        
        output_csv = os.path.join(script_dir, output_file)
        # Call visualization
    
    # visualize_board(initial_grid, output_csv)


