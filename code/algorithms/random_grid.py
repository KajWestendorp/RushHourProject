import random
import copy


def random_next_grid(nextmoves):
    chosen_index = random.randint(1, (len(nextmoves) - 1))
    
    next_grid = nextmoves[chosen_index]
    
    return next_grid, chosen_index
        