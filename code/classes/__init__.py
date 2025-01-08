# File die de beweging van de voertuigen bewerkt

# Notes:
    # We moeten nog even kijken naar hoe we de orientatie en positie gaan representeren want dit zal ook uitmaken met de berekening van de nieuwe
    # positie


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
