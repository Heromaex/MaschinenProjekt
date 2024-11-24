import time

from listenelemente import *
from maschinen import *
from ui import *

# Der Betrieb stellt die Liste dar, die die Elemente innerhalb initialisiert und bearbeitet
class Betrieb(object):
    def __init__(self, name:str="No name"):
        # Erstellt den Abschluss
        # und setzt ihn als Anfang
        self.anfang = Abschluss()
        # Listen der Maschinen
        # Dies wird benötigt falls Maschinen mit anderen Kapazitäten existieren
        self.montagen = []
        self.loeter = []
        self.pruefer = []
        self.name = name

    # Fügt eine neue Platte am Anfang des Betriebs ein
    def platte_einfuegen(self):
        self.anfang = Platte(self.anfang)

    # Gibt die Länge der Warteschlange
    def laenge_geben(self):
        laenge = self.anfang.laenge_geben()
        return laenge

    # Diese Methode gibt eine Liste mit den Kapazitaeten der jeweiligen Stationen
    # Index 0: Montagemaschinen; 1: Lötmaschinen; 2: Qualitätsprüfmaschinen
    def kapazitaeten_pruefen(self):
        # Variablen die die gesamte Kapazität der Maschinen beinhaltet
        m = 0
        l = 0
        q = 0
        
        # Addiert die Kapazitäten der Maschinen zu den Variablen
        for montage in self.montagen:
            m += montage.kapazitaet
        for loet in self.loeter:
            l += loet.kapazitaet
        for quali in self.pruefer:
            q += quali.kapazitaet

        return m,l,q
    
    # Eine neue Maschine in die Listen einfügen
    # Die Maschine sollte vorher erstellt werden
    def maschine_hinzufuegen(self, maschine:Maschine):
        # Fügt die Maschine in die zugehörige Liste ein
        if maschine.art == 1:
            self.montagen.append(maschine)
        elif maschine.art == 2:
            self.loeter.append(maschine)
        elif maschine.art == 3:
            self.pruefer.append(maschine)
    
    # Sucht eine Platte nach einem Kriterium
    # Diese Platte wird zurückgegeben
    def tag_suchen(self, kriterium:int):
        platte = self.anfang.tag_suchen(kriterium)
        return platte
    
    # Löscht eine Platte nach einem Kriterium aus der Liste
    def tag_loeschen(self, kriterium:int):
        self.anfang = self.anfang.tag_loeschen(kriterium)
    
    # Simuliert den Prozess der Fertigung der Platten
    # plot gibt an ob ein Graph erstellt werden soll
    def platten_durchschieben(self, plattenzahl:int, plot:bool=True):
        # Liste an Gesamt-Kapazitäten der Stationen, zb. [50,80,45]
        kapazitaet = self.kapazitaeten_pruefen()
        # Liste wie die Stationen gefüllt sind
        gefuellt = [0,0,0]
        # Zähler, wie viele Platten abgeschlossen wurden
        abgeschlossen = 0
        # Zähler, wie viele Platten kaputt gegangen sind
        kaputt = 0
        # Zähler, wie viele von welchen Maschinen kaputt sind
        # Dies bestimmt, mit welcher Wahrscheinlichkeit Platten falsch sortiert werden oder zerbrochen werden
        kaputt_m = [0,0,0]
        
        # Maschinen Templates um Funktionen der Stationen zu übertragen
        startm = Maschine(kapazitaet[0])
        m = Montage(startm)
        startl = Maschine(kapazitaet[1])
        l = Loeten(startl)
        startq = Maschine(kapazitaet[2])
        q = Qualitaetspruefung(startq)
        
        # Zeit-Platten-Achsen um Plotten möglich zu machen
        zeitachse = []
        plattenachse_m = []
        plattenachse_l = []
        plattenachse_q = []
        fertigachse = []
        zeit = 0
        
        # Iteriert jede Platte in der Liste um die Daten zu ändern
        while True:
            # Zeit wird beim Plotten gezählt um einen Verlauf darzustellen
            zeit += 1
            zeitachse.append(zeit)
            
            # Überprüft wie viel Maschinen defekt sind
            # Wenn eine Maschine defekt ist, gibt es eine Chance dass die Platten brechen oder als kaputt abgestempelt werden
            # Wenn mehrere Maschinen kaputt sind erhöhen sich die Chancen
            for station_b in [self.montagen, self.loeter, self.pruefer]:
                for i in range(len(station_b)):
                    if station_b[i].defekt:
                        kaputt_m[i] += 1
            
            # Neue Kapazität besteht aus der eigenen und der der vorherigen Maschine
            # Umgedrehte Reihenfolge der Stationen stellt sicher, dass Platten nicht alle sofort bei T = 1 gefertigt werden
            neu = gefuellt[2] + gefuellt[1]
            
            # Wenn die neue Plattenanzahl nicht mit der Kapazität übereinstimmt
            # wird diese limitiert auf die höchste Kapazität
            # und die hinzugefügten Platten werden bei der vorherigen Station abgezogen
            
            # QUALITÄTSPRÜFUNG
            if neu > q.kapazitaet:
                anzahl = gefuellt[1] - (neu - q.kapazitaet)
                gefuellt[1] -= anzahl
            else:
                anzahl = neu
                gefuellt[1] = 0
            
            for i in range(anzahl):
                platte = self.tag_suchen(2)
                # Überspringt den Prozess wenn die Platte nicht gefunden wurde
                if platte == None:
                    break
                
                # Schaut ob die Platte defekt ist
                # ...oder lässt eine Platte als defekt durchgehen wenn eine (oder mehrere) Maschine/n kaputt ist/sind
                # Chance: 50% pro Maschine
                if (random.random() < 0.5/kaputt_m[2]) or (not q.pruefen(platte).qualifiziert):
                    kaputt += 1
                    self.tag_loeschen(2)
                    
                # Ansonsten wird sie abgeschlossen
                # und aus der Liste entfernt
                else:
                    self.tag_loeschen(2)
                    abgeschlossen += 1
            
            plattenachse_q.append(gefuellt[2])
            fertigachse.append(abgeschlossen)
            
            # LÖTEN
            neu = gefuellt[1] + gefuellt[0]
            if neu > l.kapazitaet:
                anzahl = gefuellt[0] - (neu - l.kapazitaet)
                gefuellt[0] -= anzahl
            else:
                anzahl = neu
                gefuellt[0] = 0

            plattenachse_l.append(gefuellt[1])
            
            for i in range(anzahl):
                platte = self.tag_suchen(1)
                if platte == None:
                    break
                
                l.loeten(platte)
                if random.random() < 0.4/kaputt_m:
                    platte.defekt = True
                gefuellt[1] += 1
            
            # MONTAGE
            neu = gefuellt[0] + plattenzahl
            if neu > m.kapazitaet:
                anzahl = plattenzahl - (neu - m.kapazitaet)
                plattenzahl -= anzahl
            else:
                anzahl = plattenzahl
                plattenzahl = 0

            plattenachse_m.append(gefuellt[0])
            
            for i in range(anzahl):
                self.platte_einfuegen()
                platte = self.anfang
                
                m.montieren(platte)
                if random.random() < 0.2/kaputt_m:
                    platte.defekt = True
                gefuellt[0] += 1
            
            if plattenzahl <= 0:
                break
        
        print("Zum fortfahren Graph-Fenster schliessen")
        if plot:
            plotgraph(zeitachse, [plattenachse_m, plattenachse_l, plattenachse_q, fertigachse], xaxis="Zeit", yaxis="Platten")

def main():
    return

if __name__ == "__main__":
    main()
