class Voertuig():
    def __init__(self, positie, lengte, orientatie, breedte):
        self.positie = positie
        self.lengte = lengte
        self.orientatie = orientatie
        self.breedte = breedte

    def bewegen(self, positie, lengte, orientatie):
        self.positie = positie + 3
