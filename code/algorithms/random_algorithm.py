# This script contains an algorithm that finds random solutions.

import random
import pandas as pd
import classes


def random_car(cars):
    """
    This function selects a random car to move from a dataframe with cars
    """
    random_car = random.choice(cars)

    return random_car

def is_solution(cars):
    """
    This function checks whether or not the board has been solved. 
    It takes a grid and returns True or False
    """
    # Solution is reached if the red car 'X' is in the 6th column
    for car in cars:

        if car.name == 'X' and car.col == 5:
            return True
        
        return False

def valid_move(cars):
    """
    This function checks whether or not a move is valid.
    It takes a grid and checks if a move is possible by checking car's coordinates
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



