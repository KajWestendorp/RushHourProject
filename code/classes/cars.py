import pandas as pd
import os
from car import*

class Cars():
    def __init__(self, boardposition):
        self.boardposition = boardposition


    def add_cars(self):
        self.cars = {}

        for _, car in boardposition1.iterrows():
            name = car['car']
            orientation = car['orientation']
            col = car['col']
            row = car['row']
            length = car['length']

            new_car = Car(name, orientation, col, row, length)
            self.cars[new_car.name] = new_car.orientation, new_car.col, new_car.row, new_car.length
        return self.cars
    
    def move_cars(self):
        
        

        return self.grid

    
"""main """

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join("..", "gameboards", "Rushhour6x6_test.csv")

# Construct the path to the gameboard file
board_file = os.path.normpath(os.path.join(script_dir, relative_path))

boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

test = Cars(boardposition1)
print(Cars.add_cars(test))



