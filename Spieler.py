class Spieler:
    def __init__(self, name=None, farbe=None):
        self.name=name 
        self.farbe=farbe
        self.zug_verlauf = []
    def get_farbe(self):
        return self.farbe   
    def get_name(self):
        return self.name
    def get_zug_verlauf(self):
        return self.zug_verlauf
    def append_zug_verlauf(self, zug):
        self.zug_verlauf.append(zug)
    


#Unit test for Spieler.py
#Path: chess/test_Spieler.py

