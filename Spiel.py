from Spieler import Spieler
from Schachbrett import Schachbrett
from Spielregeln import Spielregeln
from Schachfigur import Schachfigur
from Zug import Zug


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
        """
        Führt einen Zug aus, wenn der Zug regelkonform ist.
        """
        zug = None
        while True:
            try:
                zug_string = input(f"|{spieler.get_name()}| gebe einen Zug ein (Start Ziel): ")
                start_pos, ziel_pos = self.__eingabe_regelkonform(zug_string)
                zug = Zug(start_pos, ziel_pos)
                x_start,y_start = self.zug2xycorr(start_pos)
                self.spielregeln.ist_regelkonformer_zug(zug)
                print("X",x_start)
                print("Y",y_start)
                
                self.schachbrett.schachbrett[x_start,y_start].bewegen(zug, self.schachbrett)   
                
                break
            except ValueError:
                print("Ungültige Eingabe.  Try again...")
        print(f"Dein Zug ist {zug.start} zu {zug.ziel}")
        spieler.append_zug_verlauf(zug)
        zugverlauf = spieler.get_zug_verlauf()
        print(f"Zugverlauf von {spieler.name} ist {zugverlauf}")
    def zug2xycorr(self,zug):
        """
        Zug in der Form "b4" wird in (2,4) umgewandelt
        das ASCII-Zeichen wird in eine Zahl umgewandelt und minus 96 gerechnet
        a ist in ASCII 97, b ist 98, c ist 99 usw.
        Dadurch wird aus a=1, b=2, c=3 ... h=8. 
        """
        x = ord(zug[0])-97
        print("x: ",x)
        y = zug[1]
        print("y: ",y)
        return (x,y)

    def __eingabe_regelkonform(self, zug_string):
        """
        Überprüft, ob die Eingabe regelkonform ist.
        """
        char_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

        # Remove whitespaces
        zug_string = zug_string.replace(" ", "")
        # Convert to lowercase
        zug_string = zug_string.lower()
        # Überprüfe die Länge des Strings
        if zug_string is None or len(zug_string) != 4:
            raise ValueError("Ungültige Eingabe")

        # Parse tuple
        zug_tupel = zug_string
        start_tuple = zug_tupel[0], int(zug_tupel[1])
        ziel_tuple = zug_tupel[2], int(zug_tupel[3])
        # Überprüfe die einzelnen Elemente des Tuples
        if start_tuple[0] not in char_list or ziel_tuple[0] not in char_list:
            raise ValueError("Ungültige Eingabe")

        if start_tuple[1] not in range(1, 9) or ziel_tuple[1] not in range(1, 9):
            raise ValueError("Ungültige Eingabe")

        return start_tuple, ziel_tuple


if __name__ == "__main__":
    spiel = Spiel()
    spiel.start()
