from Spieler import Spieler
from Schachbrett import Schachbrett
from Spielregeln import Spielregeln
from Schachfigur import Schachfigur
from Zug import Zug
from View import View


class Spiel:
    _instance = None
    def __init__(self) -> None:
        self.spieler1 = Spieler("", "")  #
        self.spieler2 = Spieler()
        self.schachbrett = Schachbrett()
        self.spielregeln = Spielregeln()
        self.View = View()

    def __erstelle_spieler(self):
        self.spieler1.name = input("Spieler Weiß nenne deinen Namen:")
        self.spieler1.farbe = "Weiß"
        self.spieler2.name = input("Spieler Schwarz nenne deinen Namen:")
        self.spieler2.farbe = "Schwarz"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Spiel, cls).__new__(cls)
            # Initialisierung der Instanz kann hier erfolgen
        return cls._instance
    def stop(self):
        pass

    def start(self):
        aktueller_spieler = self.spieler1
        self.__erstelle_spieler()
        while True:
            self.View.show(self.schachbrett)
            self.__führe_zug_aus(aktueller_spieler)

            # Nach jeder Runde wird der aktuelle Spieler gewechselt.
            if aktueller_spieler == self.spieler1:
                aktueller_spieler = self.spieler2
            else:
                aktueller_spieler = self.spieler1

    def __führe_zug_aus(self, spieler):
        """
        Führt einen Zug aus, wenn der Zug regelkonform ist.
        """
        zug = False
        while not zug:
            zug_raw = input(f"|{spieler.get_name()}|, {spieler.get_farbe()}  gebe einen Zug ein (Start Ziel): ")
            zug = self.spielregeln.eingabe_regelkonform(spieler, self.schachbrett, zug_raw)

        
        self.schachbrett.bewegen(zug)
           
        # print(f"Dein Zug ist {zug.start} zu {zug.ziel}")
        spieler.append_zug_verlauf(zug)
        # zugverlauf = spieler.get_zug_verlauf()
        # print(f"Zugverlauf von {spieler.name} ist {zugverlauf}")

    def zug2xycorr(self, zug):
        """
        Zug in der Form "b4" wird in (2,4) umgewandelt
        das ASCII-Zeichen wird in eine Zahl umgewandelt und minus 96 gerechnet
        a ist in ASCII 97, b ist 98, c ist 99 usw.
        Dadurch wird aus a=1, b=2, c=3 ... h=8.
        """
        x = ord(zug[0]) - 97
        print("x: ", x)
        y = zug[1]
        print("y: ", y)
        return (x, y)

    


if __name__ == "__main__":
    spiel = Spiel()
    spiel.start()
