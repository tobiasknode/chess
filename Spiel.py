from Spieler import Spieler
from Schachbrett import Schachbrett
from Spielregeln import Spielregeln


class Spiel:
    def __init__(self) -> None:
        self.spieler1 = Spieler("", "")  #
        self.spieler2 = Spieler()
        self.schachbrett = Schachbrett()
        self.spielregeln = Spielregeln(self.schachbrett)
       

    def __erstelle_spieler(self):
        self.spieler1.name = input("Spieler Weiß nenne deinen Namen:")
        self.spieler1.farbe = "w"
        self.spieler2.name = input("Spieler Schwarz nenne deinen Namen:")
        self.spieler2.farbe = "s"

    def stop(self):
        pass

    def start(self):
        aktueller_spieler = self.spieler1
        self.__erstelle_spieler()
        while True:
            self.schachbrett.anzeigen()
            self.__führe_zug_aus(aktueller_spieler)
            
            # Nach jeder Runde wird der aktuelle Spieler gewechselt.
            if aktueller_spieler == self.spieler1:
                aktueller_spieler = self.spieler2
            else:
                aktueller_spieler = self.spieler1

    def __führe_zug_aus(self, spieler):
        '''
        Führt einen Zug aus, wenn der Zug regelkonform ist.
        '''
        zug_string=input(f"{spieler.get_name()} gebe einen Zug ein (xy xy): ")
        zug_tupel=self.str2Tuple(zug_string)
        print(zug_tupel)
    def __add_zug(self, start, ziel, schachfigur):
        self.zug_verlauf.append(self.zug(start, ziel, schachfigur))
        pass
    
    def str2Tuple(self, string):
        '''
        Konvertiert einen String in ein Tupel.
        '''
        return tuple(string.split(" "))

if __name__ == "__main__":
    spiel = Spiel()
    spiel.start()
