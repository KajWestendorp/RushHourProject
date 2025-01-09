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

positie = list(zip(boardposition1.col, boardposition1.row))

print(positie)


class Voertuig():
    def __init__(self, positie, lengte, orientatie):
        self.positie = positie
        self.lengte = lengte
        self.orientatie = orientatie

    def bewegen(self, positie, lengte, orientatie, stapgrootte):
        """" Deze functie zorgt voor de beweging van de voertuig op basis van een gegeven stapgrootte, het zorgt ervoor dat de orientatie en lengte
        van de voertuig worden megenomen in de beweging
    
    Args:
        positie = De huidige positie van de voertuig
        lengte = De lengte van de voertuig
        orientatie = de orientatie van de voertuig
        stap = de grootte van de stap van de voertuig
        
    Returns:
        De nieuwe positie van de voertuig"""

        self.lengte = lengte
        self.orientatie = orientatie

        # Dit wordt een berekening, misschien chill om positie een lijst te maken in een dict zodat we bepalde indexs van de lijst kunnen pakken op basis van orientatie?
        self.positie = positie + stapgrootte
