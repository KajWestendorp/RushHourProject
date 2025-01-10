# This script preforms random valid moves until red car reaches the exit

import random
import pandas as pd

def random_move(boarddf, stepsize, car_index):
    pass


def is_valid(coords):
    """
    This functions checks if the move is valid, it checks whether the car will be in a spot where there is already a car by using the coords 
    dictionary

    """


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
