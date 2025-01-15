import os
import pandas as pd
from .car import *
import copy


script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join("..", "gameboards", "Rushhour6x6_test.csv")

# Construct the path to the gameboard file
board_file = os.path.normpath(os.path.join(script_dir, relative_path))

boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')


class Grid():

    """ This class is a current grid which we want to have as the nodes for our graph"""
    def __init__(self, boardsize):

        #Initializing Grid attributes
        self.boardsize = boardsize
        self.redcargoal = 5
        self.startcars = []
        self.cars = []

    def create_grid(self):
        """This method creates a grid full of 0s that is 2 bigger than the boardsize allowing us to add 1s to the edge for detection"""
        
        #Initialize the grid list
        self.grid = []

        # append 0s into the list by creating lists for each row, that way we have each row as a list
        for _ in range(self.boardsize + 2):
            row = []
            for _ in range(self.boardsize + 2):
                row.append(0)
            self.grid.append(row)

        return self.grid


    def add_borders(self):
        """This method adds the border around the inner boardsize grid"""
        for _ in range(self.boardsize + 2):
            self.grid[0][_] = 1
            self.grid[self.boardsize + 1][_] = 1
            self.grid[_][0] = 1
            self.grid[_][self.boardsize + 1] = 1

            #add goal
            self.grid[3][self.boardsize + 1] = 2

        return self.grid
    
    def add_cars_to_board(self, cars):
        """This method adds cars to the board and adds them to the list of car objects in the class Grid that we can later use"""

        #Create a dict to store coordinates in (might not be best way but was how i originally did it so for now keeping it)
        coords = {}

        #loop through the dataframe
        for _, car in cars.iterrows():
            self.startcars.append(Car(car['car'],car['orientation'],car['col'], car['row'], car['length']))
            self.cars.append(Car(car['car'],car['orientation'],car['col'], car['row'], car['length']))

        # Checks the orientation of the car and abjusts the coordinates depending on length of the car to ensure all coords are kept
            if car['orientation'] == 'H' and car['length'] == 2:
                coords[car['car']] = ((car['col'], car['row']), (car['col'] + 1, car['row']))
            elif car['orientation'] == 'H' and car['length'] == 3:
                coords[car['car']] = ((car['col'], car['row']), (car['col'] + 1, car['row']), (car['col'] + 2, car['row']))
            elif car['orientation'] == 'V' and car['length'] == 2:
                coords[car['car']] = ((car['col'], car['row']), (car['col'], car['row'] + 1))
            elif car['orientation'] == 'V' and car['length'] == 3:
                coords[car['car']] = ((car['col'], car['row']), (car['col'], car['row'] + 1), (car['col'], car['row'] + 2))

        # Assign the name of the current car as the value of the list in the grid

        #First loop through the cars
        for car in coords:
            coordinates = coords[car]

            #Then loop through the cars coordinates and add them to the grid by making that list index the label for that car
            for row, col in coordinates:
                self.grid[col][row] = (car)

        return self.grid
    
    def get_moves(self):
        """This method finds the possible moves 1 step further from the current board position and stores them in a list as well"""

        
        #list of possible moves and a initiliazation of the grid because it saves space
        possible_moves = []
        current_grid = self.grid
        # Go through the cars list and check orientation
        for car in self.cars:
            if car.orientation == 'H':
                #Check if the cars position is within the space of the grid and if the position 1 step away is free
                    if car.col + car.length < self.boardsize + 2 and current_grid[car.row][car.col + car.length] == 0:

                        #We create a deepcopy so that we can edit it
                        new_grid = copy.deepcopy(current_grid)

                        #Make the old position 0
                        new_grid[car.row][car.col] = 0

                        #Move 1 step forward
                        car.col += 1

                        #Assign the car name to the new index in the new grid that was deepcopied
                        new_grid[car.row][car.col + car.length - 1] = car.name

                        #Append it to the list of possible moves that were made
                        possible_moves.append(new_grid)

                        car.col -= 1
                    
            elif car.orientation == 'V':
                    if car.row + car.length < self.boardsize + 2 and current_grid[car.row + car.length][car.col] == 0:
                        new_grid = copy.deepcopy(current_grid)
                        new_grid[car.row][car.col] = 0
                        car.row += 1
                        new_grid[car.row + car.length - 1][car.col] = car.name
                        possible_moves.append(new_grid)

                        car.row -= 1
        for car in self.cars:
            if car.orientation == 'H':
                #Check if the cars position is within the space of the grid and if the position 1 step away is free
                    if car.col - car.length < self.boardsize + 2 and current_grid[car.row][car.col - 1] == 0:

                        #We create a deepcopy so that we can edit it
                        new_grid = copy.deepcopy(current_grid)

                        #Make the old position 0
                        new_grid[car.row][car.col + 1] = 0

                        #Move 1 step BACKWARD
                        car.col -= 1

                        #Assign the car name to the new index in the new grid that was deepcopied
                        new_grid[car.row][car.col + car.length - 2] = car.name

                        #Append it to the list of possible moves that were made
                        possible_moves.append(new_grid)

                        car.col += 1
            
            #Same comments as above but in this case its for vetical cars
            elif car.orientation == 'V':
                    if car.row - car.length < self.boardsize + 2 and current_grid[car.row - 1][car.col] == 0:
                        new_grid = copy.deepcopy(current_grid)
                        new_grid[car.row + 1][car.col] = 0
                        car.row -= 1
                        new_grid[car.row + car.length - 2][car.col] = car.name

                        possible_moves.append(new_grid) 

                        #TODO: Fix check for travel completion
                        car.row += 1
        return possible_moves
    


    #TODO: FIX this function to work and record the order of the moves
    # def get_move_diff(self):
    #     moves_per_car = []
    #     index_list = []

    #     for car, startcar in zip(self.cars, self.startcars):
    #         if car.orientation == 'H':
    #             car_move = car.col - startcar.col
    #         else:
    #             car_move = car.row - startcar.row

    #         moves_per_car.append(car_move)
    #         index_list.append(car.name)

    #     output_df = pd.DataFrame(moves_per_car, index= index_list)
    #     return output_df
    
    def grid_solved(self):
        for car in self.cars:
            if car.name == 'X':
                if car.col == self.redcargoal:
                    return True
        
        return False


# print(boardposition1)