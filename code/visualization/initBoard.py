# This script reads in a csv board file and visualizes the board's car positions and orientations

import pandas as pd
import random
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import os

# Get the directory of the current script and defin epath
script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join("..", "gameboards", "Rushhour6x6_1.csv")

# Construct the path to the gameboard file
board_file = os.path.normpath(os.path.join(script_dir, relative_path))

boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

board_size = 6

def visualize_board(boardposition1):
    """
    This function creates a visualization of the boards positions
    https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
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

    # Function to assign colors
    def get_car_color(name, length):

        # Colour player's car red
        if name == 'X': return 'red'

        # Trucks are either yellow or purple, cars have several other colours
        if length == 3: return random.choice(['yellow', 'purple'])
        return random.choice(['orange', 'blue', 'teal', 'cyan', 'aqua'])

    # Draw cars with borders
    for index, car in boardposition1.iterrows():
        color = get_car_color(car['car'], car['length'])

        # Convert to 0-based grid
        x, y = car['col'] - 1, board_size - car['row']  

        width, height = (car['length'], 1) if car['orientation'] == 'H' else (1, car['length'])

        # https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html
        # Add car patch with a thicker border
        rect = patches.Rectangle(
            (x, y - height + 1), width, height,
            facecolor=color, edgecolor='black', lw=3)
        axes.add_patch(rect)

        # Place the car name
        axes.text(x + 0.5, y + 0.5, car['car'], color='black', ha='center', va='center', fontsize=8, weight='bold')
    #adding block = FAlse did not work cuz plots closed immediately
    return figure

# i commented this out ebcause it caused the function in main to run xd
# board = visualize_board(boardposition1)
# print(board)