from Spieler import Spieler
from Schachbrett import Schachbrett
from Spielregeln import Spielregeln
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
                zug_string = input(f"{spieler.get_name()} gebe einen Zug ein (xy xy): ")
                start_pos, ziel_pos = self.__eingabe_regelkonform(zug_string)
                zug = Zug(start_pos, ziel_pos)
                break
            except ValueError:
                print("Oops!  That was no valid Zug.  Try again...")
         
        self.__add_zug(zug.start, zug.ziel, spieler)
        print(spieler.zug_verlauf[-1])

    def __add_zug(self, start, ziel, spieler):
        spieler.zug_verlauf.append(Zug(start, ziel))
        pass

    def __str2Tuple(self, string):
        """
        Konvertiert einen String in ein Tupel.
        """
        return tuple(string.split(" "))
    def __eingabe_regelkonform(self, zug_string):
        """
        Überprüft, ob die Eingabe regelkonform ist.
        """
        char_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        # Überprüfe die Länge des Strings
        if  zug_string is None or len(zug_string) != 5:
            raise ValueError("Ungültige Eingabe")
        
        # Parse tuple
        zug_tupel = self.__str2Tuple(zug_string)
        start_tuple = zug_tupel[0][0], int(zug_tupel[0][1])
        ziel_tuple = zug_tupel[1][0], int(zug_tupel[1][1]) 
        # Überprüfe die einzelnen Elemente des Tuples
        if start_tuple[0] not in char_list or ziel_tuple[0] not in char_list:
            raise ValueError("Ungültige Eingabe")
        
        if start_tuple[1] not in range(1, 9) or ziel_tuple[1] not in range(1, 9):
            raise ValueError("Ungültige Eingabe")

        return start_tuple, ziel_tuple


if __name__ == "__main__":
    spiel = Spiel()
    spiel.start()
