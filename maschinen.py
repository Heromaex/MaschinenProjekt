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
    def kapazitaet_berechnen(self, minimum:int, maximum:int):
        # Setzt bei zu niedriger/hoher gegebener Kap. den Wert zum nötigen Wert
        # und gibt aus, dass dieser Wert geändert wurde
        if self.kapazitaet < minimum:
            print(f"{self.kapazitaet} ist nicht verfügbar, stattdessen wurde sie auf {minimum} gesetzt")
            self.kapazitaet = minimum
            return minimum
        elif self.kapazitaet > maximum:
            print(f"{self.kapazitaet} ist nicht verfügbar, stattdessen wurde sie auf {maximum} gesetzt")
            self.kapazitaet = maximum
            return maximum
        # Ansonsten wird einfach die Berechnung ignoriert
        else:
            return self.kapazitaet
    
    # Berechnet den Preis bei gegebener Kap.
    def preis_berechnen(self, mini:int, maxi:int, minip:int, maxip:int):
        # Formel: (kap. - min. kap.) * (max. preis - min. preis) / (max. kap. - min. kap.) + min. preis
        a = maxip - minip
        b = maxi - mini
        c = a / b
        d = ((self.kapazitaet - mini) * c) + minip
        # Gibt den berechneten Preis zurück
        # Da bei Divisionen float gegeben wird, muss es in int konvertiert werden [ int(1000.0) = 1000 ]
        return int(d)
    
    # Repariert eine defekte Maschine
    def reparieren(self):
        self.defekt = False

# Abstufungen der Maschinen
# Maschine zum montieren der Platte
class Montage(Maschine):
    def __init__(self, m:Maschine):
        # Min. Kap.                         1
        self.minimum = 10
        # Min. Preis
        self.minimum_preis = 5000
        # Max. Kap.                         1
        self.maximum = 15
        # Max. Preis
        self.maximum_preis = 6000
        
        # Kap. der Maschine
        self.kapazitaet = m.kapazitaet_berechnen(self.minimum,self.maximum)
        # Kosten der Maschine
        self.preis = m.preis_berechnen(self.minimum,self.maximum,self.minimum_preis,self.maximum_preis)
        # Art der Maschine (1 = Montage; 2 = Löten; 3 = QS)
        self.art = 1
    
    # Jede Maschine besitzt eine Aktion für eine Platte
    # Ändert die benötigten Kriterien
    def montieren(self, platte:Platte):
        # Chance, dass Platte defekt wird
        if random.randint(0,100) < 3:
            platte.defekt = True
        
        platte.montiert = True
        return platte

# Maschine zum loeten der Platte
class Loeten(Maschine):
    def __init__(self, m:Maschine):
        self.minimum = 20
        self.minimum_preis = 2000
        self.maximum = 30
        self.maximum_preis = 2500
        
        self.kapazitaet = m.kapazitaet_berechnen(self.minimum,self.maximum)
        self.preis = m.preis_berechnen(self.minimum,self.maximum,self.minimum_preis,self.maximum_preis)
        
        self.art = 2
    
    def loeten(self, platte:Platte):
        if random.randint(0,100) < 5:
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
        
        self.kapazitaet = m.kapazitaet_berechnen()
        self.preis = m.preis_berechnen(self.minimum,self.maximum,self.minimum_preis,self.maximum_preis)
        
        self.art = 3
    
    def pruefen(self, platte:Platte):
        if platte.defekt:
            platte.geprueft = False
        return platte

def main():
    #m = Maschine(13)
    #montage = Montage(m)

    #print(f"Preis: {montage.preis}")

    return

if __name__ == "__main__":
    main()
