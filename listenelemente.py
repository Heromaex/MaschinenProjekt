
class Listenelement(object):
    def __init__(self):
        return

# Jede Platte repräsentiert einen neuen Knoten
class Platte(Listenelement):
    def __init__(self, daten:dict, nachfolger:Listenelement):
        self.nachfolger = nachfolger
        self.montiert = False
        self.geloetet = False
        self.qualifiziert = False

# Der Abschluss ist das Ende der Liste an Platten um das rekursive Programm abzuschliessen
class Abschluss(Listenelement):
    def __init__(self):
        return

    def neue_station(self, name:str):
        

def main():
    return

if __name__ == "__main__":
    main()
