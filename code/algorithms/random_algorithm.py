# This script contains an algorithm that finds random solutions.

import random
import pandas as pd

def random_car(cars):
    """
    This function selects a random car to move from a list of car objects
    """
    random_car = random.choice(cars)

    return random_car

def is_solution(car):
    """
    This function checks whether or not the board has been solved. 
    It takes a grid and returns True or False
    """
    # Solution is reached if the red car 'X' is in the 6th column
    if car.col == 5:
        return True
    return False
    

def valid_board(cars):
    """
    This function checks whether or not a move is valid.
    It takes a grid and checks if a move is possible by checking the car's coordinates
    """
    # Initialize empty set for saving coordinates
    coordinates_set = set()

    for car in cars:
        if car.orientation == 'H':
            car_position1 = (car.col, car.row)
            car_position2 = (car.col +1, car.row)
        
        if car.orientation == 'V':
            car_position1 = (car.col, car.row)
            car_position2 = (car.col, car.row + 1)

        # Add car's position to coordinates set
        coordinates_set.add((car_position1, car_position2))
        
        # Invalid move if coordinates already exist in set
        if (car_position1, car_position2) in coordinates_set:
            return False

        # Invalid move if car's position outside of grid
        if not (0 < car.col <= 6 and 0 < car.row <= 6):
            return False

        return True

def random_move(car, move):
    """
    This function moves a car based on orientation and move.
    Car is an instance of class Car and Move is an integer representing the amount of spaces, 
    indicating the direction (negative for backwards, 
    positive for forwards)
    """
    if car.orientation == 'H':
        car.col += move
    
    else:
        car.row += move

    return car

def update_position(boardposition, moved_car):
# Iterate through the rows of the df
    for index, car in boardposition.iterrows(): 
        # Checks for the corerct car_index and orientation, then updates the position based on the orientation
        if car['car'] == moved_car.name:
            if boardposition.loc[boardposition['car'] == moved_car.name, 'orientation'].iloc[0] == 'H':
                boardposition.loc[boardposition['car'] == moved_car.name, 'col'] += 1
            if boardposition.loc[boardposition['car'] == moved_car.name, 'orientation'].iloc[0] == 'V':
                boardposition.loc[boardposition['car'] == moved_car.name, 'row'] += 1

    return boardposition
