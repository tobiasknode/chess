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
        

