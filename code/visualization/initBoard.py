# This script reads in a csv board file and visualizes the board's car positions and orientations

import pandas as pd
import matplotlib.pyplot as plt

# Functies uit /code/classes/__init__.py importeren


# Transform car info into pd dataframe
board_file = '/users/pieterwassink/minor/ah/rushhourproject-1/code/gameboards/Rushhour6x6_1.csv'
boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')
print(boardposition1)

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

    # Format grid to fit axes and figure
    axes.set_xlim(0, board_size)
    axes.set_ylim(0, board_size)
    axes.set_yticks(range(board_size))
    axes.set_xticks(range(board_size))

    # Remove tick numbers
    axes.set_xticklabels([])
    axes.set_yticklabels([])
    axes.set_aspect('equal')

    plt.show()

    # Draw Cars
    for _, car in boardposition1.iterrows():
        print(car)

    """
    TODO:
    - auto posities lezen + plotten
    - auto instanties aanmaken door middel van __init__.py functies
    """

board = visualize_board(boardposition1)
print(board)