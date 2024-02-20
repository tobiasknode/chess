import Zug as Zg
from enum import Enum


class Symbols(Enum):
    Bauer_S = "♙"
    Turm_S = "♖"
    Springer_S = "♘"
    Läufer_S = "♗"
    König_S = "♔"
    Dame_S = "♕"
    Bauer_W = "♟"
    Turm_W = "♜"
    Springer_W = "♞"
    Läufer_W = "♝"
    König_W = "♚"
    Dame_W = "♛"


class Schachfiguren:
    
    def __init__(self):
        self.__SchachfigurenListe = self.__init_Schachfiguren()

    def __init_Schachfiguren(self):
        SchachfigurenListe = []
        for i in range(1, 9):
            SchachfigurenListe.append(
                Schachfigur("Bauer", i, "Weiß", Symbols.Bauer_W.value, (i, 7))
            )
            SchachfigurenListe.append(
                Schachfigur("Bauer", i, "Schwarz", Symbols.Bauer_S.value, (i, 2))
            )

        pass
        SchachfigurenListe.append(
            Schachfigur("Turm", 1, "Weiß", Symbols.Turm_W.value, (1, 8))
        )
        SchachfigurenListe.append(
            Schachfigur("Turm", 1, "Schwarz", Symbols.Turm_S.value, (1, 1))
        )
        SchachfigurenListe.append(
            Schachfigur("Springer", 1, "Weiß", Symbols.Springer_W.value, (2, 8))
        )
        SchachfigurenListe.append(
            Schachfigur("Springer", 1, "Schwarz", Symbols.Springer_S.value, (2, 1))
        )
        SchachfigurenListe.append(
            Schachfigur("Läufer", 1, "Weiß", Symbols.Läufer_W.value, (3, 8))
        )
        SchachfigurenListe.append(
            Schachfigur("Läufer", 1, "Schwarz", Symbols.Läufer_S.value, (3, 1))
        )
        SchachfigurenListe.append(
            Schachfigur("Dame", 1, "Weiß", Symbols.Dame_W.value, (4, 8))
        )
        SchachfigurenListe.append(
            Schachfigur("Dame", 1, "Schwarz", Symbols.Dame_S.value, (4, 1))
        )
        SchachfigurenListe.append(
            Schachfigur("König", 1, "Weiß", Symbols.König_W.value, (5, 8))
        )
        SchachfigurenListe.append(
            Schachfigur("König", 1, "Schwarz", Symbols.König_S.value, (5, 1))
        )
        SchachfigurenListe.append(
            Schachfigur("Läufer", 2, "Weiß", Symbols.Läufer_W.value, (6, 8))
        )
        SchachfigurenListe.append(
            Schachfigur("Läufer", 2, "Schwarz", Symbols.Läufer_S.value, (6, 1))
        )
        SchachfigurenListe.append(
            Schachfigur("Springer", 2, "Weiß", Symbols.Springer_W.value, (7, 8))
        )
        SchachfigurenListe.append(
            Schachfigur("Springer", 2, "Schwarz", Symbols.Springer_S.value, (7, 1))
        )
        SchachfigurenListe.append(
            Schachfigur("Turm", 2, "Weiß", Symbols.Turm_W.value, (8, 8))
        )
        SchachfigurenListe.append(
            Schachfigur("Turm", 2, "Schwarz", Symbols.Turm_S.value, (8, 1))
        )

       
        return SchachfigurenListe
    def get_SchachfigurenListe(self):
        return self.__SchachfigurenListe
    def suche_schachfigur(self, position): # gibt die Schachfigur an der Position zurück aus der Schachfigurenliste
        for schachfigur in self.__SchachfigurenListe:
            
            if schachfigur.position == position:
                return schachfigur
        return None
    def entferne_schachfigur(self, position):
        for schachfigur in self.__SchachfigurenListe:
            if schachfigur.position == position:
                self.__SchachfigurenListe.remove(schachfigur)
                return schachfigur
        return None

    def set_schachfigur(self, schachfigur):
        self.__SchachfigurenListe.append(schachfigur)



class Figur:
    def __init__(self):
        self.name  # Name der Figur
        self.index
        self.farbe
        self.symbol
        self.position  # touple (x,y) Koordinaten

class Schachfigur(Figur):
    def __init__(self, name, index, farbe, symbol, position):
        self.name = name  # Name der Figur
        self.index = index  # Welche Figur von den zwei
        self.farbe = farbe
        self.symbol = symbol
        self.position = position 
        
"""class Schachfigur:
    def __init__(self, name, index, farbe, symbol, position):
        self.name = name  # Name der Figur
        self.index = index  # Welche Figur von den zwei
        self.farbe = farbe
        self.symbol = symbol
        self.position = position  # touple (x,y) Koordinaten
 """       
    

def main():  # nur ein Test der Klasse
    print("Hello Schachfigur")

    schachfiguren = Schachfiguren()

    print(f"Schachfiguren Liste: {schachfiguren.SchachfigurenListe}")


if __name__ == "__main__":
    main()
