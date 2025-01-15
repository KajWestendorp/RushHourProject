#Implement script that takes a board starting position and can keep updating it
import pandas as pd
import random
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from movement.updatedf import update_positions
from visualization.initBoard import visualize_board
from algorithms.randomise import create_coords
from algorithms.randomise import random_car
from algorithms.randomise import is_valid
from algorithms.randomise import finish_check
import os
import copy

from algorithms.random_algorithm import *
from classes.grid import *

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join("gameboards", "Rushhour6x6_1_test.csv")

    # Construct the path to the gameboard file
    board_file = os.path.normpath(os.path.join(script_dir, relative_path))
    
    boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

    visualize_board(boardposition1)

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

    # Initialize a testing grid
    test_grid = Grid(6)
    test_grid.create_grid()
    test_grid.add_borders()

    # Add cars to grid
    test_grid.add_cars_to_board(boardposition1)
    
    