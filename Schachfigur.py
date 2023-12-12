        
    


class Schachfigur():
    
    def __init__(self, farbe, name):
        self.farbe = farbe                             # weiß oder schwarz
        self.name = name                                 # Bauer, Springer, Turm etc...
#        self.position = position                       # touple (x,y) Koordinaten
        
    def __repr__(self):
        
        return self.name
        
    def bewegen(self, neue_position):
        self.position = neue_position
        print(f"{self.farbe} {self.typ} bewegt sich nach {neue_position}")
        
        
        
                    
        
def main():    # nur ein Test der Klasse
    
    print("Hello Schachfigur")
    
    start_position = (1,2)
    farbe = "Weiß"
    
    bauer = schachfigur(farbe, "Bauer", start_position)
    
    # Test eines Spielzugs
    
    print(f"Ausgangsposition: {bauer.position}")
    bauer.bewegen((1,3))
    print(f"Neue Position: {bauer.position}")
    

if __name__=='__main__':
    main()
