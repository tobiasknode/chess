class Spieler:
    def __init__(self, name, farbe) -> None:
        self.name=name 
        self.farbe=farbe

    def get_farbe(self):
        return self.farbe   
    def get_name(self):
        return self.name
     

if __name__ == "__main__":
    spieler = Spieler("Hans", "w")
    print(spieler)
    print(spieler.get_farbe())
    