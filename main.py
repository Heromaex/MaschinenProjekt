import time
import random
import pickle
import randomname

from maschinen import *
from ui import *
from betrieb import *
from listenelemente import *

"""
Diese Datei ist dafür gedacht, das Programm zu starten und benötigte Eingaben zu visualisieren
Hierfür wird die cmd (Command Prompt) geöffnet
Um diese Funktionen zu erhalten müssen Python und die benötigten Bibliotheken installiert sein
ODER es muss eine EXE-Datei vorhanden sein, die diesen Prozess automatisch konvertiert

Bei https://www.python.org/downloads/ kann Python heruntergeladen werden mit "Download Python x.x.x"
Die cmd kann geöffnet werden indem man in der Windows Suche unten links "cmd" eingibt
Für alle benötigten, nicht vorinstallierten Bibliotheken muss "pip install [bibliothek name]" eingegeben werden

Hier eine Liste an benötigten Bibliotheken:
    - matplotlib
"""

def daten_einfuegen(datei:str, neuer_wert):
    with open(datei, "rb") as f:
        con = pickle.load(f)

    con.append(neuer_wert)

    with open(datei, "wb") as f:
        pickle.dump(con, f)

def neue_maschine(betrieb:Betrieb):
    optionen = [
    "Montage",
    "Löten",
    "Qualitätsprüfung"
    ]
    typ = prompt("Welche Maschine möchtest du hinzufügen?", optionen)
    
    print()
    print("Welche Kapazität hat die Maschine?")
    kapazitaet = int(input("(Zahl) >>> "))
    
    print()
    print("Wie viele davon möchtest du hinzufügen?")
    menge = int(input("(Zahl) >>> "))
    
    m = Maschine(kapazitaet)
    if typ == 1:
        mt = Montage(m)
    elif typ == 2:
        mt = Loeten(m)
    elif typ == 3:
        mt = Qualitaetspruefung(m)
    
    for i in range(menge):
        betrieb.maschine_hinzufuegen(mt)
    
    print()
    print("Maschine/n wurde/n erfolgreich hinzugefügt")
    
    return betrieb

def maschinen_reparieren(betrieb:Betrieb):
    maschinen_liste = [betrieb.montagen, betrieb.loeter, betrieb.pruefer]
    neue_liste = []
    for maschinen in maschinen_liste:
        neue_maschinen = []
        for m in maschinen:
            m.reparieren()
            neue_maschinen.append(m)
    
    betrieb.montagen = neue_maschinen[0]
    betrieb.loeter = neue_maschinen[1]
    betrieb.pruefer = neue_maschinen[2]
    
    return betrieb

def platte_einfuegen(betrieb:Betrieb):
    betrieb.platte_einfuegen()
    
    return betrieb

def maschinen_bearbeiten_prompt(betrieb:Betrieb):
    optionen = [
    "Neue Maschine hinzufügen",
    "Alle Maschinen reparieren",
    "Platten einfügen"
    ]
    inp = prompt("Was möchtest du mit den Maschinen machen?", optionen)
    
    if inp == 1:
        betrieb = neue_maschine(betrieb)
    elif inp == 2:
        betrieb = maschinen_reparieren(betrieb)
    elif inp == 3:
        betrieb = platte_einfuegen(betrieb)
    
    return betrieb

def testwerte_prompt(betrieb:Betrieb):
    optionen = [
        "Neue Testwerte erstellen",
        "Zufällige Testwerte erstellen",
        "Erstellen mit aktuellen Werten",
        "Testwerte nutzen",
        "Testwerte löschen"
    ]
    inp = prompt("Was möchtest du machen?", optionen)

    if inp == 1:
        return
    elif inp == 2:
        m = Maschine(random.randint(10,15))
        montage = Montage(m)
        m = Maschine(random.randint(20,30))
        loeten = Loeten(m)
        m = Maschine(random.randint(8,10))
        quali = Qualitaetspruefung(m)

        m_liste = [montage, loeten, quali]

        neuer_betrieb = Betrieb(name=randomname.get_name())
        for m in m_liste:
            for i in range(random.randint(1,10)):
                neuer_betrieb.maschine_hinzufuegen(m)

        daten_einfuegen("testdaten.pickle", neuer_betrieb)
    elif inp == 3:
        daten_einfuegen("testdaten.pickle", betrieb)
    elif inp == 4:
        with open("testdaten.pickle", "rb") as f:
            con = pickle.load(f)

        optionen = []
        for b in con:
            optionen.append(b.name)

        inp = prompt("Wähle einen gespeicherten Betrieb", optionen)
        betrieb = con[inp-1]
    elif inp == 5:
        with open("testdaten.pickle", "wb") as f:
            pickle.dump([], f)
        
    return betrieb

############################################

def simulation(betrieb:Betrieb):
    print()
    print("Starte Simulation...")
    time.sleep(0.5)
    betrieb.platten_durchschieben()

    return betrieb

############################################

def start_prompt(betrieb:Betrieb):
    optionen = [
    "Maschinen bearbeiten",
    "Simulation durchführen",
    "Werte suchen",
    "Testwerte"
    ]
    inp = prompt("Was möchtest du machen?", optionen)
    
    if inp == 1:
        betrieb = maschinen_bearbeiten_prompt(betrieb)
    elif inp == 2:
        print("Wie viele Platten möchtest du durchschieben?")
        platten_anzahl = int(input("(Zahl) >>> "))

        print("Möchtest du einen Graphen erstellt haben? (y/n)")
        plot_graph = input("(Text) >>> ").lower()

        if plot_graph == "y":
            betrieb = betrieb.platten_durchschieben(platten_anzahl)
        else:
            betrieb = betrieb.platten_durchschieben(platten_anzahl, plot=False)
    
    elif inp == 4:
        betrieb = testwerte_prompt(betrieb)
    
    return betrieb

def main(betrieb:Betrieb):
    betrieb = start_prompt(betrieb)

    return betrieb

if __name__ == "__main__":
    print("Benenne den neuen Betrieb")
    new_name = input("(Text) >>> ")
    betrieb = Betrieb()
    while True:
        betrieb = main(betrieb)
