import Zug as Zg     
    


class Schachfigur():
    
    def __init__(self, farbe, symbol, position):
        self.farbe = farbe                             # weiß oder schwarz
        self.symbol = symbol                              
        self.position = position                       # touple (x,y) Koordinaten
        
    def __repr__(self):
        
        return self.symbol
        
    def bewegen(self, zug):
        neue_position=self.__zug2xycorr(zug.ziel)
        self.position = neue_position
       # print(f"{self.farbe} {self.typ} bewegt sich nach {zug.ziel}")
    def __zug2xycorr(self,zug):
        """
        Zug in der Form "e4" wird in (2,4) umgewandelt
        """
        x = ord(zug[0])-97
        y = int(zug[1])-1
        return (x,y)
class Bauer(Schachfigur):
    
    def __init__(self,farbe,symbol,position):
        self.farbe = farbe
        self.symbol = symbol
        self.position = position
        
       
#        #of course, the smallest piece is the hardest to code. direction should be either 1 or -1, should be -1 if the pawn is traveling "backwards"
#        self.direction = direction
    
   
class Springer(Schachfigur):
    
    def __init__(self,farbe,symbol,position):
        self.farbe = farbe
        self.symbol = symbol
        self.position = position
    
class Läufer(Schachfigur):
    
    def __init__(self,farbe,symbol,position):
        self.farbe = farbe
        self.symbol = symbol
        self.position = position
    
class Turm(Schachfigur):
    
    def __init__(self,farbe,symbol,position):
        self.farbe = farbe
        self.symbol = symbol
        self.position = position
    
class Dame(Schachfigur):
    
    def __init__(self,farbe,symbol,position):
        self.farbe = farbe
        self.symbol = symbol
        self.position = position
    
class König(Schachfigur):
    
    def __init__(self,farbe,symbol,position):
        self.farbe = farbe
        self.symbol = symbol
        self.position = position
    
   

        
        
        
                    
        
def main():    # nur ein Test der Klasse
    
    print("Hello Schachfigur")
    
    start_position = (1,2)
    farbe = "Weiß"
    
    bauer = Schachfigur(farbe, "Bauer", start_position)
    
    # Test eines Spielzugs
    
    print(f"Ausgangsposition: {bauer.position}")
    zug=Zg.Zug(("c",4),("c",5))
    print(f"Zug: {zug}")
    bauer.bewegen(zug)
    print(f"Neue Position: {bauer.position}")
    

if __name__=='__main__':
    main()
