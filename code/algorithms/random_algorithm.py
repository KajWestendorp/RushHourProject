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
        print(f"Checking solution: Red car at col {red_car.col} (Exit at 5)")
        return red_car and red_car.col == 5

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
        """Selects a random valid move from the list and executes it."""
        valid_moves = self.get_valid_moves()
        if valid_moves:
            car_to_move, direction = random.choice(valid_moves)
            print(f"Moving car {car_to_move.name}, {direction}")
            self.grid.move_car(car_to_move, direction)

            # Store move as specified in check50 (future work)
            self.moves.append((car_to_move.name, direction))
            return True
        return False

    def run(self, iterations=100000, verbose=True):
        """Runs the random algorithm for a given number of iterations."""
        for _ in range(iterations):
            # Print grid state before each move
            self.print_grid() 
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
