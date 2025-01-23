import copy
import random
import pandas as pd

class Random_Algorithm:
    """
    Basic random algorithm for solving the Rush Hour puzzle.
    It randomly selects a valid move from a list of all possible moves.
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.moves = []

    def is_solution(self):
        """Checks if the red car 'X' has reached the exit."""
        red_car = next((car for car in self.grid.cars if car.name == 'X'), None)
              
        # Rightmost column of the board 
        exit_col = self.grid.boardsize  

        # Rightmost column of the board
        red_car_end_position = red_car.col + red_car.length - 1  
        
        # Check if fully at exit
        return red_car_end_position == exit_col  

    def get_valid_moves(self):
        """Finds all valid moves for each car."""
        valid_moves = []
        for car in self.grid.cars:
            if car.orientation == 'H':
                if self.grid.is_valid_move(car, car.row, car.col + 1):
                    # Move right
                    valid_moves.append((car, 1))  
                if self.grid.is_valid_move(car, car.row, car.col - 1):
                    # Move left
                    valid_moves.append((car, -1))  
            elif car.orientation == 'V':
                if self.grid.is_valid_move(car, car.row + 1, car.col):
                    # Move down
                    valid_moves.append((car, 1))  
                if self.grid.is_valid_move(car, car.row - 1, car.col):
                    # Move up
                    valid_moves.append((car, -1))  
        return valid_moves

    def random_move(self):
        valid_moves = self.get_valid_moves()
        if valid_moves:
            car_to_move, direction = random.choice(valid_moves)
            self.grid.move_car(car_to_move, direction)

            # Store moves correctly
            self.grid.car_moves.append((car_to_move.name, direction))
            self.moves.append((car_to_move.name, direction))

            return True
        return False


    def run(self, iterations=100000, verbose=True):
        """Runs the random algorithm for a given number of iterations."""
        for i in range(iterations):
            if self.is_solution():
                print(f"\nDe puzzel is opgelost in {len(self.moves)} moves!")
                return self.moves
            
            if not self.random_move():
                if verbose:
                    print("Stuck. No more valid moves.")
                break
        
        return self.moves

    def print_grid(self):
        """Prints the current state of the grid."""
        print("\nHuidige bordstatus:")
        for row in self.grid.grid:
            print(" ".join(str(cell) for cell in row))
        print("\n")
