#Implement script that takes a board starting position and can keep updating it
import pandas as pd
import random
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from code.movement.updatedf import update_positions
from code.visualization.initBoard import visualize_board

import os
import copy

from code.algorithms.random_algorithm import *
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

    # Construct the path to the gameboard file
    board_file = os.path.normpath(os.path.join(script_dir, relative_path))
    board_file2 = os.path.normpath(os.path.join(script_dir, relative_path2))
    board_file3 = os.path.normpath(os.path.join(script_dir, relative_path3))
    board_file4 = os.path.normpath(os.path.join(script_dir, relative_path4))
    board_file5 = os.path.normpath(os.path.join(script_dir, relative_path5))

    # visualize_board(boardposition1, 6)
    boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')
    boardposition2 = pd.read_csv(board_file2, sep=',', encoding='utf-8')
    boardposition3 = pd.read_csv(board_file3, sep=',', encoding='utf-8')
    boardposition4 = pd.read_csv(board_file4, sep=',', encoding='utf-8')
    boardposition5 = pd.read_csv(board_file5, sep=',', encoding='utf-8')


    """--------- Old Randomise Algorithm ---------"""
    """
    #Pick a random car to move
    chosen_car = random_car(boardposition1)
    steps = random.choice([-1, 1])
    newboarddf = update_positions(boardposition1.copy(), steps, chosen_car)
    attempts = 0
    # Check if the game is over
    while finish_check(newboarddf):
        steps = random.choice([-1, 1])
        #Set valid move to false to start off
        valid_move = False

        #Copy the board so that I can go back onto it if the move is not valid
        previousboard = copy.copy(newboarddf)
        
        while not valid_move:
            steps = random.choice([-1, 1])
            #Get random car
            chosen_car = random_car(newboarddf)

            #Copy board
            previousboard = copy.copy(newboarddf)

            #Update the newboarddf with new positions
            newboarddf = update_positions(newboarddf, steps, chosen_car)

            #Check to see if these dont collide with other cars and are within boundaries
            if is_valid(create_coords(newboarddf)):

                #If yes then break out the loop
                valid_move = True
            else:
                
                #If not we stay in the loop and the newboarddf goes back to being the previousboard so that the move gets undone
                newboarddf = copy.copy(previousboard)
            attempts += 1
            print(attempts)
        # visualize_board(newboarddf)
        # plt.show(block = False)
        # plt.pause(2)

    visualize_board(newboarddf)
    print(f"done this is how many tries it took {attempts}")
    print(boardposition1)
    print(newboarddf)

    create_coords(newboarddf)
    print(newboarddf)

    # Made it so that the plots show 2 seconds after eachother making a sort of stop motion
    plt.show(block = False)
    plt.pause(2)
    plt.show()
    """
    """--------- New Random_Algorithm ---------"""

    # # Initialize the board
    # boardsize = 6  
    # grid = Grid(boardsize)
    # grid.create_grid()
    # grid.add_borders()

    # # Add cars to board
    # grid.add_cars_to_board(boardposition1)

    # print("Startpositie van het bord:")
    # print_grid(grid)

    # total_moves = 0
    # solved = False

    # while not solved:
    #     if valid_board(grid.cars):
    #         car_to_move, direction = random_move(grid)
    #         if car_to_move:
    #             total_moves += 1
    #             direction_str = "forward" if direction > 0 else "backward"
    #             print(f"Move {total_moves}: Moving car {car_to_move.name} {direction_str}")
    #             print_grid(grid)
    #     else:
    #         print("Invalid board configuration. Exiting.")
    #         break

    #     # Check if board is solved
    #     if grid.grid_solved():
    #         print(f"The board is solved in {total_moves} moves!")
    #         solved = True

#     "----TEsting grid --- "

    # test = Grid(6)
    # (Grid.create_grid(test))
    # (Grid.add_borders(test))


    # #Create a test grid
    # gridtesting = Grid.add_cars_to_board(test, boardposition1)

#     #Create next moves list of grids
#     next_move = Grid.get_moves(test)


#     #Print loops to visualize them
#     for row in gridtesting:
#         #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
#         print(" ".join(str(cell) for cell in row))
#     print()

#     for move in next_move:
#         for row in move:
#             print(" ".join(str(cell) for cell in row))
#         print()


#     chosen_grid, index = random_next_grid(next_move)

#     print(f"The grid that was chosen was grid: {index}")
#     print()

#     for row in chosen_grid:
#         #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
#         print(" ".join(str(cell) for cell in row))
#     print()

#     attempts = 0
#     while Grid.grid_solved(test) and attempts > 20:
#         next_move = Grid.get_moves(test)
#         chosen_grid, index = random_next_grid(next_move)
#         attempts += 1

#         print(f"The grid that was chosen was grid: {index}")
#         print()

#         for row in chosen_grid:
#             #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
#             print(" ".join(str(cell) for cell in row))
#         print()

#         test = chosen_grid
# print(attempts)


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


"""----- Hill Climber Algorithm -----"""

from code.algorithms.random_hillclimber import *

experiment_data_random = []
trials = 1

for i in range(trials):
    print(f"Starting trial {i + 1}/{trials}")
    
    # Initialize the grid 
    grid = Grid(6)
    grid.create_grid()
    grid.add_borders()
    grid.add_cars_to_board(boardposition1)

    # Initialize the Hill Climber
    hill_climber = Random_HillClimber(grid)

    # Run the Hill Climber for a number of iterations
    hill_climber.run(iterations=100_000, verbose=False)

    # Store the number of moves 
    experiment_data_random.append(len(hill_climber.moves))

# Save results 
df_random = pd.DataFrame(experiment_data_random, columns=['move count'])
df_random.to_csv("100trials_random_6x6test.csv", index=False)

# Debugging
print("Experiment klaar. Resultaten opgeslagen in 100trials_random_6x6test.csv")


# """----- BreadthFirstSearch Algorithm -----"""
# initial_grid = Grid(9)
# initial_grid.create_grid()
# initial_grid.add_borders()
# initial_grid.add_cars_to_board(boardposition2)

# #Run algorithm
# import time

# # Calculate the start time
# start = time.time()
# final_grid, outputdf = breadth_first(initial_grid)
# # Calculate the end time and time taken
# end = time.time()
# length = end - start
# # Show the results : this can be altered however you like

# print("It took", length, "seconds to find the best solution!")
# print()

# print(outputdf)
# outputdf.to_csv('output.csv',index=False)

# #nOTES

# # 6x6 Board 1 output = checked :)
# # 6x6 Board 2 output = checked :)
# # 6x6 Board 3 output = checked :)

# # 9x9 board 4 output = 

