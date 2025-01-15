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
    

def valid_move(cars):
    """
    This function checks whether or not a move is valid.
    It takes a grid and checks if a move is possible by checking the car's coordinates
    """
    # Initialize empty set for saving coordinates
    coordinates = set()

    for car in cars:

        car_position = (car.col, car.row)
        # Invalid move if coordinates already exist in set
        if car_position in coordinates:
            return False

        # Invalid move if car's position outside of grid
        if not (0 < car.col <= 6 and 0 < car.row <= 6):
            return False
        
        # Add car's position to coordinates set
        coordinates.append(car_position)

        return True


def random_move(car, move):
    """
    This function moves a car based on orientation and move.
    Car is an instance of class Car and Move is an integer, indicating the direction (negative for backwards, 
    positive for forwards)
    """
    if car.orientation == 'H':
        car.col += move
    
    else:
        car.row += move

    return car