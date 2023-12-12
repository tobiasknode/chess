class Zug:
    def __init__(self, start, ziel) -> None:
        self.start=start
        self.ziel=ziel
    def __str__(self) -> str:
        return f"Start: {self.start} Ziel: {self.ziel}"
        

