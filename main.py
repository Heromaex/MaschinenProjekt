import time
import random
import pickle
import randomname
import sys

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
    - randomname
"""

def daten_einfuegen(datei:str, neuer_wert):
    with open(datei, "rb") as f:
        con = pickle.load(f)

    con.append(neuer_wert)

    with open(datei, "wb") as f:
        pickle.dump(con, f)

############################################

def betriebinfo(betrieb:Betrieb):
    name = betrieb.name
    betrieb_m = [betrieb.montagen, betrieb.loeter, betrieb.pruefer]
    betrieb_k = betrieb.kapazitaeten_pruefen()
    gebrochen_zahlen = []
    
    for station in betrieb_m:
        gebrochen = 0
        for m in station:
            if m.defekt:
                gebrochen += 1
        gebrochen_zahlen.append(gebrochen)
    
    infotext = f"""
Name: {name}

Maschinen:
 - Montagen: {len(betrieb_m[0])} (Gebrochen: {gebrochen_zahlen[0]})
 - Löten: {len(betrieb_m[1])} (Gebrochen: {gebrochen_zahlen[1]})
 - Prüfer: {len(betrieb_m[2])} (Gebrochen: {gebrochen_zahlen[2]})

Maschinen Kapazitäten:
 - Montage: {betrieb_k[0]}
 - Löten: {betrieb_k[1]}
 - Qualitätsprüfung: {betrieb_k[2]}
"""
    
    return infotext

############################################

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
    
############################################

def maschinen_reparieren(betrieb:Betrieb):
    maschinen_liste = [betrieb.montagen, betrieb.loeter, betrieb.pruefer]
    neue_liste = []
    for maschinen in maschinen_liste:
        neue_maschinen = []
        for m in maschinen:
            m = m.reparieren()
            neue_maschinen.append(m)
    
    betrieb.montagen = neue_maschinen[0]
    betrieb.loeter = neue_maschinen[1]
    betrieb.pruefer = neue_maschinen[2]
    
    return betrieb
    
############################################

def platte_einfuegen(betrieb:Betrieb):
    betrieb.platte_einfuegen()
    
    return betrieb

############################################

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

def testwerte_prompt(betrieb:Betrieb):
    optionen = [
        "Zufällige Testwerte erstellen",
        "Erstellen mit aktuellen Werten",
        "Testwerte nutzen",
        "Alle Testwerte löschen"
    ]
    inp = prompt("Was möchtest du machen?", optionen)
        
    if inp == 1:
        m = Maschine(random.randint(10,15))
        montage = Montage(m)
        m = Maschine(random.randint(20,30))
        loeten = Loeten(m)
        m = Maschine(random.randint(8,10))
        quali = Qualitaetspruefung(m)

        m_liste = [montage, loeten, quali]

        neuer_betrieb = Betrieb(name=randomname.get_name())
        print()
        print("Neuer Betrieb wurde erstellt")
        
        for m in m_liste:
            zufallszahl = random.randint(5,10)
            for i in range(zufallszahl):
                neuer_betrieb.maschine_hinzufuegen(m)
            print(f"{zufallszahl} von {m.art} wurden eingefügt mit Kapazität {m.kapazitaet}")

        daten_einfuegen("testdaten.pickle", neuer_betrieb)
        
    elif inp == 2:
        daten_einfuegen("testdaten.pickle", betrieb)
        
        print("Aktueller Betrieb wurde erfolgreich eingefügt")
        
    elif inp == 3:
        with open("testdaten.pickle", "rb") as f:
            con = pickle.load(f)

        optionen = []
        for b in con:
            optionen.append(b.name)

        inp = prompt("Wähle einen gespeicherten Betrieb", optionen)
        if inp == None:
            return betrieb
        betrieb = con[inp-1]
        print()
        print(f"Testbetrieb {betrieb.name} wurde erfolgreich gewählt")
        
    elif inp == 4:
        with open("testdaten.pickle", "wb") as f:
            pickle.dump([], f)
        
    return betrieb

############################################

def simulation(betrieb:Betrieb, platten_anzahl:int, do_plot:bool=True):
    print()
    print(betriebinfo(betrieb))
    print("Starte Simulation...")
    time.sleep(0.5)
    betrieb.platten_durchschieben(platten_anzahl, plot=do_plot)

    return betrieb

############################################

def start_prompt(betrieb:Betrieb):
    optionen = [
    "Maschinen bearbeiten",
    "Simulation durchführen",
    "Betrieb anschauen",
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
            betrieb = simulation(betrieb, platten_anzahl)
        else:
            betrieb = simulation(betrieb, platten_anzahl, do_plot=False)
    
    elif inp == 3:
        text = betriebinfo(betrieb)
        print(text)
    
    elif inp == 4:
        betrieb = testwerte_prompt(betrieb)
    
    return betrieb

############################################

def main(betrieb:Betrieb):
    recursion_limit = sys.getrecursionlimit()
    if recursion_limit < 2500:
        sys.setrecursionlimit(2500)
    betrieb = start_prompt(betrieb)

    return betrieb

if __name__ == "__main__":
    print("Benenne den neuen Betrieb")
    neuer_name = input("(Text) >>> ")
    betrieb = Betrieb(name=neuer_name)
    while True:
        betrieb = main(betrieb)
