import copy
import random
import pandas as pd

# https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/hillclimber.py ('inspiratie')

class HillClimber:
    """Hill Climber Algorithm that optimizes a solved board by copying a solved grid, and mutating moves by either
    removing a random move, swapping two moves or changing a random direction.."""
    
    def __init__(self, solved_grid):
        if not solved_grid.grid_solved():
            raise Exception("HillClimber requires a solved grid")
        
        self.grid = copy.deepcopy(solved_grid)
        self.best_moves = []

        # Determine solved path length
        self.best_value = len(solved_grid.car_moves)  

    def calculate_value(self, move_sequence):
        """
        Evaluates a solution based on the number of moves used.
        """
        return len(move_sequence)

    def mutate_moves(self, move_sequence):
        """
        Mutates the move sequence by randomly removing, reordering, or tweaking moves.
        """
        new_moves = copy.deepcopy(move_sequence)

        # Choose a random mutation type
        mutation_type = random.choice(["remove", "swap", "modify"])

        # Remove a random move
        if mutation_type == "remove" and len(new_moves) > 1:
            index = random.randint(0, len(new_moves) - 1)
            del new_moves[index]  

        # Swap two moves
        elif mutation_type == "swap" and len(new_moves) > 1:
            i, j = random.sample(range(len(new_moves)), 2)
            new_moves[i], new_moves[j] = new_moves[j], new_moves[i]  

        # Pick a new random direction and change direction
        elif mutation_type == "modify":
            index = random.randint(0, len(new_moves) - 1)
            car_name, direction = new_moves[index]
            new_direction = random.choice([-1, 1])  
            new_moves[index] = (car_name, new_direction) 
        return new_moves

    def apply_moves(self, move_sequence):
        """
        Applies a sequence of moves to a copy of the solved grid.
        """
        test_grid = copy.deepcopy(self.grid)
        test_grid.create_grid()
        test_grid.add_borders()

        # Convert list of Car objects back to a DataFrame format
        cars_data = [{'car': car.name, 'orientation': car.orientation, 'col': car.col, 'row': car.row, 'length': car.length} for car in self.grid.cars]
        cars_df = pd.DataFrame(cars_data)  

        # Add cars to the test grid
        test_grid.add_cars_to_board(cars_df)

        for car_name, direction in move_sequence:
            car = next(car for car in test_grid.cars if car.name == car_name)
            test_grid.move_car(car, direction)

        return test_grid


    def run(self, iterations=1000, verbose=True):
        """
        Runs the Hill Climber algorithm to iteratively optimize the move sequence.
        """
        current_moves = copy.deepcopy(self.grid.car_moves)

        for iteration in range(iterations):
            new_moves = self.mutate_moves(current_moves)
            new_grid = self.apply_moves(new_moves)

            if new_grid.grid_solved():
                new_value = self.calculate_value(new_moves)

                if new_value < self.best_value:
                    self.best_value = new_value
                    self.best_moves = new_moves

                    # Accept better solution
                    current_moves = new_moves  

                    if verbose:
                        print(f"Iteration {iteration}: Found better solution ({new_value} moves)")

        print(f"\nFinal Optimized Solution: {self.best_value} moves")
        return self.best_moves
