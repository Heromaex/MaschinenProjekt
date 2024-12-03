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

    # Zählt, wie viele Platten mit einem Kriterium existieren
    def zaehle_kriterium(self, kriterium:int):
        anzahl = self.anfang.zaehle_kriterium(kriterium)
        return anzahl

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

    # Gibt die Platte aus, die diese ID hat
    def id_suchen(self, pid:int):
        ergebnis = self.anfang.id_suchen(pid)
        return ergebnis

    # Löscht eine Platte nach ihrer ID
    def id_loeschen(self, pid:int):
        self.anfang = self.anfang.id_loeschen(pid)
    
    # Simuliert den Prozess der Fertigung der Platten
    # plot gibt an ob ein Graph erstellt werden soll
    def platten_durchschieben(self, plattenzahl:int, plot:bool=True):
        # Liste an Gesamt-Kapazitäten der Stationen, zb. [50,80,45]
        kapazitaet = self.kapazitaeten_pruefen()
        # Zähler, wie viele Platten abgeschlossen wurden
        abgeschlossen = 0
        # Zähler, wie viele Platten kaputt gegangen sind
        kaputt = 0
        # Zähler, wie viele von welchen Maschinen kaputt sind
        # Dies bestimmt, mit welcher Wahrscheinlichkeit Platten falsch sortiert werden oder zerbrochen werden
        kaputt_m = [0,0,0]
        
        # Maschinen Templates um Funktionen der Stationen zu übertragen
        startm = Maschine(kapazitaet[0])
        m = Montage(startm, cap=False)
        startl = Maschine(kapazitaet[1])
        l = Loeten(startl, cap=False)
        startq = Maschine(kapazitaet[2])
        q = Qualitaetspruefung(startq, cap=False)

        print(kapazitaet[0],kapazitaet[1],kapazitaet[2])
        
        # Zeit-Platten-Achsen um Plotten möglich zu machen
        zeitachse = []
        plattenachse_m = []
        plattenachse_l = []
        plattenachse_q = []
        fertigachse = []
        zeit = 0


        for i in range(plattenzahl):
            platte = Platte(self.anfang)
  
            self.anfang = platte
            print(f"{platte.pid} wurde erstellt")
        
        # Iteriert jede Platte in der Liste um die Daten zu ändern
        while True:
            # Zeit wird beim Plotten gezählt um einen Verlauf darzustellen
            zeit += 1
            zeitachse.append(zeit)
            print("Zeitachse verändert")
            
            # Überprüft wie viel Maschinen defekt sind
            # Wenn eine Maschine defekt ist, gibt es eine Chance dass die Platten brechen oder als kaputt abgestempelt werden
            # Wenn mehrere Maschinen kaputt sind erhöhen sich die Chancen
            for station_b in [self.montagen, self.loeter, self.pruefer]:
                for i in range(len(station_b)):
                    if station_b[i].defekt:
                        kaputt_m[i] += 1
            print(f"Kaputt: {kaputt_m}")

            # QUALITÄTSPRÜFUNG

            neu = self.zaehle_kriterium(2)
            print(f"Neu QS: {neu}")

            if neu > kapazitaet[2]:
                anzahl = q.kapazitaet
            else:
                anzahl = neu

            print(anzahl)

            plattenachse_q.append(neu-anzahl)
            try:
                fertigachse.append(fertigachse[-1] + anzahl)
            except IndexError:
                fertigachse.append(0)

            for i in range(anzahl):
                platte = self.tag_suchen(2)
                pid = platte.pid

                if platte == None:
                    break
                
                qualifiziert = q.pruefen(platte)
                if qualifiziert:
                    abgeschlossen += 1
                    self.id_loeschen(pid)
                    print("Platte wurde abgeschlossen")
                else:
                    kaputt += 1
                    self.id_loeschen(pid)
                    print("Platte wurde aussortiert")
                    continue

            # LÖTEN

            neu = self.zaehle_kriterium(1)
            print(f"Neu LÖ: {neu}")

            if neu > kapazitaet[1]:
                anzahl = kapazitaet[1]
            else:
                anzahl = neu

            plattenachse_l.append(neu-anzahl)

            for i in range(anzahl):
                platte = self.tag_suchen(1)
                if platte == None:
                    break
                l.loeten(platte)
                

            # MONTAGE

            neu = self.zaehle_kriterium(0)
            print(f"Neu MT: {neu}")

            if neu > m.kapazitaet:
                anzahl = m.kapazitaet
            else:
                anzahl = neu

            plattenachse_m.append(neu-anzahl)

            for i in range(anzahl):
                platte = self.tag_suchen(0)
                if platte == None:
                    break

                m.montieren(platte)
            
            #if self.zaehle_kriterium(0) <= 0:
            #    break

        print(f"Montage: {plattenachse_m}")
        print(f"Löten: {plattenachse_l}")
        print(f"QS: {plattenachse_q}")
        
        print("Zum fortfahren Graph-Fenster schliessen")
        if plot:
            print(zeitachse)
            print(plattenachse_l)
            print(plattenachse_m)
            print(plattenachse_q)
            print(fertigachse)
            plotgraph(zeitachse, [plattenachse_m, plattenachse_l, plattenachse_q, fertigachse], xaxis="Zeit", yaxis="Platten")

def main():
    return

if __name__ == "__main__":
    main()
