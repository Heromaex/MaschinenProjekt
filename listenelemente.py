import random

class Listenelement(object):
    def __init__(self):
        return

# Jede Platte repräsentiert einen neuen Knoten
class Platte(Listenelement):
    def __init__(self, nachfolger:Listenelement):
        self.nachfolger = nachfolger
        
        self.defekt = False
        if random.randint(0,100) < 10:
            self.defekt = True
            
        self.montiert = False
        self.geloetet = False
        self.qualifiziert = False

# Der Abschluss ist das Ende der Liste an Platten um das rekursive Programm abzuschliessen
class Abschluss(Listenelement):
    def __init__(self):
        return        

def main():
    return

if __name__ == "__main__":
    main()
