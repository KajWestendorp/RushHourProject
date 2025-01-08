# This script reads in a csv board file and visualizes the board's car positions and orientations

import pandas as pd
import matplotlib.pyplot as plt

# Functies uit /code/classes/__init__.py importeren


# Transform car info into pd dataframe
board_file = 'Rushhour6x6_1.csv'
boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

board_size = 6

def visualize_board(boardposition1):
    """
    This function creates a visualization of the boards positions
    """
    figure, axes = plt.subplots(figsize=(board_size, board_size))

    # Draw the grid
    for x in range(board_size + 1):
        axes.axhline(x, color='black', linewidth=0.5)
        axes.axvline(x, color='black', linewidth=0.5)

    # Format the board
    axes.set_title(f"Rush Hour {board_size}x{board_size} Board")
    
    # Flip the y-axis to match the board's natural orientation
    axes.invert_yaxis()  

    plt.show()

    """
    TODO:
    - auto posities lezen + plotten
    - auto instanties aanmaken door middel van __init__.py functies
    """

visualize_board(boardposition1)