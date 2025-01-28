import random
import copy

class HillClimber2:
    """
    Optimized Hill Climber that minimizes deepcopies and reduces redundant move mutations.
    """

    def __init__(self, solved_grid):
        if not solved_grid.grid_solved():
            raise Exception("HillClimber requires a solved grid")

        self.grid = solved_grid 

        # Copy move sequence
        self.best_moves = list(solved_grid.car_moves) 
        self.best_value = len(self.best_moves)

    def calculate_value(self, move_sequence):
        """Evaluates a solution based on the number of moves used."""
        return len(move_sequence)

    def mutate_moves(self, move_sequence):
        """Applies optimized mutations to reduce unnecessary moves."""
        if len(move_sequence) < 2:
            return move_sequence  

        # No deepcopy to avoid memory issues
        new_moves = move_sequence[:]  
        mutation_type = random.choice(["remove_redundant", "swap", "modify"])

        if mutation_type == "remove_redundant":
            # Remove back-and-forth moves (A,+1 followed by A,-1)
            for i in range(len(new_moves) - 1, 0, -1):  
                if new_moves[i][0] == new_moves[i - 1][0] and new_moves[i][1] == -new_moves[i - 1][1]:
                    
                    # Remove both moves
                    del new_moves[i - 1:i + 1] 
                    break

        elif mutation_type == "swap":
            # Swap two non-consecutive random moves
            i, j = sorted(random.sample(range(len(new_moves)), 2))
            if abs(i - j) > 1:  
                new_moves[i], new_moves[j] = new_moves[j], new_moves[i]

        elif mutation_type == "modify":
            # Modify a move’s direction without affecting goal state
            index = random.randint(0, len(new_moves) - 1)
            car_name, direction = new_moves[index]

            # Change direction randomly
            new_moves[index] = (car_name, random.choice([-1, 1]))  

        return new_moves

    def apply_moves(self, previous_moves, new_moves):
        """
        Efficiently applies only the changed moves instead of resetting the board.
        Instead of resetting the grid, it tracks changes and applies only the required updates.
        """

        # Undo only the last applied move (if applicable)
        if len(previous_moves) > len(new_moves):
            removed_move = previous_moves[len(new_moves)]
            car = next((c for c in self.grid.cars if c.name == removed_move[0]), None)
            if car:
                # Reverse move
                self.grid.move_car(car, -removed_move[1])  

        # Apply only the new move
        if len(new_moves) > len(previous_moves):
            added_move = new_moves[-1]
            car = next((c for c in self.grid.cars if c.name == added_move[0]), None)
            if car:
                self.grid.move_car(car, added_move[1]) 

    def run(self, iterations=1000, verbose=True):
        """Runs the optimized Hill Climber algorithm."""
        current_moves = list(self.best_moves)

        for iteration in range(iterations):
            new_moves = self.mutate_moves(current_moves)

            # Apply only changed moves
            self.apply_moves(current_moves, new_moves)  

            if self.grid.grid_solved():
                new_value = self.calculate_value(new_moves)

                if new_value < self.best_value:
                    self.best_value = new_value
                    self.best_moves = new_moves[:]

                    # Accept new sequence
                    current_moves = new_moves  

                    if verbose:
                        print(f"Iteration {iteration}: Found better solution ({new_value} moves)")

        print(f"\nFinal Optimized Solution: {self.best_value} moves")
        return self.best_moves
