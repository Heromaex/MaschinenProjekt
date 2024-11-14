# MaschinenProjekt

## Einführung
Das Projekt ist das Schulprojekt vom 7.11.2024 - 21.11.2024
Das Hauptthema ist das Kompositum Liste, welches hier deutlich integriert wurde

Jede Eigenschaft des Themas wurde von Java in **Python** übersetzt
Die Installation ist NUR benötigt, wenn keine EXE-Datei vorhanden ist

## Funktionen
1. Erstellen einer **Simulation** eines Betriebs in einer IT-Firma
- Die Funktionen wurden nach der Aufgabenstellung bearbeitet
- Ein Betrieb enthält mehrere Stationen mit Maschinen wie Montage, Löten, Qualitätsprüfung (QS)
- Jede Maschine ist dafür zuständig eine Platte zu bearbeiten
- Jeder Lauf wird in Zeitschritten durchgeführt
- Ab und zu kann eine Platte defekt werden. Diese wird bei der QS als Ausschuss "gemeldet" und automatisch entfernt

2. Erstellen eines **Graphen** zur Verlaufsbeschreibung
- Ein Graph wird mit matplotlib erstellt
- Ein Koordinatensystem mit mehreren Graphen in Stationsschritte unterteilt
- Parallel wird ein Gesamtverlauf der durchgelaufenen (nicht-defekten) Platten angezeigt
- Das Koordinatensystem zeigt die Produktion in einer beliebigen Zeiteinheit T

3. Interaktives Menü
- Zum Anfang wird die cmd geöffnet
- Hier können Eingaben zu den gefragten Werten gemacht, die von der Firma bestimmt werden
- Die Eingaben werden ausgewertet und virtuell umgesetzt
- Die meisten Eingaben geben ebenfalls eine Ausgabe, die gefragte Werte und Berechnungen ausgibt

## Wie starte ich das Programm?
### Installation
Benötigte Ressourcen:
	- Python: https://www.python.org/downloads/
	- Command Prompt (cmd, windows shell, etc.)
	- Windows 10+

1. Python downloaden und installieren (**Mit** "ADD TO PATH")
- python-amd.exe öffnen
- Unten "ADD TO PATH" ankreuzen
- Weiter und Abschliessen

2. Bibliotheken installieren
- Command Prompt öffnen
	CMD:
		Unten links bei der Windowssuche "cmd" eingeben
- "pip install (bibliothek)" eingeben
	oder: "pip install requirements.txt" im Ordner mit den Dateien (in der cmd kann man mit "cd (directory)" zum Pfad wechseln)
	zweiteres funktioniert nur wenn requirements.txt vorhanden ist

Fertig!

### Ausführen des Programms
1. Explorer öffnen
2. Zum gedownloadeten Ordner gehen (normal unter /Downloads)
3. zip-Datei entpacken im gewünschten Ordner, z.B. auf dem Desktop
4. Ordner öffnen mit den Dateien
5. main.py ausführen