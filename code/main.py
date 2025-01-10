#Implement script that takes a board starting position and can keep updating it
import pandas as pd
import random
import matplotlib.patches as patches
import matplotlib.pyplot as plt
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

    visualize_board(boardposition1)

    newboarddf = update_positions(boardposition1, -1, 'A')

    visualize_board(newboarddf)

    #Made it so that the plots show 2 seconds after eachother making a sort of stop motion
    plt.show(block = False)
    plt.pause(2)
    plt.close()
    plt.show()


