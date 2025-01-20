import copy
import random

from random_algorithm import random_move

class HillClimber:
    """
    The HillClimber class changes a random node in the graph to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, grid, cars):
        if not grid.grid_solved():
            raise Exception("HillClimber requires a complete solution")
        
        self.grid = copy.deepcopy(grid)
        self.cars = cars

        self.value = grid.cost_function()

    def calculate_value(self, grid):
        """Calculates the value of the grid based on:
        - Number of spaces between red car and exit
        - Number of cars between red car and exit

        Moven naar grid.py
        """

    def mutate_single_car(self, new_grid):
        """Changes the position of a random car with a random direciton"""
        car_to_move, direction = random_move(new_grid)

    def mutate_grid(self, new_grid, number_of_cars=1):
        """Changes the value of a number of nodes with a random valid value"""
        for _ in range(number_of_cars):
            self.mutate_single_car(new_grid)

    def check_solution(self, new_grid):
        """Checks and accepts better solutions than the currrent solution"""
        new_value = new_grid.calculate_value()
        old_value = self.calculate_value()

        if new_value <= old_value:
            self.grid = new_grid
            self.value = new_value

    def run(self, iterations, verbose=False, mutate_nodes_number=1):
        """Runs the HillClimber algorithm for a specific amount of iterations"""
        self.iterations = iterations

        for iteration in range(iterations):
            # Trick to only print if variable is set to True
            print(f"Iteration {iteration}/{iterations}, current vallue: {self.value}") if verbose else None

            # Create copy of grid to simulate change
            new_grid = copy.deepcopy(self.grid)

            self.mutate_graph(new_grid, number_of_nodes=mutate_nodes_number)

            # Accept if better
            self.check_solution(new_grid)


