from Schachfigur import Schachfigur
from Schachfigur import Bauer
from Schachfigur import Turm
from Schachfigur import Springer
from Schachfigur import Läufer
from Schachfigur import König
from Schachfigur import Dame


class Schachbrett:
    
    def __init__(self):
       
        self.schachbrett = {}

        self.setzen_figuren_schachbrett()   # Die Methode wird direkt ausgeführt 
                    
    def entferne_schachfigur(self):
        pass
    
    def suche_schachfigur(self):
        pass
    
    def anzeigen(self):
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(0,8):
            print("-"*32)
            print(chr(i+97),end="|")
            for j in range(0,8):
                item = self.schachbrett.get((i,j)," ")
#                print("item",item)
                print(str(item)+' |', end = " ")
            print()
        print("-"*32)
        
    def setzen_figuren_schachbrett(self):
        
        symboleW = {Bauer : "♙", Turm : "♖", Springer : "♘", Läufer : "♗", König : "♔", Dame : "♕" }
        symboleS = {Bauer : "♟", Turm : "♜", Springer : "♞", Läufer : "♝", König : "♛", Dame : "♚" }
        figuren = [Turm,Springer,Läufer,Dame,König,Läufer,Springer,Turm]
        for i in range(0,8):

            self.schachbrett[(i,1)] = Bauer("Weiß",symboleW[Bauer],(i,1))
            self.schachbrett[(i,6)] = Bauer("Schwarz",symboleS[Bauer], (i,1))
            

     
        
        for i in range(0,8):
            self.schachbrett[(i,0)] = figuren[i]("Weiß",symboleW[figuren[i]],(i,0))
            self.schachbrett[((7-i),7)] = figuren[i]("Schwarz",symboleS[figuren[i]],((7-i),7))



     



def main():    # nur ein Test der Klasse
    
    print("Hello Schachbrett")

    
    schachbrett = Schachbrett()
    
    schachbrett.anzeigen()
    
    

if __name__=='__main__':

    main()
