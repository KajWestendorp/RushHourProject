import copy
import random

class HillClimber:
    """The HillClimber class implements an optimization algorithm to find
    better solutions by modifying the grid state and keeping improvements.
    """
    def __init__(self, grid):
        if grid.grid_solved():
            raise Exception("HillClimber requires an unsolved grid")
        
        self.grid = copy.deepcopy(grid)
        self.value = self.calculate_value(self.grid)

    def calculate_value(self, grid):
        """
        Calculates the value of the grid based on:
        - Number of spaces between the red car and the exit
        - Number of cars blocking the red car
        """
        red_car = [car for car in grid.cars if car.name == 'X']
        if not red_car:
            raise ValueError("Red car 'X' not found in the grid.")
        red_car = red_car[0]

        distance_to_exit = grid.boardsize - (red_car.col + red_car.length)

        # Count blocking cars
        blocking_cars = 0
        for col in range(red_car.col + red_car.length, grid.boardsize):
            if grid.grid[red_car.row][col] != 0:
                blocking_cars += 1

        # Total cost is distance + number of blocking cars
        return distance_to_exit + blocking_cars

    def mutate_single_car(self, grid):
        """
        Changes the position of a random car by moving it in a random valid direction.
        """
        car_to_move = random.choice(grid.cars)
        direction = random.choice([-1, 1])

        print(f"Trying to move car {car_to_move.name} in direction {'left/up' if direction == -1 else 'right/down'}")

        # Try to move the car in the chosen direction
        if grid.move_car(car_to_move, direction):
            print(f"Move successful for car {car_to_move.name}")
            return True
        
        print(f"Move failed for car {car_to_move.name}")
        return False

    def mutate_grid(self, grid, number_of_cars=1):
        """
        Mutates the grid by moving one or more cars randomly.
        """
        for i in range(number_of_cars):
            if not self.mutate_single_car(grid):
                print("Mutation failed; trying a different car.")

    def check_solution(self, new_grid):
        """
        Checks if the new grid has a better or equal solution. If so, accept it.
        """
        new_value = self.calculate_value(new_grid)
        print(f"Evaluating new grid: New Value = {new_value}, Current Value = {self.value}")

        if new_value <= self.value:
            print("New grid accepted.")
            self.grid = copy.deepcopy(new_grid)
            self.value = new_value
        else:
            print("New grid rejected.")

    def run(self, iterations, verbose=False):
        """
        Runs the HillClimber algorithm for a given number of iterations.
        """
        print("Starting Hill Climber...")
        for iteration in range(iterations):
            # Added some print statements for clarity
            if verbose:
                print(f"\nIteration {iteration + 1}/{iterations}")
                print(f"Current Value: {self.value}")

            # Create a copy of the grid to simulate
            new_grid = copy.deepcopy(self.grid)

            # Apply a random mutation
            self.mutate_grid(new_grid)

            # Accept or reject the new solution
            self.check_solution(new_grid)

            # If the grid is solved, break 
            if self.value == 0:
                print(f"Solution found at iteration {iteration + 1}")
                break

        print("\nFinal Results:")
        print(f"Final Value: {self.value}")
        print(f"Final Grid:\n{self.grid}")
