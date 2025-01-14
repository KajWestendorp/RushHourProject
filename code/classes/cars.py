import pandas as pd
import os
from car import*

class Cars():
    def __init__(self, boardposition):
        self.boardposition = boardposition


    def add_cars(self):
        self.cars = {}

        for car in self.boardposition:
            name = car['car']
            orientation = car['orientation']
            col = car['col']
            row = car['row']
            length = car['length']

            new_car = Car(name, orientation, col, row, length)
            self.cars[name] = new_car
        print(self.cars)
        return self.cars
    

    def add_cars_to_board(self, grid):

        self.grid = grid

        coords = {}
        for _, car in self.cars.iterrows():
        # Checks the orientation of the car and adjusts the column by 1 to include the space above it and row plus 1 for vertical cars
        # TODO: WIll need to add a check for car length later on to ensure the corret amount is being added to the coords for trucks
            if car['orientation'] == 'V':
                coords[car['car']] = ((car['col'], car['row']), (car['col'] + 1, car['row']))
            else:
                coords[car['car']] = ((car['col'], car['row']), (car['col'], car['row'] + 1))

        for car in coords:
            coordinates = coords[car]
            for row, col in coordinates:
                self.grid[row][col] = (car)

        print(self.cars)
        return self.grid
    
    def move_cars(self):
        
        

        return self.grid

    
"""main """

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join("..", "gameboards", "Rushhour6x6_test.csv")

# Construct the path to the gameboard file
board_file = os.path.normpath(os.path.join(script_dir, relative_path))

boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

print(boardposition1)

test = Cars(boardposition1)
print(Cars.add_cars(test))

