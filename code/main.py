#Implement script that takes a board starting position and can keep updating it
import pandas as pd
import os
from movement.updatedf import update_positions
from visualization.initBoard import visualize_board


if __name__ == "__main__":
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # relative_path = os.path.join("..", "gameboards", "Rushhour6x6_1.csv")

    # # Construct the path to the gameboard file
    # board_file = os.path.normpath(os.path.join(script_dir, relative_path))

    #for now boardfile hardcoded cuz errors 
    board_file = "C:/Users/Weste/Documents/MinorAI/Algos/RushHourProject/code/gameboards/Rushhour6x6_1.csv"
    
    
    boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

    board = visualize_board(boardposition1)

    newboarddf = update_positions(boardposition1, -1, 'A')

    newboard = visualize_board(newboarddf)


