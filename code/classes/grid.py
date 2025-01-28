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
        """This method adds cars to the board and adds them to the list of car objects in the class Grid that we can later use
        
        Args: The grid (self) and the cars (df) from csv file
        
        Returns: The grid object but with a list of car objects added in the correct coords"""

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

        #First loop through the cars
        for car in self.cars:
            coordinates = coords[car.name]

            #Then loop through the cars coordinates and add them to the grid by making that list index the label for that car
            for row, col in coordinates:
                self.grid[col][row] = (car.name)

        return self.grid

    
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
        Moves a car in the specified direction (-1 for backward, 1 for forward).
        """
        # Validate the direction
        if direction not in [-1, 1]:
            return False

        # Determine the new front and back positions based on the car's orientation and direction
        if car.orientation == 'H':

            # If moving right, new_front will be the car's new right-most position
            new_front = car.col + car.length + direction - 1

            # If moving left, new_back will be the car's new left-most position
            new_back = car.col + direction
        else: 

            # If moving down, new_front will be the car's new bottom-most position
            new_front = car.row + car.length + direction - 1

            # If moving up, new_back will be the car's new top-most position
            new_back = car.row + direction

        # Check if the new front and back positions are within the grid boundaries
        if new_front < 1 or new_front >= self.boardsize + 1 or new_back < 1 or new_back >= self.boardsize + 1:
            return False

        # Check if there is a collision in the new position (after the car moves)
        if car.orientation == 'H':
            # For horizontal cars, check all the columns that the car will occupy
            for i in range(car.length):
                if self.grid[car.row][car.col + i + direction] != 0 and self.grid[car.row][car.col + i + direction] != car.name:
                    return False
        else:
            # For vertical cars, check all the rows that the car will occupy
            for i in range(car.length):
                if self.grid[car.row + i + direction][car.col] != 0 and self.grid[car.row + i + direction][car.col] != car.name:
                    return False

        # Now update the grid:
        # Clear the old position of the car
        for i in range(car.length):
            if car.orientation == 'H':
                self.grid[car.row][car.col + i] = 0
            else:
                self.grid[car.row + i][car.col] = 0

        # Update the car's position
        if car.orientation == 'H':
            car.col += direction
        else:
            car.row += direction

        # Place the car in its new position
        for i in range(car.length):
            if car.orientation == 'H':
                self.grid[car.row][car.col + i] = car.name
            else:
                self.grid[car.row + i][car.col] = car.name

        return True

    
    def grid_solved(self):
        """Checks if the red car 'X' has reached the exit."""
        red_car = next((car for car in self.cars if car.name == 'X'), None)

        exit_col = self.boardsize
        red_car_end_position = red_car.col + red_car.length - 1  

        return red_car_end_position == exit_col
        
    def __hash__(self):
        """Returns a hash of the grid based on car positions. Created using deepseek
        """
        car_positions = tuple((car.name, car.row, car.col) for car in sorted(self.cars, key=lambda x: x.name))
        return hash(car_positions)
    
    def __eq__(self, other):
        """Allows for the hashed strings to be compared"""
        if isinstance(other, Grid):
            # Compare the grid strings
            return ''.join(''.join(str(cell) for cell in self.grid)) == ''.join(''.join(str(cell) for cell in other.grid))
        return False
    
    
    def print_grid(self):
        """Prints the current state of the grid."""
        print("\nHuidige bordstatus:")
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print("\n")


    def get_moves(self):
        """Find all possible moves for the current board state and store them in a list.
        
        Args: self (the grid object)
        
        Returns: A list grid objects which are possible moves"""

        #init list
        possible_moves = []

        #loop through the cars in the given "parent" grid
        for car in self.cars:

            # Check for Horizontal movement
            if car.orientation == 'H':

                # Move right
                step = 1
                
                #Border check and collision check
                while car.col + car.length + step - 1 < self.boardsize + 1 and self.grid[car.row][car.col + car.length + step - 1] == 0:

                    #Copy the grid as to not impact the original parent grid
                    new_grid = copy.deepcopy(self)

                    #loop through new grids cars to update the new grid cars and not the parent grids ones
                    for cars in new_grid.cars:
                        if cars.name == car.name:
                            new_car = cars
                            break  
                    
                    #Call the clear and update car helper functions
                    new_grid.clear_car(new_car)
                    new_car.col += step  
                    new_grid.update_car(new_car)

                    #Append the grid object to the list
                    possible_moves.append(new_grid)

                    #Increase the step to allow for more than 1 step mvoement
                    step += 1  

                # Move left and reset the step
                step = 1

                #Same as moving right except tghat step is now -= to move left
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

                #Same as moving right
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

                #Same as moving left
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

