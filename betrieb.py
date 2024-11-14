from listenelemente import *

# Der Betrieb stellt die Liste dar, die die Elemente innerhalb initialisiert und bearbeitet
class Betrieb(object):
    def __init__(self):
        self.anfang = Abschluss()
        self.montagen = []
        self.loeter = []
        self.pruefer = []

    # Fügt eine der Platten am Anfang des Betriebs ein
    def platte_einfuegen(self, platte:Platte):
        self.anfang = Platte()

    # Diese Methode gibt eine Liste mit den Kapazitaeten der jeweiligen Stationen
    # Index 0: Montagemaschinen; 1: Lötmaschinen; 2: Qualitätsprüfmaschinen
    def kapazitaeten_pruefen(self):
        m = 0
        l = 0
        q = 0

        for montage in self.montagen:
            m += montage.kapazitaet
        for loet in self.loeter:
            l += loet.kapazitaet
        for quali in self.pruefer:
            q += quali.kapazitaet

def main():
    return

if __name__ == "__main__":
    main()
