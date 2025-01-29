from code.algorithms.random_algorithm import Random_Algorithm
import copy
import random

class Random_Heuristic(Random_Algorithm):
    """
    Inherits from Random_Algorithm and adds the heuristic that if a move leads to a previously seen board configuration, all previous moves in between are removed.
    """
    def __init__(self, grid):
        super().__init__(grid)

        # Track visited states in order
        self.state_history = [self.hash_grid(self.grid)] 
        
        # Store {state: index}
        self.state_index = {self.hash_grid(self.grid): 0} 

    def hash_grid(self, grid):
        """Creates an identifier for the current board state."""
        # https://www.geeksforgeeks.org/hashing-data-structure/
        return tuple(tuple(str(cell) for cell in row) for row in grid.grid)

    def revert_to_state(self, target_index):
        """
        Reverts the grid back to the board configuration at the target_index.
        """
        # Debug print (turned off for experimental purposes)
        #print(f"Reverting back to state {target_index}")

        # Reset the grid
        self.grid.create_grid()
        self.grid.add_borders()

        # Clear and re-add cars based on original positions and reset car list
        self.grid.cars = copy.deepcopy(self.grid.cars)

        for car in self.grid.cars:
            # Place car in original position
            self.grid.update_car(car)  

        # Replay only valid moves up to `target_index`
        for car_name, direction in self.moves[:target_index]:
            car = next(car for car in self.grid.cars if car.name == car_name)
            self.grid.move_car(car, direction)

        # Correct move history
        self.moves = self.moves[:target_index]
        self.state_history = self.state_history[:target_index]
        self.state_index = {state: i for i, state in enumerate(self.state_history)}


    def random_move(self):
        """Selects a random valid move while avoiding redundant board states."""
        valid_moves = self.get_valid_moves()
        random.shuffle(valid_moves) 

        for car, direction in valid_moves:

            # Test a random move and save  state
            test_grid = copy.deepcopy(self.grid)
            test_grid.move_car(car, direction)
            new_state = self.hash_grid(test_grid)

            # Check if state is already seen before
            if new_state in self.state_index:
                # Debug print (turned off for experimental purposes)
                #print(f"State already seen! Rolling back to index {self.state_index[new_state]}")
                self.revert_to_state(self.state_index[new_state])

            # Store state if move is made
            if super().random_move():
                self.state_history.append(new_state)

                # Store the move index
                self.state_index[new_state] = len(self.moves) - 1  
                return True

        print("No valid moves found.")
        return False
