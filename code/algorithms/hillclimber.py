import copy
import random
import pandas as pd

class HillClimber:
    """
    Hill Climber Algorithm that optimizes a solved board by copying a solved grid and mutating moves
    by either removing a random move, swapping two moves, or changing a random direction.
    """

    def __init__(self, solved_grid):
        if not solved_grid.grid_solved():
            raise Exception("HillClimber requires a solved grid")

        self.grid = copy.deepcopy(solved_grid)
        self.best_moves = copy.deepcopy(solved_grid.car_moves) 
        self.best_value = len(self.best_moves)  

    def calculate_value(self, move_sequence):
        """Evaluates a solution based on the number of moves used."""
        return len(move_sequence)

    def mutate_moves(self, move_sequence):
        """Modifies the move sequence without increasing its length."""
        new_moves = copy.deepcopy(move_sequence)

        if len(new_moves) > 1:
            mutation_type = random.choice(["remove", "swap", "modify"])

            # Remove a random move
            if mutation_type == "remove":
                index = random.randint(0, len(new_moves) - 1)
                del new_moves[index]

            # Swap two moves
            elif mutation_type == "swap":
                i, j = random.sample(range(len(new_moves)), 2)
                new_moves[i], new_moves[j] = new_moves[j], new_moves[i]

            # Pick a new random direction and change direction
            elif mutation_type == "modify":
                index = random.randint(0, len(new_moves) - 1)
                car_name, direction = new_moves[index]
                new_direction = random.choice([-1, 1])
                new_moves[index] = (car_name, new_direction)

        # Ensure the mutated sequence is shorter
        if len(new_moves) >= len(move_sequence):
            return move_sequence
        
        return new_moves  

    def apply_moves(self, move_sequence):
        """Applies a sequence of moves to a copy of the solved grid."""
        test_grid = copy.deepcopy(self.grid)
        test_grid.create_grid()
        test_grid.add_borders()

        # Convert Car objects back to DataFrame format
        cars_data = [{'car': car.name, 'orientation': car.orientation, 'col': car.col, 'row': car.row, 'length': car.length}
                     for car in self.grid.cars]
        cars_df = pd.DataFrame(cars_data)

        # Add cars to the test grid
        test_grid.add_cars_to_board(cars_df)

        # Apply moves sequentially
        for car_name, direction in move_sequence:
            car = next((car for car in test_grid.cars if car.name == car_name), None)
            if car:  # Ensure car exists before moving
                test_grid.move_car(car, direction)
            else:
                print(f"Warning: Car {car_name} not found in grid. Skipping move.")

        return test_grid

    def run(self, iterations=1000, verbose=True):
        """Runs the Hill Climber algorithm to iteratively optimize the move sequence."""
        current_moves = copy.deepcopy(self.best_moves)

        for iteration in range(iterations):

            # Try new move sequence
            new_moves = self.mutate_moves(current_moves)
            new_grid = self.apply_moves(new_moves)

            # Check if a solution is reached
            if new_grid.grid_solved():
                new_value = self.calculate_value(new_moves)

                # Update attributes if value is increased or the same
                if new_value < self.best_value:
                    self.best_value = new_value
                    self.best_moves = new_moves

                    # Update move sequence
                    current_moves = new_moves

                    if verbose:
                        print(f"Iteration {iteration}: Found better solution ({new_value} moves)")

        print(f"\nFinal Optimized Solution: {self.best_value} moves")
        return self.best_moves
