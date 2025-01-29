class Car():
    """This class represents the car objects on the grid, they have various attributes"""
    def __init__(self, name, orientation, col, row, length):
        self.col = col
        self.row = row
        self.orientation = orientation
        self.name = name
        self.length = length