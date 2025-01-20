import random
import math

from hillclimber import HillClimber

class SimulatedAnnealing(HillClimber):
    """
    The SimulatedAnnealing class that changes a random node in the graph to a random valid value.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.

    Most of the functions are similar to those of the HillClimber class, which is why
    we use that as a parent class.
    """
    def __init__(self):
        pass

    def update_temperature(self):
        """
        This function implements a linear cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        pass

    def check_solution(self):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        pass


 

    