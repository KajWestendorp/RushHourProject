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
    return car.col == 5

# Random valid move
def valid_board(cars):
    """Check if the current car locations are valid."""
    for car in cars:
        car_positions = [(car.col + i, car.row) if car.orientation == 'H' else (car.col, car.row + i)
                         for i in range(car.length)]
        
        # Check to see if cars are not in the same location
        if len(set(car_positions)) != len(car_positions):
            return False
    return True

def random_move(grid):
    """Make a random move"""
    movable_cars = []
    for car in grid.cars:
        if car.orientation == 'H':
            
            # Check spaces left and right  
            if grid.is_valid_move(car, car.row, car.col + 1):
                movable_cars.append((car, 1))  
            if grid.is_valid_move(car, car.row, car.col - 1):
                movable_cars.append((car, -1))  
        elif car.orientation == 'V':

            # Check spaces above and below
            if grid.is_valid_move(car, car.row + 1, car.col):
                movable_cars.append((car, 1))  
            if grid.is_valid_move(car, car.row - 1, car.col):
                movable_cars.append((car, -1))  
    
    # Make a random move
    if movable_cars:
        car_to_move, direction = random.choice(movable_cars)
        grid.move_car(car_to_move, direction)
        return car_to_move, direction
    return None, None

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

# Helperfunctie om het bord netjes te printen
def print_grid(grid):
    for row in grid.grid:
        print(" ".join(str(cell) for cell in row))
    print("\n")

