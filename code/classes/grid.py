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
        self.redcargoal = boardsize - 1
        self.startcars = []
        self.cars = []
        self.car_moves = []

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
        #TODO: Not adding object to list but adding the label
        for car in self.cars:
            coordinates = coords[car.name]

            #Then loop through the cars coordinates and add them to the grid by making that list index the label for that car
            for row, col in coordinates:
                self.grid[col][row] = (car.name)

        return self.grid
    
    #TODO: FIX SO THAT THE CARS for that grid are updated and not the universal cars
    # def get_moves(self):
    #     """This method finds the possible moves 1 step further from the current board position and stores them in a list as well"""
    #     possible_moves = []  
    #     current_grid = copy.deepcopy(self.grid)
    #     # print(self.grid)
    #     # print(self.cars)
    #     new_cars = copy.deepcopy(self.cars)
    #     # print(new_cars)
        
    #     # Go through the cars list and check orientation
    #     for car in new_cars:
    #         if car.orientation == 'H':
    #             # Check if the cars position is within the space of the grid and if the position 1 step away is free
    #             if car.col + car.length < self.boardsize + 1 and current_grid[car.row][car.col + car.length] == 0:
    #                 print("moved forward")
    #                 # Create a new Grid 
    #                 new_grid = copy.deepcopy(self)  
                    
                    
    #                 # Make the old position 0
    #                 new_grid.grid[car.row][car.col] = 0
                    
    #                 # Move the car 1 step forward
    #                 # car.col += 1
                    
    #                 # Assign the car name to the new index in the new grid that was deepcopied
    #                 for i in range(1,car.length + 1):
    #                     new_grid.grid[car.row][car.col + i] = car.name

    #                 # Append the new Grid object to the list
    #                 possible_moves.append(new_grid)

    #                 # # Restore the original position of the car
    #                 car.col -= 1

    #         elif car.orientation == 'V':
    #             if car.row + car.length < self.boardsize + 1 and current_grid[car.row + car.length][car.col] == 0:
    #                 print("moved down")
    #                 # Create a new Grid object
    #                 new_grid = copy.deepcopy(self)  

    #                 # Make the old position 0
    #                 new_grid.grid[car.row][car.col] = 0
                    
    #                 # Move the car 1 step forward
    #                 # car.row += 1

    #                 # Assign the car name to the new index in the new grid
    #                 for i in range(1,car.length + 1):
    #                     new_grid.grid[car.row + i][car.col] = car.name
                    
    #                 # Append the new Grid object to the list
    #                 possible_moves.append(new_grid)
                    

    #                 # Restore the original position of the car
    #                 for i in range(1,car.length + 1):
    #                     new_grid.grid[car.row - i][car.col] = car.name
    #                     print(car.row, car.col)


        
    #     # Repeat the same for moving cars backward (if applicable)
    #     for car in new_cars:
    #         if car.orientation == 'H':
    #             if car.col - car.length < self.boardsize + 1 and current_grid[car.row][car.col - 1] == 0:
    #                 print("moved backward")
    #                 # Create a new Grid object
    #                 new_grid = copy.deepcopy(self)    
                    
    #                 # Make the old position 0
    #                 new_grid.grid[car.row][car.col + 1] = 0
                    
    #                 # # Move the car 1 step backward
    #                 # car.col -= 1
                    
    #                 # Assign the car name to the new index in the new grid
    #                 for i in range(1,car.length + 1):
    #                     new_grid.grid[car.row][car.col - i] = car.name
                    
    #                 # Append the new Grid object to the list
    #                 possible_moves.append(new_grid)

    #                 # Restore the original position of the car
    #                 car.col += 1
            
    #         elif car.orientation == 'V':
    #             if car.row - car.length < self.boardsize + 2 and current_grid[car.row - 1][car.col] == 0:
    #                 print(f"{car.name}")
    #                 print(f"{car.row}")
                    
    #                 new_grid = copy.deepcopy(self) 
                    
                    
    #                 new_grid.grid[car.row + 1][car.col] = 0
                    
                    
    #                 # car.row -= 1
                    
                    
    #                 for i in range(1,car.length + 1):
    #                     new_grid.grid[car.row - i][car.col] = car.name
    #                     print("moving")
                    
    #                 print("moved up")
    #                 print(f"{car.name}")
    #                 print(f"{car.row}")
                    
    #                 possible_moves.append(new_grid)
                    
    #                 car.row += 1
    #     return possible_moves

    
    def is_valid_move(self, car, new_row, new_col):
        """
        Checks if a car can move to a new location. The function takes a car object,
        and the new column a nd row the car wants to move to. 
        If the move is valid, the function returns True
        """
        # Controleer of de nieuwe locatie binnen de grenzen van het bord valt
        if not (1 <= new_row <= self.boardsize and 1 <= new_col <= self.boardsize):
            return False

        # Controleer of de nieuwe locatie leeg is
        for i in range(car.length):
            if car.orientation == 'H':
                # Controleer de nieuwe kolommen van de auto
                if self.grid[car.row][new_col + i] not in [0, car.name]:
                    return False
            elif car.orientation == 'V':
                # Controleer de nieuwe rijen van de auto
                if self.grid[new_row + i][car.col] not in [0, car.name]:
                    return False

        return True

    def move_car(self, car, direction):
        """
        Move a car in the specified direction
        """
        # Add move to list
        self.car_moves.append((car.name, direction))
        
        # Delete the car from its current location
        for i in range(car.length):
            if car.orientation == 'H':
                self.grid[car.row][car.col + i] = 0
            elif car.orientation == 'V':
                self.grid[car.row + i][car.col] = 0

        # Update the car's position
        if car.orientation == 'H':
            car.col += direction
        elif car.orientation == 'V':
            car.row += direction

        # Put car in new location
        for i in range(car.length):
            if car.orientation == 'H':
                self.grid[car.row][car.col + i] = car.name
            elif car.orientation == 'V':
                self.grid[car.row + i][car.col] = car.name

    
    def grid_solved(self):
        for car in self.cars:
            if car.name == 'X':
                if car.col == self.redcargoal:
                    return True
        
        return False
    
    def __hash__(self):
        string_grid = ''.join(''.join(str(cell) for cell in row) for row in self.grid)
        return hash(string_grid)
    
    def __eq__(self, other):
        if isinstance(other, Grid):
            # Compare the grid strings
            return ''.join(''.join(str(cell) for cell in self.grid)) == ''.join(''.join(str(cell) for cell in other.grid))
        return False
    
    



