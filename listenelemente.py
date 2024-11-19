import random

# Listenelement als "abstrakte" Klasse zu den Knoten bzw. dem Abschluss
class Listenelement(object):
    def __init__(self):
        return

# Jede Platte repräsentiert einen neuen Knoten
class Platte(Listenelement):
    def __init__(self, nachfolger:Listenelement):
        self.nachfolger = nachfolger
        
        # Wenn die Platte defekt ist wird sie aussortiert
        # Während der Montage und dem Lötvorgang hat die Platte eine geringe Chance (3-5%) defekt zu werden
        self.defekt = False
        # Kriterien die den Status der Platte beschreiben.
        # montiert -> geloetet -> qualifiziert (Bei defekter Platte Falsch)
        self.montiert = False
        self.geloetet = False
        self.qualifiziert = True
    
    # Übersetzt die Zahlen 1-3 in das jeweilige Kriterium
    def kriterium_holen(self, kriterium:int):
        if kriterium == 1:
            return self.montiert
        elif kriterium == 2:
            return self.geloetet
        elif kriterium == 3:
            return self.qualifiziert
    
    # Ändert ein Kriterium bei der ersten Platte, die dieses besitzt
    def tag_aendern(self, kriterium:int, aendern:int):
        if self.kriterium_holen(kriterium):
            # Wenn ein Kriterium übereinstimmt, wird es invertiert (True -> False; False -> True)
            if kriterium == 1:
                self.montiert = not self.montiert
            elif kriterium == 2:
                self.geloetet = not self.geloetet
            elif kriterium == 3:
                self.qualifiziert = not self.qualifiziert
        # Wenn das Kriterium nicht gefunden wurde
        # Wird die Methode beim Nachfolger ausgeführt
        else:
            self.nachfolger.tag_aendern(kriterium, aendern)
    
    # Löscht eine Platte aus der Liste nach einem Kriterium
    def tag_loeschen(self, kriterium:int):
        # Sollte das Kriterium vorhanden sein, wird beim Vorgänger dieser Nachfolger als Nachfolger gesetzt
        if self.kriterium_holen(kriterium):
            return self.nachfolger
        # Ansonsten behält er sich selber als Nachfolger
        else:
            nachfolger = self.nachfolger.tag_loeschen(kriterium)
            return self
    
    # Sucht eine Platte nach einem Kriterium
    def tag_suchen(self, kriterium:int):
        # Gibt sich selber, wenn diese dieses Kriterium besitzt
        if kriterium_holen(kriterium):
            return self
        # Ansonsten wird die Methode beim Nachfolger aufgerufen
        # und das Ergebnis dem Vorgänger gegeben
        else:
            ergebnis = self.nachfolger.tag_suchen(kriterium)
            return ergebnis

# Der Abschluss ist das Ende der Liste an Platten um das rekursive Programm abzuschliessen
class Abschluss(Listenelement):
    def __init__(self):
        return
    
    # Methoden wenn keine Platte mit diesem Kriterium gefunden wurde
    def kriterium_holen(self, kriterium):
        return
    
    def tag_aendern(self, kriterium, aendern):
        return
    
    def tag_loeschen(self, kriterium):
        return
    
    def tag_suchen(self, kriterium):
        return

def main():
    return

if __name__ == "__main__":
    main()
