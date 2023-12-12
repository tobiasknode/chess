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
        self.__erstelle_spieler()
        while True:
            self.schachbrett.anzeigen()
            self.__führe_zug_aus(self.spieler1)
            # Spieler1 und Spieler 2 soll abwechselnd einen Zug ausführen

    def __führe_zug_aus(self, spieler):
        '''
        Führt einen Zug aus, wenn der Zug regelkonform ist.
        '''
        input(f"{spieler.get_name()} gebe einen Zug ein: ")

    def __add_zug(self, start, ziel, schachfigur):
        self.zug_verlauf.append(self.zug(start, ziel, schachfigur))
        pass


if __name__ == "__main__":
    spiel = Spiel()
    spiel.start()
