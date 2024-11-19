import time

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

def neue_maschine(betrieb:Betrieb):
    optionen = [
    "Montage",
    "Löten",
    "Qualitätsprüfung"
    ]
    typ = prompt("Welche Maschine möchtest du hinzufügen?", optionen)
    
    print()
    print("Welche Kapazität hat die Maschine?")
    kapazitaet = int(input(">>> "))
    
    print()
    print("Wie viele davon möchtest du hinzufügen?")
    menge = int(input(">>> "))
    
    m = Maschine(kapazitaet)
    if typ == 1:
        mt = Montage(m)
    elif typ == 2:
        mt = Loeten(m)
    elif typ == 3:
        mt = Qualitätsprüfung(m)
    
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

############################################

def simulation(betrieb:Betrieb):
    print()
    print("Starte Simulation...")
    time.sleep(0.5)
    betrieb.platten_durchschieben()

############################################

def start_prompt(betrieb:Betrieb):
    optionen = [
    "Maschinen bearbeiten",
    "Simulation durchführen",
    "Werte suchen"
    ]
    inp = prompt("Was möchtest du machen?", optionen)
    
    if inp == 1:
        betrieb = maschinen_bearbeiten_prompt(betrieb)
    if inp == 2:
        return
    
    return betrieb

def main(betrieb:Betrieb):
    betrieb = start_prompt(betrieb)

if __name__ == "__main__":
    betrieb = Betrieb()
    while True:
        betrieb = main(betrieb)
