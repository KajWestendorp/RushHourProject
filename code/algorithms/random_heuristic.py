from code.algorithms.random_algorithm import Random_Algorithm
import random
import copy

class Random_Heuristic(Random_Algorithm):
    """
    Inherits from Random_Algorithm and adds the heuristic:
    - Avoid repeating previously seen board configurations.
    """
    def __init__(self, grid):
        super().__init__(grid)
        self.previous_states = set()
        self.previous_states.add(self.hash_grid(self.grid))

    def hash_grid(self, grid):
        """Creates a unique identifier for the current board state TODO."""
        return tuple(tuple(row) for row in grid.grid)

    def random_move(self):
        """Selects a random valid move, avoiding repeated board states."""
        valid_moves = self.get_valid_moves()
        

        for car, direction in valid_moves:
            test_grid = copy.deepcopy(self.grid)
            test_grid.move_car(car, direction)
            new_state = self.hash_grid(test_grid)

            if new_state not in self.previous_states:
                self.grid.move_car(car, direction)
                self.moves.append((car.name, "left/up" if direction == -1 else "right/down"))
                self.previous_states.add(new_state)
                return True

        print("No valid moves found.")
        return False