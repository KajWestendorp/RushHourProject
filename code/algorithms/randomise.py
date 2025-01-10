# This script preforms random valid moves until red car reaches the exit

import random
import pandas as pd


def is_valid(coords):
    """
    This functions checks if the move is valid, it checks whether the car will be in a spot where there is already a car by using the coords 
    dictionary

    """
    coord_set = set()

    for car, coordinates in coords.items():
        for coordinate in coordinates:
            if coordinate in coord_set:
                return False
            coord_set.add(tuple(coordinate))
    return True


def create_coords(boarddf):
    """
    Function that uses the col, orientation and row to create coordinates column for each car and add it to the df
    
    """
    coords = {}
    
    # https://stackoverflow.com/questions/16031056/how-to-form-tuple-column-from-two-columns-in-pandas
    for _, car in boarddf.iterrows():
        if car['orientation'] == 'H':
            coords[car['car']] = ((car['col'], car['row']), (car['col'] + 1, car['row']))
        else:
            coords[car['car']] = ((car['col'], car['row']), (car['col'], car['row'] + 1))

    return coords

def random_car(boarddf):
    return boarddf['car'].sample(1).iloc[0]


