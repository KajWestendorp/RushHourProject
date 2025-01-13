# This script preforms random valid moves until red car reaches the exit

import random
import pandas as pd


def is_valid(coords):
    """
    This functions checks if the move is valid, it checks whether the car will be in a spot where there is already a car by using the coords 
    dictionary

    """

    #create a set to store the seen coordinates into 
    coord_set = set()

    # go through the items in the dictionary and check if it is in the set and if it is not we add it as a tuple 
    # Use a tuple so that we can add it to the set
    for car, coordinates in coords.items():
        for coordinate in coordinates:
            if coordinate in coord_set:
                return False
            row, col = coordinate
            if not (0 <= row <= 6 and 0 <= col <= 6):
                return False
            coord_set.add(coordinate)
    return True


def create_coords(boarddf):
    """
    Function that uses the col, orientation and row to create coordinates column for each car and add it to the df
    
    """

    #initialize the dict
    coords = {}
    
    # https://stackoverflow.com/questions/16031056/how-to-form-tuple-column-from-two-columns-in-pandas
    for _, car in boarddf.iterrows():

        # Checks the orientation of the car and adjusts the column by 1 to include the space above it and row plus 1 for vertical cars

        # TODO: WIll need to add a check for car length later on to ensure the corret amount is being added to the coords for trucks
        if car['orientation'] == 'H':
            coords[car['car']] = ((car['col'], car['row']), (car['col'] + 1, car['row']))
        else:
            coords[car['car']] = ((car['col'], car['row']), (car['col'], car['row'] + 1))
    print(coords)
    return coords

def random_car(boarddf):

    # Takes a random sample from the cars that are available
    return boarddf['car'].sample(1).iloc[0]

def finish_check(boarddf):

    # Checks whether the red car has reached an exit
    if boarddf.loc[boarddf['car'] == 'X', 'col'].iloc[0] == 5:
        return False
    return True


