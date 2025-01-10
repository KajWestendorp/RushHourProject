#Implement script that takes a board starting position and can keep updating it
import pandas as pd
import os
from movement.updatedf import update_positions
from visualization.initBoard import visualize_board


# if __name__ == "__main__":
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     relative_path = os.path.join("..", "gameboards", "Rushhour6x6_1.csv")

#     # Construct the path to the gameboard file
#     board_file = os.path.normpath(os.path.join(script_dir, relative_path))

#     boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

    # print(boardposition1)
    # board = visualize_board(boardposition1)
    # print(board)

    # print("yes")
    # newdf = update_positions(boardposition1, 2, 'X')
    # print(newdf)


