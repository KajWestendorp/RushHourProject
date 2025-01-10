import pandas as pd
import os

# Get the directory of the current script and defin epath
script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join("..", "gameboards", "Rushhour6x6_1.csv")

# Construct the path to the gameboard file
board_file = os.path.normpath(os.path.join(script_dir, relative_path))

boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

def update_positions(boardposition, stepsize, car_index):
    """
    This function updates the given boardposition dataframe to adjust the position of the given car index

    The function returns the updated dataframe
    
    """
    print(car_index)
    #Iterate through the rows of the df
    for _, car in boardposition1.iterrows(): 
        #Checks for the corerct car_index and orientation, then updates the position based on the given stepsize and orientation
        if car['car'] == car_index:
            if boardposition.loc[boardposition['car'] == car_index, 'orientation'].iloc[0] == 'H':
                boardposition.loc[boardposition['car'] == car_index, 'col'] += stepsize
                print("yes1")
            if boardposition.loc[boardposition['car'] == car_index, 'orientation'].iloc[0] == 'V':
                print("yes2")
                boardposition.loc[boardposition['car'] == car_index, 'row'] += stepsize
    return boardposition

    