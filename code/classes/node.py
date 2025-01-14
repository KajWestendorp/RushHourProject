class Node():
    def __init__(self, uid, coords):

        # id will be the car
        self.id = uid

        # Coords are the current position of the car
        self.coords = coords

        #Neighbours should be the positions surrounding the car that are taken
        self.neighbours = {}

        #value will be the coords where the car is
        self.value = None

    def add_neighbour(self, node):
        # TODO: add the coordinates of the other cars
        self.neighbours[node.id] = node

    def get_positions(self, options):
        """Return all possible coordinates that this car can take based on its position and the car around it. Options should be a list of the
        coords that this car could travel to"""

        available_options = set(options)
        unavailable_options = set()

        for neighbour in self.neighbours.value():
            unavailable_options.add(neighbour.value)

        return list(available_options - unavailable_options)
    
    def is_node_valid(self):
        """
        Returns whether the node is valid. A node is valid when there are no
        neighbours with the same value, and it's value is not None.
        """
        if not self.has_value():
            return False

        #TODO: Fix as this might not work
        for neighbour in self.neighbours.values():
            if neighbour.value == self.value:
                return False
            
        return True
    
    def has_value(self):
        return self.value is not None