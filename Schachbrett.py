from Schachfigur import Schachfigur
from Schachfigur import Name


WHITE = "white"
BLACK = "black"


class Piece:
    
    def __init__(self,color,name):
        self.name = name
        self.position = None
        self.Color = color
    def isValid(self,startpos,endpos,Color,gameboard):
        if endpos in self.availableMoves(startpos[0],startpos[1],gameboard, Color = Color):
            return True
        return False
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        print("TestX: " ,self.name)
        return self.name
    
    def availableMoves(self,x,y,gameboard):
        print("ERROR: no movement for base class")
        
    def AdNauseum(self,x,y,gameboard, Color, intervals):
        """repeats the given interval until another piece is run into. 
        if that piece is not of the same color, that square is added and
         then the list is returned"""
        answers = []
        for xint,yint in intervals:
            xtemp,ytemp = x+xint,y+yint
            while self.isInBounds(xtemp,ytemp):
                #print(str((xtemp,ytemp))+"is in bounds")
                
                target = gameboard.get((xtemp,ytemp),None)
                if target is None: answers.append((xtemp,ytemp))
                elif target.Color != Color: 
                    answers.append((xtemp,ytemp))
                    break
                else:
                    break
                
                xtemp,ytemp = xtemp + xint,ytemp + yint
        return answers
                
    def isInBounds(self,x,y):
        "checks if a position is on the board"
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False
    
    def noConflict(self,gameboard,initialColor,x,y):
        "checks if a single position poses no conflict to the rules of chess"
        if self.isInBounds(x,y) and (((x,y) not in gameboard) or gameboard[(x,y)].Color != initialColor) : return True
        return False

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
#            self.schachbrett[(i,1)] = Pawn(WHITE,uniDict[WHITE][Pawn],1)
#            self.schachbrett[(i,6)] = Pawn(BLACK,uniDict[BLACK][Pawn],-1)
#            self.schachbrett[(i,1)] = Schachfigur("Weiß","Bauer",uniDict[WHITE][Pawn])
#            self.schachbrett[(i,6)] = Schachfigur("Schwarz","Bauer",uniDict[BLACK][Pawn])
            self.schachbrett[(i,1)] = Schachfigur("Weiß","♙")
            self.schachbrett[(i,6)] = Schachfigur("Schwarz","♙")
            
            
#        placers = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        
#        for i in range(0,8):
#            self.schachbrett[(i,0)] = placers[i](WHITE,uniDict[WHITE][placers[i]])
#            self.schachbrett[((7-i),7)] = placers[i](BLACK,uniDict[BLACK][placers[i]])
#        placers.reverse()

        

        

#uniDict = {WHITE : {Bauer : "♙", Turm : "♖", Springer : "♘", Laeufer : "♗", Koenig : "♔", Dame : "♕" }, BLACK : {Bauer : "♟", Turm : "♜", Springer : "♞", Laeufer : "♝", Koenig : "♚", Dame : "♛" }}    
#uniDict = {WHITE : {Pawn : "♙", Rook : "♖", Knight : "♘", Bishop : "♗", King : "♔", Queen : "♕" }, BLACK : {Pawn : "♟", Rook : "♜", Knight : "♞", Bishop : "♝", King : "♚", Queen : "♛" }}
#uniDict = {WHITE : {Pawn : "♙"}, BLACK : {Pawn : "♟"}}    

def main():    # nur ein Test der Klasse
    
    print("Hello Schachbrett")
#    start_position = (1,2)
       
#    bauer = Schachfigur("Weiß", "Bauer", start_position)
  
    
    # Test eines Spielzugs
    
#    print(f"Ausgangsposition: {bauer.position}")
#    bauer.bewegen((1,3))
#    print(f"Neue Position: {bauer.position}")
    
    
    schachbrett = Schachbrett()
    
    schachbrett.anzeigen()
    
    

if __name__=='__main__':

    main()
