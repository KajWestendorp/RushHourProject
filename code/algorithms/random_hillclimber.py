import copy
import random

class Random_HillClimber:
    """This random algorithm implements a random algorithm with a couple added heuristics:
    - Hill Climber: Only accept new grids that have equal or better board value
    - Prioritize cars that block the exit
    - Prioritize optimal mutations
    """
    def __init__(self, grid):
        if grid.grid_solved():
            raise Exception("Random HillClimber requires an unsolved grid")
        
        self.grid = copy.deepcopy(grid)
        self.value = self.calculate_value(self.grid)
        self.moves = []

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

    def prioritize_blocking_cars(self, grid):
        red_car = [car for car in grid.cars if car.name == 'X'][0]
        blocking_cars = []
        for col in range(red_car.col + red_car.length, grid.boardsize):
            if grid.grid[red_car.row][col] != 0:
                blocking_cars.append(grid.grid[red_car.row][col])
        return blocking_cars

    def mutate_single_car(self, grid):
        blocking_cars = self.prioritize_blocking_cars(grid)
        car_to_move = None

        # Prioritize blocking cars if they exist
        if blocking_cars:
            car_to_move = random.choice([car for car in grid.cars if car.name in blocking_cars])
        else:
            car_to_move = random.choice(grid.cars)
        
        direction = random.choice([-1, 1])

        print(f"Trying to move car {car_to_move.name} in direction {'left/up' if direction == -1 else 'right/down'}")

        if grid.move_car(car_to_move, direction):
            print(f"Move successful for car {car_to_move.name}")
            self.moves.append(({car_to_move.name}, {"left/up" if direction == -1 else "right/down"}))
            return True
        
        print(f"Move failed for car {car_to_move.name}")
        return False

    def mutate_grid(self, grid, number_of_cars=1):
        for i in range(number_of_cars):
            self.mutate_single_car(grid)

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
        print("Starting Hill Climber...")
        for iteration in range(iterations):
            if verbose:
                print(f"\nIteration {iteration + 1}/{iterations}")
                print(f"Current Value: {self.value}")

            new_grid = copy.deepcopy(self.grid)
            self.mutate_grid(new_grid)
            new_value = self.calculate_value(new_grid)

            if new_value <= self.value:
                self.grid = copy.deepcopy(new_grid)
                self.value = new_value
                if verbose:
                    print(f"Move accepted. New Value: {new_value}")
            else:
                if verbose:
                    print("Move rejected.")

            if self.value == 0:
                print(f"Solution found at iteration {iteration + 1}")
                break

        print("\nFinal Results:")
        print(f"Final Value: {self.value}")
        print(f"Final Grid:\n{self.grid}")
        print(f"Moves Made: {len(self.moves)}")