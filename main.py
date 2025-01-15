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

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join("code", "gameboards", "Rushhour6x6_test.csv")

    # Construct the path to the gameboard file
    board_file = os.path.normpath(os.path.join(script_dir, relative_path))
    
    boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

    visualize_board(boardposition1, 6)

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
    possible_moves = test_grid.get_moves()

    # Assign cars to list
    test_cars = test_grid.cars
    for car in test_cars:
        print(car.name)
        if car.name == 'X':
            player_car = car

    # Pick a random car to move
    random_step = random.choice([-1, 1])
    total_moves = 0

    new_boardposition = copy.copy(boardposition1)
    print(new_boardposition)
    
    while is_solution(player_car) is False:
        random_car_to_move = random_car(test_cars)
        random_move(random_car_to_move, 1)
        total_moves += 1
        print(f"Move {total_moves}, moving car '{random_car_to_move.name}'")

        #Iterate through the rows of the df
        for index, car in new_boardposition.iterrows(): 
            #Checks for the corerct car_index and orientation, then updates the position based on the given stepsize and orientation
            if car['car'] == random_car_to_move.name:
                if new_boardposition.loc[new_boardposition['car'] == random_car_to_move.name, 'orientation'].iloc[0] == 'H':
                    new_boardposition.loc[new_boardposition['car'] == random_car_to_move.name, 'col'] += 1
                if new_boardposition.loc[new_boardposition['car'] == random_car_to_move.name, 'orientation'].iloc[0] == 'V':
                    new_boardposition.loc[new_boardposition['car'] == random_car_to_move.name, 'row'] += 1

        print(new_boardposition)

        solved_grid = Grid(6)
        solved_grid.create_grid()
        solved_grid.add_borders()

        solved_grid = Grid.add_cars_to_board(solved_grid, new_boardposition)

        for row in solved_grid:
            print(" ".join(str(cell) for cell in row))
        print()


    print(f"Board solved after {total_moves} moves")



    "----TEsting grid --- "

    # test = Grid(6)
    # (Grid.create_grid(test))
    # (Grid.add_borders(test))


    # #Create a test grid
    # gridtesting = Grid.add_cars_to_board(test, boardposition1)

    # #Create next moves list of grids
    # next_move = Grid.get_moves(test)
    # moves_per_car = Grid.get_move_diff(test)
    # print(moves_per_car)



    # #Print loops to visualize them
    # for row in gridtesting:
    #     #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
    #     print(" ".join(str(cell) for cell in row))
    # print()
    # for move in next_move:
    #     for row in move:
    #         print(" ".join(str(cell) for cell in row))
    #     print()

    
