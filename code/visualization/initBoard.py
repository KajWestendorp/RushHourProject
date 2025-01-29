import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import time

def visualize_board(grid, moves_csv):
    """
    This function creates an animatin of the Rush Hour board state and move sequence by using a step-by-step update.
    Takes the initial grid and an output CSV with move sequences to animate.
    """

    # Load the move sequence
    moves_df = pd.read_csv(moves_csv)

    # Board size from the grid
    board_size = grid.boardsize

    # Assign constant colors to each car by mapping
    car_names = [car.name for car in grid.cars]
    color_map = {car: random.choice(['yellow', 'purple', 'orange', 'blue', 'teal', 'cyan', 'aqua']) for car in car_names}
    
    # Ensure the player's car is always red
    color_map['X'] = 'red'  

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(board_size, board_size))

    def draw_grid():
        """Draws a board grid."""
        ax.clear()
        ax.set_title(f"Rush Hour {board_size}x{board_size} - BFS Animation")
        ax.set_xlim(0, board_size)
        ax.set_ylim(0, board_size)
        ax.set_xticks(range(board_size))
        ax.set_yticks(range(board_size))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_aspect('equal')

        # Draw grid lines
        for x in range(board_size + 1):
            ax.axhline(x, color='black', linewidth=0.5)
            ax.axvline(x, color='black', linewidth=0.5)

    def draw_cars():
        """Places all cars on the board, ensuring correct alignment."""
        for car in grid.cars:
            color = color_map[car.name]

            # Convert from 1-based to 0-based indexing
            if car.orientation == 'H':
                # Adjust horizontal cars by reformatting col and row index
                x = car.col - 1  
                y = board_size - car.row  
                width, height = car.length, 1  
            else:
                # Adjust vertical cars by reofrmatting col and row index
                x = car.col - 1  
                y = board_size - car.row - car.length + 1  
                width, height = 1, car.length  

            # Draw the car
            rect = patches.Rectangle((x, y), width, height, facecolor=color, edgecolor='black', lw=3)
            ax.add_patch(rect)
            ax.text(x + width / 2, y + height / 2, car.name, 
                    color='black', ha='center', va='center', fontsize=10, weight='bold')

    def update_board(car_name, move):
        """Moves the car in the correct direction based on the BFS output."""
        car = next((c for c in grid.cars if c.name == car_name), None)
        if car:
            if car.orientation == 'H':

                # Move entire car horizontally
                car.col += move  
            else:
                # Move entire car vertically
                car.row += move  

    # Clear previous state before moving cars
    for index, row in moves_df.iterrows():
        # debug
        print(f"Move {index}: {row['car']} moves {row['move']} spaces") 
        
        draw_grid()
        draw_cars()

        # Apply move
        update_board(row['car'], row['move'])

        # Pause between each move to visualize each step
        plt.pause(1)

    # Show final frame
    plt.show()
