# File die de beweging van de voertuigen bewerkt

# Notes:
    # We moeten nog even kijken naar hoe we de orientatie en positie gaan representeren want dit zal ook uitmaken met de berekening van de nieuwe
    # positie


#Pandas df uit initBoard importeren als board_df

import pandas as pd
import matplotlib.pyplot as plt


#Temporary second import of file
board_file = 'C:/Users/Weste/Documents/MinorAI/Algos/RushHourProject/code/gameboards/Rushhour6x6_1.csv'
boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

print(boardposition1)

positions = list(zip(boardposition1.col, boardposition1.row))
lengths = list(boardposition1.length)
orientations = list(boardposition1.orientation)

class Vehicle():
    def __init__(self, position, length, orientation):
        self.position = position
        self.length = length
        self.orientation = orientation

#Class for the red car
class RedCar(Vehicle):
    def __init__(self, position, length, orientation):
        super().__init__(self, position, length, orientation)

#Class for the 2 lengths vehicles which we label as cars
class Car(Vehicle):
    def __init__(self, position, length, orientation):
        super().__init__(self, position, length, orientation)

#Class for the 3 length vehicles which we label as trucks
class Truck(Vehicle):
    def __init__(self, position, length, orientation):
        super().__init__(self, position, length, orientation)


class LoadBoard():
    def __init__(self, )




# class UpdateBoard():
#     """Class that updates the positions of the cars"""
#     def __init__(self, position, length, orientation, stepsize):
#         self.stepsize = stepsize
#         self.position = position
#         self.length = length
#         self.orientation = orientation

#     def move(self):
#         stepsize = self.stepsize
#         if self.orientation == 'H':
#             self.position[0] = self.position[0] + stepsize
#         else:
#             self.position[1] = self.position[1] + stepsize