import random
import math
import copy
import time
from code.algorithms.hillclimber2 import HillClimber2  

class SimulatedAnnealing(HillClimber2):
    """
    The SimulatedAnnealing class that changes a random node in the graph to a random valid value.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.
    Most of the functions are similar to those of the HillClimber class, which is why
    we use that as a parent class.
    """

    def __init__(self, grid, temperature=5, cooling_rate=0.95, stop_threshold=200):
        super().__init__(grid)
        self.T0 = temperature  
        self.T = temperature   
        self.cooling_rate = cooling_rate  

        # Added to stop if no improvement is made for X iterations
        self.stop_threshold = stop_threshold  
        self.iterations = 1000  
        self.best_grid = copy.deepcopy(self.grid)
        self.best_value = self.best_value  

        # Track if there is a lack of progress
        self.no_improvement_count = 0  

    def update_temperature(self):
        """This function implements an exponential cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed"""
        self.T *= self.cooling_rate  
        self.T = max(self.T, 0.01) 

    def mutate_moves(self, move_sequence):
        """ Mutates move sequence by reducing redundant moves. """
        if len(move_sequence) < 2:
            return move_sequence  

        new_moves = list(move_sequence)  
        mutation_type = random.choice(["remove_redundant", "aggressive_trim", "swap"])

        if mutation_type == "remove_redundant":
            # Remove back-and-forth moves (A,+1 followed by A,-1)
            for i in range(len(new_moves) - 1):
                if new_moves[i][0] == new_moves[i + 1][0] and new_moves[i][1] == -new_moves[i + 1][1]:
                    # Remove both moves
                    del new_moves[i:i + 2]  
                    return new_moves  

        elif mutation_type == "aggressive_trim":
            # Randomly remove 5-15% of moves
            num_remove = max(1, len(new_moves) // random.randint(7, 15))
            indices = random.sample(range(len(new_moves)), num_remove)
            for i in sorted(indices, reverse=True):
                del new_moves[i]

        elif mutation_type == "swap":
            # Swap two random moves
            if len(new_moves) > 2:
                i, j = random.sample(range(len(new_moves)), 2)
                new_moves[i], new_moves[j] = new_moves[j], new_moves[i]

        return new_moves

    def apply_moves(self, move_sequence):
        """ Resets grid and applies a new move sequence. """
        self.grid.reset_grid()  
        for car_name, direction in move_sequence:
            car = next((car for car in self.grid.cars if car.name == car_name), None)
            if car:
                self.grid.move_car(car, direction)

    def check_solution(self, new_moves):
        """Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature."""
        new_value = len(new_moves)
        old_value = self.best_value
        delta = new_value - old_value  

        if delta < 0:
            self.best_value = new_value
            self.best_moves = new_moves

            # Reset counter
            self.no_improvement_count = 0  
        else:
            probability = math.exp(-delta / (self.T + 1))
            if random.random() < probability:
                self.best_value = new_value
                self.best_moves = new_moves
            else:
                # Track lack of improvement
                self.no_improvement_count += 1 

    def run(self, iterations=1000, verbose=False):
        """ Runs Simulated Annealing for the given number of iterations. """
        self.iterations = iterations
        current_moves = list(self.best_moves)

        for iteration in range(iterations):
            if self.no_improvement_count >= self.stop_threshold:
                print(f"Stopping early: No improvement for {self.stop_threshold} iterations")
                break

            new_moves = self.mutate_moves(current_moves)
            self.apply_moves(new_moves)  

            if self.grid.grid_solved():
                self.check_solution(new_moves)  

            self.update_temperature()  

            if iteration % 100 == 0 or verbose:
                print(f"Iteration {iteration}, Temp: {self.T:.4f}, Best Moves: {self.best_value}")

        print(f"\nFinal Optimized Solution: {self.best_value} moves")
        return self.best_moves
