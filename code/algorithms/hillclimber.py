import copy
import random

#TODO: Inheriten van random_hillclimber ? 

class HillClimber:
    """This Hill Climber Algorithm class implements an optimization algorithm to find
    better solutions by modifying the grid state and keeping improvements.
    """
    def __init__(self, grid):
        if not grid.grid_solved():
            raise Exception("HillClimber requires a solved grid")
        
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

        # Distance to the exit (number of spaces)
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

        if grid.move_car(car_to_move, direction):
            # Log the successful move
            self.moves.append((car_to_move.name, "left/up" if direction == -1 else "right/down"))
            return True
        return False

    def generate_neighbor(self):
        """
        Creates a neighbor grid by applying a random mutation to the current grid.
        """
        new_grid = copy.deepcopy(self.grid)
        if not self.mutate_single_car(new_grid):
            return None  # If the move was invalid, return None
        return new_grid

    def run(self, iterations, verbose=False):
        """
        Runs the Hill Climber algorithm for a given number of iterations.
        """
        print("Starting Hill Climber...")
        for iteration in range(iterations):
            if verbose:
                print(f"\nIteration {iteration + 1}/{iterations}")
                print(f"Current Value: {self.value}")

            # Generate a neighbor grid
            neighbor_grid = self.generate_neighbor()

            if neighbor_grid is None:
                continue 

            # Calculate the value of the neighbor
            neighbor_value = self.calculate_value(neighbor_grid)

            if verbose:
                print(f"Neighbor Value: {neighbor_value}, Current Value: {self.value}")

            # Accept or reject the new solution
            if neighbor_value <= self.value:
                self.grid = neighbor_grid
                self.value = neighbor_value
                if verbose:
                    print("Accepted new grid.")
            else:
                if verbose:
                    print("Rejected new grid.")

        print("\nFinal Results:")
        print(f"Final Value: {self.value}")
        print(f"Final Moves Made: {len(self.moves)}")
