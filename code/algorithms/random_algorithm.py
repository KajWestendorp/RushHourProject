# This script contains an algorithm that finds random solutions.

import random
import pandas as pd

def move(grid):
    """
    This function randomly moves cars on the board.
    It takes a grid and returns a new grid.
    """



    return grid


def is_solution(boardposition):
    """
    This function checks whether or not the board has been solved. 
    It takes a grid and returns True or False
    """
    # Solution is reached if car is in the 6th column
    for car in boardposition:
        
        if car['car'] == 'X' and car['col'] + 1 ==
            return True
        
        return False


def valid_move(grid):
    """
    This function checks whether or not a move is valid.
    It takes a grid and checks if a move is possible by checking car's coordinates
    """
    # Initialize empty set for saving coordinates
    coordinates = set()


    


    return



