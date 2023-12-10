



class spielfigur:
    
    def __init__(self, farbe, typ, position):
        self.farbe = farbe                             # weiß oder schwarz
        self.typ = typ                                 # Bauer, Springer, Turm etc...
        self.position = position                       # touple (x,y) Koordinaten
        
    def bewegen(self, neue_position):
        self.position = neue_position
        print(f"{self.farbe} {self.typ} bewegt sich nach {neue_position}")
        
        
        
                
        
        
def main():    # nur ein Test der Klasse
    
    print("Hello Schachfigur")
    
    start_position = (1,2)
    farbe = "Weiß"
    
    bauer = spielfigur(farbe, "Bauer", start_position)
    
    # Test eines Spielzugs
    
    print(f"Ausgangsposition: {bauer.position}")
    bauer.bewegen((1,3))
    print(f"Neue Position: {bauer.position}")
    
    
main()