"""
In dem Fertigungsbetrieb Grund-IT für Leiterplattenbestückung bei Mobiltelefonen werden unterschiedliche Maschinen zur Produktion benötigt.
Zunächst müssen die Leiterplatten mit den notwendigen elektronischen Bauteilen bestückt werden (Montage), danach müssen die Bauteile mit der Platte verlötet werden (Löten) und anschließend muss die fehlerfreie Funktionsweise überprüft werden.
Für jede Station (Montage, Löten, Qualitätsprüfung) stehen unterschiedliche Maschinen zur Verfügung
Diese müssen wegen der Neugründung des Fertigungsbetriebs erst gekauft werden
Jede Maschine kann dabei mit einer bestimmten Kapazität (Anzahl der Stücke, die pro Zeiteinheit verarbeitet werden können) erstanden werden
Der Fertigungsbetrieb Grund-IT möchte dabei natürlich möglichst wenig Warte- und Lagerungszeit zwischen den einzelnen Stationen erreichen
"""

# Oberklasse Maschine
class Maschine(object):
    def __init__(self, kapazitaet:int):
        # Kapazitaet entspricht der Anzahl der Stücke, die pro Zeiteinheit verarbeitet werden können
        self.kapazitaet = kapazitaet

    def kapazitaet_berechnen(self, minimum:int, maximum:int):
        if self.kapazitaet < minimum:
            print(f"{self.kapazitaet} ist nicht verfügbar, stattdessen wurde sie auf {minimum} gesetzt")
            self.kapazitaet = minimum
            return minimum
        elif self.kapazitaet > maximum:
            print(f"{self.kapazitaet} ist nicht verfügbar, stattdessen wurde sie auf {maximum} gesetzt")
            self.kapazitaet = maximum
            return maximum
        else:
            return self.kapazitaet

    def preis_berechnen(self, mini:int, maxi:int, minip:int, maxip:int):
        a = maxip - minip
        b = maxi - mini
        c = a / b
        d = ((self.kapazitaet - mini) * c) + minip
        return int(d)
        

# Abstufungen der Maschinen
class Montage(Maschine):
    def __init__(self, m:Maschine):
        self.minimum = 10
        self.minimum_preis = 5000
        self.maximum = 15
        self.maximum_preis = 6000
        self.kapazitaet = m.kapazitaet_berechnen(self.minimum,self.maximum)
        self.preis = m.preis_berechnen(self.minimum,self.maximum,self.minimum_preis,self.maximum_preis)

class Loeten(Maschine):
    def __init__(self, m:Maschine):
        self.minimum = 20
        self.minimum_preis = 2000
        self.maximum = 30
        self.maximum_preis = 2500
        self.kapazitaet = m.kapazitaet_berechnen()
        self.preis = m.preis_berechnen(self.minimum,self.maximum,self.minimum_preis,self.maximum_preis)

class Qualitaetspruefung(Maschine):
    def __init__(self, m:Maschine):
        self.minimum = 8
        self.minimum_preis = 8000
        self.maximum = 10
        self.maximum_preis = 12000
        self.kapazitaet = m.kapazitaet_berechnen()
        self.preis = m.preis_berechnen(self.minimum,self.maximum,self.minimum_preis,self.maximum_preis)

def main():
    #m = Maschine(13)
    #montage = Montage(m)

    #print(f"Preis: {montage.preis}")

    return

if __name__ == "__main__":
    main()
