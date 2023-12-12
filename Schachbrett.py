from Schachfigur import Schachfigur
#from Schachfigur import Name




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
    
        for i in range(0,8):

            self.schachbrett[(i,1)] = Schachfigur("Weiß","♙")
            self.schachbrett[(i,6)] = Schachfigur("Schwarz","♟")
            
            
        symboleW = ["♖","♘","♗","♕","♔","♗","♘","♖"]
        symboleS = ["♜","♞","♝","♚","♛","♝","♞","♜"]
        
        for i in range(0,8):
            self.schachbrett[(i,0)] = symboleW[i]
            self.schachbrett[((7-i),7)] = symboleS[i]


     



def main():    # nur ein Test der Klasse
    
    print("Hello Schachbrett")

    
    schachbrett = Schachbrett()
    
    schachbrett.anzeigen()
    
    

if __name__=='__main__':

    main()
