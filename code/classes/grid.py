import os
import pandas as pd
from cars import *
import copy

class Grid():
    def __init__(self, boardsize):

        #col and row
        self.boardsize = boardsize
        self.redcargoal = 5
        self.cars = []

    def create_grid(self):
        self.grid = []

        for _ in range(self.boardsize + 2):
            row = []
            for _ in range(self.boardsize + 2):
                row.append(0)
            self.grid.append(row)

        return self.grid


    def add_borders(self):
        for _ in range(self.boardsize + 2):
            self.grid[0][_] = 1
            self.grid[self.boardsize + 1][_] = 1
            self.grid[_][0] = 1
            self.grid[_][self.boardsize + 1] = 1

        return self.grid
    
    def add_cars_to_board(self, cars):
        coords = {}
        for _, car in cars.iterrows():
            self.cars.append(Car(car['car'],car['orientation'],car['col'], car['row'], car['length']))
        # Checks the orientation of the car and adjusts the column by 1 to include the space above it and row plus 1 for vertical cars
        # TODO: WIll need to add a check for car length later on to ensure the corret amount is being added to the coords for trucks
            if car['orientation'] == 'H' and car['length'] == 2:
                coords[car['car']] = ((car['col'], car['row']), (car['col'] + 1, car['row']))
            elif car['orientation'] == 'H' and car['length'] == 3:
                coords[car['car']] = ((car['col'], car['row']), (car['col'] + 1, car['row']), (car['col'] + 2, car['row']))
            elif car['orientation'] == 'V' and car['length'] == 2:
                coords[car['car']] = ((car['col'], car['row']), (car['col'], car['row'] + 1))
            elif car['orientation'] == 'V' and car['length'] == 3:
                coords[car['car']] = ((car['col'], car['row']), (car['col'], car['row'] + 1), (car['col'], car['row'] + 2))

        for car in coords:
            coordinates = coords[car]
            for row, col in coordinates:
                self.grid[col][row] = (car)

        print(coords)
        return self.grid
    
    def get_moves(self):
        possible_moves = []
        current_grid = self.grid

        for car in self.cars:
            if car.orientation == 'H':
                if car.col + car.length < self.boardsize + 2 and current_grid[car.row][car.col + car.length] == 0:
                    new_grid = copy.deepcopy(current_grid)
                    new_grid[car.row][car.col] = 0
                    car.col += 1
                    new_grid[car.row][car.col + car.length - 1] = car.name
                    possible_moves.append(new_grid)


            elif car.orientation == 'V':
                if car.row + car.length < self.boardsize + 2 and current_grid[car.row + car.length][car.col] == 0:
                    new_grid = copy.deepcopy(current_grid)
                    new_grid[car.row][car.col] = 0
                    car.row += 1
                    new_grid[car.row + car.length - 1][car.col] = car.name
                    possible_moves.append(new_grid) 
        
        return possible_moves
    

    

test = Grid(6)
(Grid.create_grid(test))
(Grid.add_borders(test))


# Cars(boardposition1)
# cardf = Cars.add_cars(test)

gridtesting = Grid.add_cars_to_board(test, boardposition1)
next_move = Grid.get_moves(test)

for row in gridtesting:
    #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
    print(" ".join(str(cell) for cell in row))
print()
for move in next_move:
    for row in move:
        print(" ".join(str(cell) for cell in row))
    print()



script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join("..", "gameboards", "Rushhour6x6_test.csv")

# Construct the path to the gameboard file
board_file = os.path.normpath(os.path.join(script_dir, relative_path))

boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

# print(boardposition1)
