import random

# Listenelement als "abstrakte" Klasse zu den Knoten bzw. dem Abschluss
class Listenelement(object):
    def __init__(self):
        return

# Jede Platte repräsentiert einen neuen Knoten
class Platte(Listenelement):
    def __init__(self, nachfolger:Listenelement):
        # Nachfolger im Betrieb
        self.nachfolger = nachfolger
        # Die Platten ID
        self.pid = random.randint(1000000,9999999)
        
        # Wenn die Platte defekt ist wird sie aussortiert
        # Während der Montage und dem Lötvorgang hat die Platte eine geringe Chance (3-5%) defekt zu werden
        self.defekt = False
        # Kriterien die den Status der Platte beschreiben.
        # montiert -> geloetet -> qualifiziert (Bei defekter Platte Falsch)
        self.montiert = False
        self.geloetet = False
        self.qualifiziert = False

        self.laenge = 0

    #def __del__(self):
    #    print(f"Platte {self.pid} wurde gelöscht")
    
    # Übersetzt die Zahlen 1-3 in das jeweilige Kriterium
    # Wenn Kriterium nicht existiert, wird False zurückgegeben
    def kriterium_holen(self, kriterium:int):
        if kriterium == 0:
            return not self.montiert
        elif kriterium == 1:
            return self.montiert
        elif kriterium == 2:
            return self.geloetet
        elif kriterium == 3:
            return self.qualifiziert
        return False

    # Prüft, ob diese Platte ein Kriterium besitzt und fügt +1 zur Ausgabe hinzu
    # Darf nicht das höhere Kriterium besitzen
    def zaehle_kriterium(self, kriterium:int):
        if (self.kriterium_holen(kriterium)) and (not self.kriterium_holen(kriterium+1)):
            anzahl = self.nachfolger.zaehle_kriterium(kriterium) + 1
        else:
            anzahl = self.nachfolger.zaehle_kriterium(kriterium)
        return anzahl
    
    # Ändert ein Kriterium bei der ersten Platte, die dieses besitzt
    def tag_aendern(self, kriterium:int, aendern:int):
        if (self.kriterium_holen(kriterium)) and (not self.kriterium_holen(kriterium+1)):
            # Wenn ein Kriterium übereinstimmt, wird es invertiert (True -> False; False -> True)
            if aendern == 1:
                self.montiert = not self.montiert
            elif aendern == 2:
                self.geloetet = not self.geloetet
            elif aendern == 3:
                self.qualifiziert = not self.qualifiziert
        # Wenn das Kriterium nicht gefunden wurde
        # Wird die Methode beim Nachfolger ausgeführt
        else:
            self.nachfolger.tag_aendern(kriterium, aendern)
    
    # Löscht eine Platte aus der Liste nach einem Kriterium
    def tag_loeschen(self, kriterium:int):
        # Sollte das Kriterium vorhanden sein, wird beim Vorgänger dieser Nachfolger als Nachfolger gesetzt
        if (self.kriterium_holen(kriterium)) and (not self.kriterium_holen(kriterium+1)):
            return self.nachfolger
        # Ansonsten behält er sich selber als Nachfolger
        else:
            self.nachfolger = self.nachfolger.tag_loeschen(kriterium)
            return self

    # Löscht eine spezifische Platte nach ihrer Platten ID
    def id_loeschen(self, pid:int):
        if self.pid == pid:
            return self.nachfolger
        else:
            self.nachfolger = self.nachfolger.id_loeschen(pid)
            return self
    
    # Sucht eine Platte nach einem Kriterium
    def tag_suchen(self, kriterium:int):
        # Gibt sich selber, wenn diese dieses Kriterium besitzt
        # und nicht das höhere Kriterium [Danke Frau Kamm :)]
        if (self.kriterium_holen(kriterium)) and (not self.kriterium_holen(kriterium+1)):
            return self
        # Ansonsten wird die Methode beim Nachfolger aufgerufen
        # und das Ergebnis dem Vorgänger gegeben
        else:
            ergebnis = self.nachfolger.tag_suchen(kriterium)
            return ergebnis

    # Sucht eine spezifische Platte nach ihrer Platten-ID
    def id_suchen(self, pid:int):
        if self.pid == pid:
            return self
        else:
            ergebnis = self.nachfolger.id_suchen(pid)
            return ergebnis

# Der Abschluss ist das Ende der Liste an Platten um das rekursive Programm abzuschliessen
class Abschluss(Listenelement):
    def __init__(self):
        return
    
    # Methoden wenn keine Platte mit diesem Kriterium gefunden wurde
    def kriterium_holen(self, kriterium):
        return

    def zaehle_kriterium(self, kriterium):
        return 0
    
    def tag_aendern(self, kriterium, aendern):
        return
    
    def tag_loeschen(self, kriterium):
        return self

    def id_loeschen(self, pid):
        return self
    
    def tag_suchen(self, kriterium):
        return

    def id_suchen(self, pid):
        return

def main():
    return

if __name__ == "__main__":
    main()
