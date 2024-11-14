from listenelemente import *

# Der Betrieb stellt die Liste dar, die die Elemente innerhalb initialisiert und bearbeitet
class Betrieb(object):
    def __init__(self):
        # Erstellt den Abschluss
        # und setzt ihn als Anfang
        self.anfang = Abschluss()
        # Listen der Maschinen
        # Dies wird benötigt falls Maschinen mit anderen Kapazitäten existieren
        self.montagen = []
        self.loeter = []
        self.pruefer = []

    # Fügt eine neue Platte am Anfang des Betriebs ein
    def platte_einfuegen(self):
        self.anfang = Platte(self.anfang)
    
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
    
    # Eine neue Maschine in die Listen einfügen
    # Die Maschine sollte vorher erstellt werden
    def maschine_hinzufuegen(self, maschine:Maschiene):
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
        anfang = anfang.tag_loeschen(kriterium)
    
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
        zeit = 0
        
        # Iteriert jede Platte in der Liste um die Daten zu ändern
        while True:
            # Zeit wird beim Plotten gezählt um einen Verlauf darzustellen
            zeit += 1
            zeitachse.append(zeit)
            
            
            # Neue Kapazität besteht aus der eigenen und der der vorherigen Maschine
            # Umgedrehte Reihenfolge der Stationen stellt sicher, dass Platten nicht alle sofort bei T = 1 gefertigt werden
            neu = gefuellt[2] + gefuellt[1]
            
            # Wenn die neue Plattenanzahl nicht mit der Kapazität übereinstimmt
            # wird diese limitiert auf die höchste Kapazität
            # und die hinzugefügten Platten werden bei der vorherigen Station abgezogen
            if neu > kapazitaet[2]:
                anzahl = neu - kapazitaet[2]
                gefuellt[1] -= anzahl
            else:
                anzahl = gefuellt[1]
                gefuellt[1] = 0
            
            for i in range(anzahl):
                platte = self.tag_suchen(2)
                # Überspringt den Prozess wenn die Platte nicht gefunden wurde
                if platte == None:
                    break
                
                # Schaut ob die Platte defekt ist
                if not q.pruefen(platte).geprueft:
                    kaputt += 1
                    self.tag_loeschen(2)
                # Ansonsten wird sie abgeschlossen
                # und aus der Liste entfernt
                else:
                    self.tag_loeschen(2)
                    abgeschlossen += 1
            
            
            neu = gefuellt[1] + gefuellt[0]
            if neu > kapazitaet[1]:
                anzahl = neu - kapazitaet[1]
                gefuellt[0] -= anzahl
            else:
                anzahl = gefuellt[0]
                gefuellt[0] = 0
            
            for i in range(anzahl):
                platte = self.tag_suchen(1)
                if platte == None:
                    break
                
                l.loeten(platte)
            
            
            neu = gefuellt[0] + plattenzahl
            if neu > kapazitaet[0]:
                anzahl = kapazitaet[0] - gefuellt[0]
                plattenzahl -= anzahl
            else:
                anzahl = plattenzahl
                plattenzahl = 0
            
            for i in range(anzahl):
                self.platte_einfuegen()
                platte = self.anfang
                
                m.montage(platte)
    
    # Gibt die Gesamt-Kapazitäten der Stationen
    def gesamt_kapazitaet(self):
        # Zähler der jeweiligen Stations-Kapazitäten
        mk = 0
        lk = 0
        qk = 0
        
        # Fügt die Kapazität der jeweiligen Maschine zur Gesamt-Kapazität hinzu
        for m in self.montagen:
            mk += m.kapazitaet
        for l in self.loeter:
            lk += l.kapazitaet:
        for q in self.pruefer:
            qk += q.kapazitaet
        
        # Am Ende werden diese zurückgegeben zum Nutzen
        return mk, lk, qk

def main():
    return

if __name__ == "__main__":
    main()