# print(boardposition1)

    def get_moves(self):
        """Find all possible moves for the current board state and store them in a list."""
        possible_moves = []

        for car in self.cars:
            # Horizontal movement
            if car.orientation == 'H':
                # Move right
                step = 1
                while car.col + car.length + step - 1 < self.boardsize + 1 and self.grid[car.row][car.col + car.length + step - 1] == 0:
                    new_grid = copy.deepcopy(self)
                    for cars in new_grid.cars:
                        if cars.name == car.name:
                            new_car = cars
                            break  
                    new_grid.clear_car(new_car)
                    new_car.col += step  
                    new_grid.update_car(new_car)
                    possible_moves.append(new_grid)
                    step += 1  

                # Move left
                step = 1
                while 0 <= car.col - step < self.boardsize and self.grid[car.row][car.col - step] == 0:
                    new_grid = copy.deepcopy(self)
                    for cars in new_grid.cars:
                        if cars.name == car.name:
                            new_car = cars
                            break  
                    new_grid.clear_car(new_car)
                    new_car.col -= step  
                    new_grid.update_car(new_car)
                    possible_moves.append(new_grid)
                    step += 1  

            # Vertical movement
            elif car.orientation == 'V':
                # Move down
                step = 1
                while car.row + car.length + step - 1 < self.boardsize + 1 and self.grid[car.row + car.length + step - 1][car.col] == 0:
                    new_grid = copy.deepcopy(self)
                    for cars in new_grid.cars:
                        if cars.name == car.name:
                            new_car = cars
                            break  
                    new_grid.clear_car(new_car)
                    new_car.row += step  
                    new_grid.update_car(new_car)
                    possible_moves.append(new_grid)
                    step += 1  

                # Move up
                step = 1
                while car.row - step < self.boardsize and self.grid[car.row - step][car.col] == 0:
                    new_grid = copy.deepcopy(self)
                    for cars in new_grid.cars:
                        if cars.name == car.name:
                            new_car = cars
                            break  
                    new_grid.clear_car(new_car)
                    new_car.row -= step  
                    new_grid.update_car(new_car)
                    possible_moves.append(new_grid)
                    step += 1  

        return possible_moves


    
    def clear_car(self, car):
        """Clear the car's current position from the grid."""
        for i in range(car.length):
            if car.orientation == 'H':
                self.grid[car.row][car.col + i] = 0
            elif car.orientation == 'V':
                self.grid[car.row + i][car.col] = 0


    def update_car(self, car):
        """Place the car at its new position on the grid."""
        for i in range(car.length):
            if car.orientation == 'H':
                self.grid[car.row][car.col + i] = car.name
            elif car.orientation == 'V':
                self.grid[car.row + i][car.col] = car.name


