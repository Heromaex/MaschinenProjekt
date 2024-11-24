"""
In dem Fertigungsbetrieb Grund-IT für Leiterplattenbestückung bei Mobiltelefonen werden unterschiedliche Maschinen zur Produktion benötigt.
Zunächst müssen die Leiterplatten mit den notwendigen elektronischen Bauteilen bestückt werden (Montage), danach müssen die Bauteile mit der Platte verlötet werden (Löten) und anschließend muss die fehlerfreie Funktionsweise überprüft werden.
Für jede Station (Montage, Löten, Qualitätsprüfung) stehen unterschiedliche Maschinen zur Verfügung
Diese müssen wegen der Neugründung des Fertigungsbetriebs erst gekauft werden
Jede Maschine kann dabei mit einer bestimmten Kapazität (Anzahl der Stücke, die pro Zeiteinheit verarbeitet werden können) erstanden werden
Der Fertigungsbetrieb Grund-IT möchte dabei natürlich möglichst wenig Warte- und Lagerungszeit zwischen den einzelnen Stationen erreichen
"""

"""
Abkürzungen:
    Max.: Maximal
    Min.: Minimal
    Kap.: Kapazität
"""

import random

from listenelemente import *

# Oberklasse Maschine
class Maschine(object):
    def __init__(self, kapazitaet:int):
        # Kap. entspricht der Anzahl der Stücke, die pro Zeiteinheit verarbeitet werden können
        self.kapazitaet = kapazitaet
        # Die Art gibt an welche Maschinenart (zb. Montage) diese Maschine repräsentiert
        self.art = None
        # Variable ob Maschine defekt ist. Kann zufällig beim Prozess passieren
        self.defekt = False
    
    # Prüft, ob die gegebene Kap. am Anfang zu klein/groß ist
    # und ändert sie auf die richtigen Werte
    def kapazitaet_berechnen(self, m):
        # Setzt bei zu niedriger/hoher gegebener Kap. den Wert zum nötigen Wert
        # und gibt aus, dass dieser Wert geändert wurde
        if self.kapazitaet < m.minimum:
            print(f"Kapazität {self.kapazitaet} ist nicht verfügbar, stattdessen wurde sie auf {m.minimum} gesetzt")
            self.kapazitaet = m.minimum
        elif self.kapazitaet > m.maximum:
            print(f"Kapazität {self.kapazitaet} ist nicht verfügbar, stattdessen wurde sie auf {m.maximum} gesetzt")
            self.kapazitaet = m.maximum
        # Der gegebene oder gesetzte Wert wird zurückgegeben
        return self.kapazitaet
    
    # Berechnet den Preis bei gegebener Kap.
    def preis_berechnen(self, m):
        # Formel: (kap. - min. kap.) * (max. preis - min. preis) / (max. kap. - min. kap.) + min. preis
        a = m.maximum_preis - m.minimum_preis
        b = m.maximum - m.minimum
        c = a / b
        d = ((m.kapazitaet - m.minimum) * c) + m.minimum_preis
        # Gibt den berechneten Preis zurück
        # Da bei Divisionen float gegeben wird, muss es in int konvertiert werden [ int(1000.0) = 1000 ]
        return int(d)
    
    # Repariert eine defekte Maschine
    def reparieren(self, m):
        m.defekt = False
        return m

# Abstufungen der Maschinen
# Maschine zum montieren der Platte
class Montage(Maschine):
    def __init__(self, m:Maschine):
        # Min. Kap.                         10
        self.minimum = 10
        # Min. Preis
        self.minimum_preis = 5000
        # Max. Kap.                         15
        self.maximum = 15
        # Max. Preis
        self.maximum_preis = 6000
        
        # Kap. der Maschine
        self.kapazitaet = m.kapazitaet_berechnen(self)
        # Kosten der Maschine
        self.preis = m.preis_berechnen(self)
        # Art der Maschine (1 = Montage; 2 = Löten; 3 = QS)
        self.art = 1
        # Attribut ob die Maschine defekt ist
        self.defekt = False
    
    # Jede Maschine besitzt eine Aktion für eine Platte
    # Ändert die benötigten Kriterien
    def montieren(self, platte:Platte):
        # Chance, dass Platte defekt wird
        if random.randint(0,100) < 5:
            platte.defekt = True
        
        # Setzt den Zustand der Montage auf wahr
        platte.montiert = True
        return platte

# Maschine zum loeten der Platte
class Loeten(Maschine):
    def __init__(self, m:Maschine):
        self.minimum = 20
        self.minimum_preis = 2000
        self.maximum = 30
        self.maximum_preis = 2500
        
        self.kapazitaet = m.kapazitaet_berechnen(self)
        self.preis = m.preis_berechnen(self)
        self.defekt = False
        
        self.art = 2
    
    # Setzt den Zustand des Lötens auf wahr
    def loeten(self, platte:Platte):
        if random.randint(0,100) < 7:
            platte.defekt = True
        
        platte.geloetet = True
        return platte

# Maschine die prueft, ob die Platte defekt ist oder nicht
class Qualitaetspruefung(Maschine):
    def __init__(self, m:Maschine):
        self.minimum = 8
        self.minimum_preis = 8000
        self.maximum = 10
        self.maximum_preis = 12000
        
        self.kapazitaet = m.kapazitaet_berechnen(self)
        self.preis = m.preis_berechnen(self)
        self.defekt = False
        
        self.art = 3
    
    # Setzt den Zustand der Qualitätsprüfung auf falsch, wenn die Platte defekt ist
    def pruefen(self, platte:Platte):
        if platte.defekt:
            platte.qualifiziert = False
        return platte

def main():
    #m = Maschine(13)
    #montage = Montage(m)

    #print(f"Preis: {montage.preis}")

    return

if __name__ == "__main__":
    main()
