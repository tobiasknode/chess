from Schachfigur import Schachfiguren

from View import View
from Zug import Zug     # nur zum test der main()

   

class Schachbrett:


    def __init__(self):
       
        
        self.schachfiguren = Schachfiguren()
        

    def entferne_schachfigur(self):
        pass
     
    def bewegen(self, zug):
        x_start, y_start = zug.get_Start()
        x_ziel,y_ziel = zug.get_Ziel()
        print("x_start",x_start)
        print("y_start",y_start)
        schachfigur = self.schachfiguren.suche_schachfigur((x_start, y_start))
        self.schachfiguren.entferne_schachfigur((x_start, y_start))
        schachfigur.position = (x_ziel, y_ziel)
        self.schachfiguren.set_schachfigur(schachfigur)
        
        
        

            
   


     



def main():    # nur ein Test der Klasse
    
    print("Hello Schachbrett")
    
    schachbrett = Schachbrett()
   
    view = View()
    view.show(schachbrett)
    

if __name__=='__main__':

    main()
