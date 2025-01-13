#Implement script that takes a board starting position and can keep updating it
import pandas as pd
import random
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from movement.updatedf import update_positions
from visualization.initBoard import visualize_board
from algorithms.randomise import create_coords
from algorithms.randomise import random_car
from algorithms.randomise import is_valid
from algorithms.randomise import finish_check
import os


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join("gameboards", "Rushhour6x6_test.csv")

    # Construct the path to the gameboard file
    board_file = os.path.normpath(os.path.join(script_dir, relative_path))
    
    boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

    visualize_board(boardposition1)



    #Pick a random car to move
    chosen_car = random_car(boardposition1)
    newboarddf = update_positions(boardposition1.copy(), 1, chosen_car)

    # Check if the game is over
    while finish_check(newboarddf):
        valid_move = False

        previousboard = newboarddf.copy()

        while not valid_move:

            chosen_car = random_car(newboarddf)
            newboarddf = update_positions(previousboard, 1, chosen_car)
            if is_valid(create_coords(newboarddf)):
                valid_move = True
            else:
                previousboard = newboarddf.copy()
        visualize_board(newboarddf)
        plt.show(block = False)
        plt.pause(2)

    

    visualize_board(newboarddf)

    print(boardposition1)
    print(newboarddf)

    create_coords(newboarddf)
    print(newboarddf)

    #Made it so that the plots show 2 seconds after eachother making a sort of stop motion
    plt.show(block = False)
    plt.pause(2)
    plt.show()

    


