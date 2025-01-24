import random
import math
import copy
import time
from code.algorithms.hillclimber import HillClimber

class SimulatedAnnealing(HillClimber):
    """
    The SimulatedAnnealing class that changes a random node in the graph to a random valid value.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.
    Most of the functions are similar to those of the HillClimber class, which is why
    we use that as a parent class.
    """
    def __init__(self, grid, temperature=1, cooling_rate=0.99):
        super().__init__(grid)
        self.T0 = temperature 
        self.T = temperature   
        self.cooling_rate = cooling_rate  
        self.iterations = 1000  
        self.best_grid = copy.deepcopy(self.grid)
        self.best_value = self.best_value

    def update_temperature(self):
        """ 
        This function implements a linear cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        self.T -= (self.T0 / (self.iterations // 2))  
        self.T = max(self.T, 0)

    def check_solution(self, new_grid):
        """ Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature."""
        new_value = len(new_grid.car_moves)
        old_value = self.best_value
        delta = new_value - old_value  

        if delta < 0:
            self.grid = new_grid
            self.best_value = new_value
            self.best_grid = copy.deepcopy(new_grid)
        else:
            probability = math.exp(-delta / (self.T + 1))
            if random.random() < probability and probability > 0.05:
                self.grid = new_grid
                self.best_value = new_value 
        
        temp_start_time = time.time()
        self.update_temperature()
        temp_time = time.time() - temp_start_time

        if temp_time > 0.5:
            print(f"Warning: Temperature update took {temp_time:.4f}s!")

    def run(self, iterations=100, verbose=False):
        """ Runs Simulated Annealing for the given number of iterations. """
        self.iterations = iterations
        current_moves = copy.deepcopy(self.grid.car_moves)

        for iteration in range(iterations):
            start_time = time.time()

            mutate_start = time.time()
            new_moves = self.mutate_moves(current_moves)
            mutate_time = time.time() - mutate_start

            apply_start = time.time()
            new_grid = self.apply_moves(new_moves)
            apply_time = time.time() - apply_start

            check_start = time.time()
            if new_grid.grid_solved():
                self.check_solution(new_grid)
            check_time = time.time() - check_start

            iteration_time = time.time() - start_time

            if iteration_time > 1:
                print(f"Warning: Iteration {iteration} took {iteration_time:.4f}s!")

            if iteration % 100 == 0:
                print(f"Iteration {iteration}, Temp: {self.T:.4f}, Best Moves: {self.best_value}")
                print(f"  - Mutate Time: {mutate_time:.4f}s, Apply Time: {apply_time:.4f}s, Check Time: {check_time:.4f}s")

        print(f"\nFinal Optimized Solution: {self.best_value} moves")
        return self.best_grid.car_moves  
