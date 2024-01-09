
class View:
    
    def __init__(self):
        pass

    def show(self, schachbrett):
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(1,9):
            print("-"*32)
            print(chr(i+96),end="|")
            for j in range(1,9):
                
                item = " " if schachbrett.schachfiguren.suche_schachfigur((i, j)) is None else schachbrett.schachfiguren.suche_schachfigur((i, j)).symbol
#                print("item",item)
                print(str(item)+' |', end = " ")
            print()
        print("-"*32)

    