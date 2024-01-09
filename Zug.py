class Zug:
    def __init__(self, start, ziel) -> None:
        '''Start und Ziel sind Tupel
        Beispiel: 
        Start: ("c",2)	
        Ziel: ("c",4)
        '''
        self.start=start 
        self.ziel=ziel

    def __str__(self) -> str:
        return f"Start: {self.start} Ziel: {self.ziel}"
    
    def get_Start(self):
        """
        Zug in der Form "b4" wird in (2,4) umgewandelt
        das ASCII-Zeichen wird in eine Zahl umgewandelt und minus 96 gerechnet
        a ist in ASCII 97, b ist 98, c ist 99 usw.
        Dadurch wird aus a=1, b=2, c=3 ... h=8. 
        """
        x = ord(self.start[0])-96
       
        y = self.start[1]
        
        return (x,y)
    def get_Ziel(self):
        """
        Zug in der Form "b4" wird in (2,4) umgewandelt
        das ASCII-Zeichen wird in eine Zahl umgewandelt und minus 96 gerechnet
        a ist in ASCII 97, b ist 98, c ist 99 usw.
        Dadurch wird aus a=1, b=2, c=3 ... h=8. 
        """
        x = ord(self.ziel[0])-96
       
        y = self.ziel[1]
        
        return (x,y)     

