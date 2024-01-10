from Zug import Zug
class Spielregeln:
    def __init__(self):
        pass
        

    def ist_regelkonformer_zug(self, spieler, zug, schachbrett):
        startx, starty = zug.get_Start()
        zielx, ziely = zug.get_Ziel()
        if schachbrett.schachfiguren.suche_schachfigur((startx, starty)) is None:
            print("Keine Schachfigur gefunden")
            
            return False
        else:
            if schachbrett.schachfiguren.suche_schachfigur((startx, starty)).farbe != spieler.farbe:
                print("Falsche Farbe")
                
                return False
            if schachbrett.schachfiguren.suche_schachfigur((zielx, ziely)) is not None:
                if schachbrett.schachfiguren.suche_schachfigur((zielx, ziely)).farbe == spieler.farbe:
                    print("Ziel ist besetzt")
                    
                    return False
                
        
        # Suche in Schabrett nach einer Schachfigur
        # Wenn keine Schachfigur gefunden wird, dann ist der Zug ungültig.

        # Überprüfe Farbe der Schachfigur und der des Spielers
        # Wenn die Farben nicht übereinstimmen, dann ist der Zug ungültig.


        
        # Hier würde die Logik implementiert, um zu überprüfen, ob ein Zug regelkonform ist.
        # Dies würde die Überprüfung der Bewegungsregeln für die spezifische Schachfigur beinhalten.
        
        return True

    def ist_schach(self, spieler):
        # Überprüfen, ob der König des Spielers im Schach steht.
        # Dies würde erfordern, alle möglichen Züge der gegnerischen Figuren zu überprüfen.
        pass

    def ist_schachmatt(self, spieler):
        # Überprüfen, ob der Spieler im Schachmatt steht.
        # Dies würde bedeuten, dass der Spieler im Schach steht und keinen legalen Zug hat, um das Schach aufzuheben.
        pass

    def ist_patt(self, spieler):
        # Überprüfen, ob eine Patt-Situation vorliegt.
        # Dies tritt auf, wenn der Spieler am Zug ist, aber keinen legalen Zug hat und nicht im Schach steht.
        pass
    def eingabe_regelkonform(self, spieler, schachbrett, zug_raw):
        """
        Überprüft, ob die Eingabe regelkonform ist.
        """
        char_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

        # Remove whitespaces
        zug_raw = zug_raw.replace(" ", "")
        # Convert to lowercase
        zug_raw = zug_raw.lower()
        # Überprüfe die Länge des Strings
        if zug_raw is None or len(zug_raw) != 4:
            print("Ungültige Eingabe. Try again...")
            return False

        # Parse tuple
       
        if not (zug_raw[0].isalpha() and zug_raw[2].isalpha()):
            print("Kein Buchstabe")
            print("Ungültige Eingabe. Try again...")
            return False
        if not (zug_raw[1].isdigit() and zug_raw[3].isdigit()):
            print("Keine Zahl")
            print("Ungültige Eingabe. Try again...")
            return False
        
        start_tuple = zug_raw[0], int(zug_raw[1])
        ziel_tuple = zug_raw[2], int(zug_raw[3])
        # Überprüfe die einzelnen Elemente des Tuples
        if start_tuple[0] not in char_list or ziel_tuple[0] not in char_list:
            print("Ungültige Eingabe. Try again...")
            return False

        if start_tuple[1] not in range(1, 9) or ziel_tuple[1] not in range(1, 9):
            print("Ungültige Eingabe. Try again...")
            return False
        zug = Zug(start_tuple, ziel_tuple)
        if not self.ist_regelkonformer_zug(spieler, zug, schachbrett):
            print("Ungültige Eingabe. Try again...")
            return False

        return zug
